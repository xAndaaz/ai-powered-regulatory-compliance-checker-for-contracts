from fastapi import APIRouter, HTTPException, UploadFile
from src.manager.extraction_manager import ExtractionManager

router = APIRouter()

@router.post("/extract-data/")
async def extract_data(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")

    extraction_manager = ExtractionManager()
    try:
        chunks = await extraction_manager.extract_and_chunk(file)
        return {"message": "Data extracted and chunked successfully", "chunks": chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Extraction error: {str(e)}")