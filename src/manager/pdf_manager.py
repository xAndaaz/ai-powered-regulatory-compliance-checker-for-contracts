from src.config.settings import settings
from src.utils.file_validator import validate_file_type
from src.models.pdf_model import PDFResponse

class PDFManager:
    async def process_pdf(self, file):
        try:
            # Validate the file type
            validate_file_type(file.content_type, settings.ALLOWED_FILE_TYPE)
            
            # Example: Reading file content (further processing can be added here)
            content = await file.read()
            num_pages = len(content)  # Dummy logic to replace with actual PDF parsing
            
            return PDFResponse(file_name=file.filename, num_pages=num_pages)
        except Exception as e:
            raise ValueError(f"Error processing PDF: {str(e)}")
