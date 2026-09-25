from fastapi import FastAPI

app = FastAPI()

failure_mode = False


@app.get("/")
def root():
    return {"message": "Self-Healing DevOps Platform is running!"}


@app.get("/health")
def health():
    if failure_mode:
        return {"status": "unhealthy"}, 500

    return {"status": "healthy"}


@app.post("/simulate-failure")
def simulate_failure():
    global failure_mode
    failure_mode = True
    return {"message": "Failure simulation enabled"}


@app.post("/recover")
def recover():
    global failure_mode
    failure_mode = False
    return {"message": "Failure simulation disabled"}
