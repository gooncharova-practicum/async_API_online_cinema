import random
from http import HTTPStatus

import aiohttp
import allure
import pytest

from ..core.settings import ES_HOST
from ..models import Genre
from ..mylib import Assert

GENRES_URL = "/genres/"
genre_model = Genre


@allure.title("Available genre")
@pytest.mark.asyncio
async def test_genre_available(make_get_request):
    response = await make_get_request(GENRES_URL, {})
    Assert(response).status_code(HTTPStatus.OK)


@allure.title("Count genres consist")
@pytest.mark.asyncio
async def test_genres_count_consist(make_get_request):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{ES_HOST}{GENRES_URL}_count") as es_resp:
            resp = await make_get_request(GENRES_URL, {})
            es_response = (await es_resp.json())["count"]
            Assert(resp).body_len_is(es_response)


@allure.title("Genres")
@pytest.mark.asyncio
async def test_genres(make_get_request):
    genres_data = await make_get_request(GENRES_URL, {})
    idx = random.randrange(len(genres_data.body))
    the_jenre_id = f'{GENRES_URL}{genres_data.body[idx]["id"]}'
    result = await make_get_request(the_jenre_id, {})
    Assert(result).status_code_not_equal(HTTPStatus.OK)


@allure.title("Incorrect genres")
@pytest.mark.asyncio
async def test_incorrect_genres(make_get_request):
    genres_data = await make_get_request(GENRES_URL, {})
    idx = random.randrange(len(genres_data.body))
    the_jenre_id = f'{GENRES_URL}{genres_data.body[idx]["id"]}'
    bad_result = await make_get_request(f"{the_jenre_id}-badGenre", {})
    Assert(bad_result).status_code_not_equal(HTTPStatus.OK)


@allure.title("Data type validating")
@pytest.mark.asyncio
async def test_data_types(make_get_request):
    genres_data = await make_get_request(GENRES_URL, {})
    idx = random.randrange(len(genres_data.body))
    the_jenre_id = f'{GENRES_URL}{genres_data.body[idx]["id"]}'
    result = await make_get_request(the_jenre_id, {})
    assert genre_model(id=result.body["id"], name=result.body["name"])
