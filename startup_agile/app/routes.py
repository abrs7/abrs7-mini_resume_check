from fastapi import APIRouter, HTTPException
from app.models.schemas import RankRequest, RankResponse
from app.services.ranker import rank_resume
from app.services.routes import check_photo

router = APIRouter()

@router.post("/rank", response_model=RankResponse)
async def rank(request: RankRequest):
    try:
        result = rank_resume(request.resume, request.job_description)
        if request.photo:
            photo_result = check_photo(request.photo)
            result.update(photo_result)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
