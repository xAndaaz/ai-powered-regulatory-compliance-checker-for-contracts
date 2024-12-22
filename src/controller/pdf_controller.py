from fastapi import APIRouter, UploadFile, HTTPException
from src.manager.pdf_manager import PDFManager
from src.models.pdf_model import PDFResponse

router = APIRouter()

@router.post("/ingest-pdf/", response_model=PDFResponse)
async def ingest_pdf(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="File must be a PDF")
    
    pdf_manager = PDFManager()
    result = await pdf_manager.process_pdf(file)
    return result
