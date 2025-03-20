# filepath: /Users/rakko/UserDocuments/Studies/University/Year3/Semester2/DES422_BusinessApplicationDevelopment/TestProject/backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from supabase import create_client, Client

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Add CORS middleware
origins = [
    "http://localhost:3000",  # React development server
    "https://test-app-init-frontend-production.up.railway.app",  # Your deployed frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI Backend with Supabase"}

@app.get("/users")
def get_users():
    response = supabase.table("users").select("*").execute()
    return response