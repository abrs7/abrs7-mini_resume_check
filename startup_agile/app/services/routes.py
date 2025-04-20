from fastapi import HTTPException, APIRouter
from app.models.entities import ResumeMatch
from app.models.database import SessionLocal
from app.services.ranker import rank_resume
from app.services.photo_check import check_photo
from app.models.schemas import RankRequest, RankResponse
from sqlalchemy.engine import Engine
import traceback

router = APIRouter()
print("📦 Router file loaded", flush=True)


@router.get("/test")
def test():
    print("🚨 /test endpoint hit", flush=True)
    return {"message": "Router is working"}


@router.post("/rank", response_model=RankResponse)
async def rank(request: RankRequest):
    print("🧠 rank() called")

    print("###############")
    try:
        # Start DB session
        with SessionLocal() as db:
            # DEBUG: Print DB URL
            engine = db.get_bind()
            if isinstance(engine, Engine):
                print("🚀 Using DB:", engine.url)

            # Run ranker logic
            result = rank_resume(request.resume, request.job_description)

            if request.photo:
                photo_result = check_photo(request.photo)
                result.update(photo_result)
            else:
                result["photo_check"] = None

            # Save to DB
            record = ResumeMatch(
                resume=request.resume,
                job_description=request.job_description,
                score=result["score"],
                feedback=result["feedback"],
                photo_check=result["photo_check"]
            )
            db.add(record)
            db.commit()
            db.refresh(record)
            print(f"✅ Saved to DB: {record}")

        return result

    except Exception as e:
        print("🔥 ERROR:", str(e))
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
