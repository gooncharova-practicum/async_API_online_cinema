from typing import List
from pydantic import UUID4

from fastapi import APIRouter, Depends

from .genre_models import Genre
from services.genre import GenreService, get_genre_service

router = APIRouter()


@router.get("/{genre_id:uuid}/", response_model=Genre, description="Get genre info")
async def genre_details(
    genre_id: UUID4, genre_service: GenreService = Depends(get_genre_service)
) -> Genre:
    return await genre_service.get_genre(genre_id)


@router.get("/", response_model=List[Genre], description="Get genres list")
async def genre_list(
    genre_service: GenreService = Depends(get_genre_service),
) -> List[Genre]:
    return await genre_service.get_all_genres()
