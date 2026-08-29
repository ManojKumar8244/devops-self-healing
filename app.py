from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Self-Healing DevOps Platform is running!"}


@app.get("/health")
def health():
    return {"status": "healthy"}
