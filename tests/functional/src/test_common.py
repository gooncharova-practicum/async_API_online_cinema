from http import HTTPStatus

import allure
import pytest

from ..mylib import Assert


@allure.title("Missing routes")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    "route, response_body",
    (
        ("/wrong_route", {"detail": "Not Found"}),
        ("/film/random_id", {"detail": "Film with uuid 'random_id' was not found."}),
        ("/persons/random_id", {"detail": "person not found"}),
        ("/persons/random_id/film", {"detail": "person not found"}),
        ("/genres/random_id", {"detail": "genre not found"}),
    ),
)
async def test_missing_routes(make_get_request, route, response_body):
    response = await make_get_request(route)
    Assert(response).status_code(HTTPStatus.NOT_FOUND).body(response_body)
