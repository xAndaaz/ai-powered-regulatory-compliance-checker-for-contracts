from PyPDF2 import PdfReader
from typing import List

class ExtractionManager:
    async def extract_and_chunk(self, file) -> List[str]:
        # Read the PDF content
        pdf_reader = PdfReader(file.file)
        text = " ".join(page.extract_text() for page in pdf_reader.pages)

        # Perform semantic chunking (dummy example, adjust as needed)
        chunks = self.semantic_chunking(text)
        return chunks

    def semantic_chunking(self, text: str) -> List[str]:
        # Example: Split into chunks of 500 characters
        chunk_size = 500
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
