# Local Dev

Install dependencies in the requirements.txt:
  `pip install -r requirements.txt`

Use uvicorn to run FastAPI application:
  `uvicorn app.main:app --host 0.0.0.0 --port 8000`


# Dev with Docker:

Build the image
  `docker build -t my-backend-app .`

Run the container
  `docker run -p 8000:8000 --env-file .env my-backend-app`