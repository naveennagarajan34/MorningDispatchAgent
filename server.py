from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import build_morning_briefing

app = FastAPI(title="Morning Dispatch API")

# Allow your mobile frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {"status": "online", "service": "Morning Dispatch Backend"}


@app.get("/api/dispatch")
def get_dispatch():
    """
    Triggers the weather + news synthesis and returns structured JSON to the mobile app.
    """
    briefing_text = build_morning_briefing()
    return {"success": True, "dispatch": briefing_text}
