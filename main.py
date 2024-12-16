from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional
import os
from src.utils.extract_text_from_pdf import extract_text_from_pdf
from src.utils.chunking import chunk_docs
from src.utils.embeddings_generator import generate_embeddings
from src.utils.pinecone_handler import create_vectorstore
from src.utils.faiss_handler import store_in_faiss

app = FastAPI()

UPLOAD_DIR = os.path.abspath(os.path.join("docs"))
FAISS_INDEX_PATH = os.path.abspath(os.path.join("data", "faiss_index.index"))


class StepStatus(BaseModel):
    step: str
    status: str
    message: Optional[str] = None
    error: Optional[str] = None


class APIResponse(BaseModel):
    overall_status: str
    steps: list[StepStatus]


@app.get("/")
def index():
    return {"msg": "Welcome !!"}


@app.post("/process-pdf/", response_model=APIResponse)
async def process_pdf(file: UploadFile = File()):
    steps = []

    try:
        # PDF Ingestion and Validation
        if not file.filename.endswith(".pdf"):
            raise ValueError("Invalid file type. Please upload a PDF.")

        # Get the size of the uploaded file
        file.file.seek(0, os.SEEK_END)  # Move pointer to the end
        file_size = file.file.tell()  # Get file size
        file.file.seek(0)  # Reset pointer to the start
        if file_size > 50 * 1024 * 1024:  # 50 MB
            raise ValueError("PDF too large. Should be less than 50MB.")

        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        steps.append(
            StepStatus(
                step="PDF Upload", status="success", message="PDF uploaded successfully"
            )
        )

        # PDF extraction
        try:
            docs = extract_text_from_pdf()
            steps.append(
                StepStatus(
                    step="Text Extraction",
                    status="success",
                    message=f"Extracted {len(docs)} characters",
                )
            )
        except Exception as e:
            raise ValueError(f"Text extraction failed: {str(e)}")

        # Chunk extracted text
        try:
            split_docs = chunk_docs(docs)
            steps.append(
                StepStatus(
                    step="Text Chunking",
                    status="success",
                    message=f"Generated {len(split_docs)} chunks",
                )
            )
        except Exception as e:
            raise ValueError(f"Text chunking failed: {str(e)}")

        # Generate embeddings
        try:
            embeddings = generate_embeddings(split_docs)
            steps.append(
                StepStatus(
                    step="Embedding Generation",
                    status="success",
                    message="Embeddings generated successfully",
                )
            )
        except Exception as e:
            raise ValueError(f"Embedding generation failed: {str(e)}")

        # Initialize and store in Pinecone
        try:
            index_name = "infy"
            vector_store = create_vectorstore(
                index_name=index_name, split_docs=split_docs
            )

            steps.append(
                StepStatus(
                    step="Vector Store",
                    status="success",
                    message="Stored embeddings in Pinecone",
                )
            )

            # Store locally in FAISS
            store_in_faiss(embeddings, FAISS_INDEX_PATH)
            steps.append(
                StepStatus(
                    step="Local FAISS Store",
                    status="success",
                    message="Stored embeddings in local FAISS index",
                )
            )

        except Exception as e:
            raise ValueError(f"Vector storage failed: {str(e)}")

        return APIResponse(overall_status="success", steps=steps)

    except Exception as e:
        steps.append(StepStatus(step="Failure", status="failed", error=str(e)))
        return APIResponse(overall_status="failed", steps=steps)