from fastapi import FastAPI
from app.routes import bug_submission

app = FastAPI(
    title="AI Smart Bug Analyzer & Fix Advisor",
    description="Infosys Virtual Internship Project",
    version="1.0.0"
)

app.include_router(bug_submission.router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Smart Bug Analyzer & Fix Advisor!",
        "status": "Backend is running successfully."
    }