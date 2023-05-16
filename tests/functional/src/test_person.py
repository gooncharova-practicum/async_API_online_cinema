import uuid
from http import HTTPStatus

import allure
import pytest

from ..mylib import Assert

PERSONS_URL = "/persons/"


@allure.title("Get person by unknown id")
@pytest.mark.asyncio
async def test_get_unknown_person(make_get_request):
    unknown_uuid = str(uuid.uuid4())
    response = await make_get_request(f"{PERSONS_URL}{unknown_uuid}/")
    Assert(response).status_code(HTTPStatus.OK).body_len_is(0)


@allure.title("Get list of films by unknown person id")
@pytest.mark.asyncio
async def test_get_person_film_details(make_get_request):
    unknown_uuid = str(uuid.uuid4())
    response = await make_get_request(f"{PERSONS_URL}{unknown_uuid}/film")
    Assert(response).status_code(HTTPStatus.OK).body_len_is(0)


@allure.title("Search unkown person")
@pytest.mark.asyncio
async def test_search_unknown_person(make_get_request):
    response = await make_get_request(
        f"{PERSONS_URL}search/", {"query": "UnknownPerson"}
    )
    Assert(response).status_code(HTTPStatus.OK).body_len_is(0)


@allure.title("Paging persons by invalid page")
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
async def test_paging_persons_by_invalid_page(make_get_request, page_number, page_size):
    response = await make_get_request(
        f"{PERSONS_URL}search/", {"page[number]": page_number, "page[size]": page_size}
    )
    Assert(response).status_code(HTTPStatus.UNPROCESSABLE_ENTITY)
