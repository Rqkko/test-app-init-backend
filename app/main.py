from fastapi import FastAPI
import os
from supabase import create_client, Client

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")
def read_root():
    return {"message": "FastAPI Backend with Supabase"}

@app.get("/users")
def get_users():
    response = supabase.table("users").select("*").execute()
    return response