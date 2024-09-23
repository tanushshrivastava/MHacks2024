from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

feature_state = False

@app.get("/api/message")
def read_message():
    return {"message": "Hello from FastAPI!"}

@app.get("/api/time")
def get_time():
    return {"time": datetime.now().isoformat()}

@app.get("/api/toggle")
def toggle_feature():
    global feature_state
    feature_state = not feature_state
    return {"featureEnabled": feature_state}
