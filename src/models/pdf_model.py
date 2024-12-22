from pydantic import BaseModel

class PDFResponse(BaseModel):
    file_name: str
    num_pages: int
