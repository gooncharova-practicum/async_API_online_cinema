from http import HTTPStatus

import allure
import pytest

from ..mylib import Assert


FILMS_URL = "/films/"


@allure.title("Get all films")
@pytest.mark.asyncio
async def test_get_all_films(make_get_request):
    response = await make_get_request(FILMS_URL, {})
    Assert(response).status_code(HTTPStatus.OK).body_len_is(10)


@allure.title("Paging film")
@pytest.mark.asyncio
@pytest.mark.parametrize(("page_size", "page_number"), ((1, 1), (1, 2), (50, 1)))
async def test_paging_film(make_get_request, page_size, page_number):
    response = await make_get_request(
        FILMS_URL, {"page[number]": page_number, "page[size]": page_size}
    )
    Assert(response).status_code(HTTPStatus.OK).body_len_is(page_size)


@allure.title("Paging film by invalid page")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("page_number", "page_size"),
    (
        (0, 1),
        (1, 0),
        (-1, 1),
        (1, -1),
    ),
)
async def test_paging_film_by_invalid_page(make_get_request, page_number, page_size):
    response = await make_get_request(
        f"{FILMS_URL}search/", {"page[number]": page_number, "page[size]": page_size}
    )
    Assert(response).status_code(HTTPStatus.UNPROCESSABLE_ENTITY)


@allure.title("Search unkown film")
@pytest.mark.asyncio
async def test_search_unknown_film(make_get_request):
    response = await make_get_request(f"{FILMS_URL}search/", {"query": "UnknownFilm"})
    Assert(response).status_code(HTTPStatus.OK).body_len_is(0)


@allure.title("Filter film by unknown genre")
@pytest.mark.asyncio
async def test_filter_film_by_unknown_genre(make_get_request):
    response = await make_get_request(FILMS_URL, {"filter[genre]": "unknown_genre"})
    Assert(response).status_code(HTTPStatus.OK).body_len_is(0)
