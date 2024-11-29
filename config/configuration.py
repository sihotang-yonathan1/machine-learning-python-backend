from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


BASE_PATH = '/api/v1'

app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, use specific URLs for more security
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)