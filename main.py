from fastapi import FastAPI
from src.controller import pdf_controller

app = FastAPI()

# Include the router
app.include_router(pdf_controller.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
