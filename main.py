from fastapi import FastAPI
from src.controller import pdf_controller, extraction_controller, embedding_controller

app = FastAPI()

# Include routers
app.include_router(pdf_controller.router, prefix="/api/v1")
app.include_router(extraction_controller.router, prefix="/api/v1")
app.include_router(embedding_controller.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
