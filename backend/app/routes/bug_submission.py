from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.services.file_service import extract_text

router = APIRouter()


class BugReport(BaseModel):
    bug_text: str


@router.post("/submit-bug")
def submit_bug(report: BugReport):

    return {
        "status": "success",
        "received_bug": report.bug_text,
        "message": "Bug report received successfully."
    }


@router.post("/upload-bug")
async def upload_bug(file: UploadFile = File(...)):

    upload_folder = "app/uploads"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text(file_path)

    return {
        "filename": file.filename,
        "content": extracted_text
    }