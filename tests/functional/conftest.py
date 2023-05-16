from dataclasses import dataclass

import pytest_asyncio
import aiohttp

from .core import BASE_URL


@dataclass
class HTTPResponse:
    body: dict
    headers: dict
    status: int


@pytest_asyncio.fixture
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest_asyncio.fixture
def make_get_request(session):
    async def inner(route: str, params: dict = None) -> HTTPResponse:
        url = f"{BASE_URL}{route}"
        async with session.get(url, params=params) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status=response.status,
            )

    return inner
