from app.services.ranker import rank_resume

def test_rank_resume_mock():
    result = rank_resume("Python developer", "Looking for Python backend dev")
    assert isinstance(result["score"], int)
    assert "feedback" in result
