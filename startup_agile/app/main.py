from fastapi import HTTPException, APIRouter
from app.models.entities import ResumeMatch
from app.models.database import SessionLocal
from app.services.ranker import rank_resume
from app.services.photo_check import check_photo
from app.models.schemas import RankRequest, RankResponse
from sqlalchemy.engine import Engine
import traceback
from fastapi import FastAPI
from app.routes import router as rank_router

app = FastAPI(title="StartUp Agile --- Mini Resume Ranker")
app.include_router(rank_router, prefix="/v1")
@app.get("/health")
def health():
    return {"status": "ok"}
print("📋 Routes registered:")
for route in app.routes:
    print("  ", route.path)


@app.get("/test")
def test():
    print("/test endpoint hit", flush=True)
    return {"message": "Router is working"}

@app.post("/rank", response_model=RankResponse)
async def rank(request: RankRequest):
    print("🧠 rank() called")
    try:
        with SessionLocal() as db:
            engine = db.get_bind()
            if isinstance(engine, Engine):
                print("🚀 Using DB:", engine.url)

            result = rank_resume(request.resume, request.job_description)

            photo_check_result = None
            if request.photo:
                photo_check_result = check_photo(request.photo)
                result.update(photo_check_result)
            else:
                result["photo_check"] = None

            record = ResumeMatch(
                resume=request.resume,
                job_description=request.job_description,
                score=result["score"],
                feedback=result["feedback"],
                photo_check=result["photo_check"],
                image_base64=request.photo
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
