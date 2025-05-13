from fastapi import FastAPI, Query
from app.config import settings

app = FastAPI(title=settings.app_name)

# Sample distortion keywords
distortion_keywords = {
    "all-or-nothing": ["never", "always", "every time", "all"],
    "catastrophizing": ["disaster", "ruined", "worst", "terrible"],
    "mind reading": ["they think", "they hate", "they must"],
    "should statements": ["should", "must", "have to"],
    "labeling": ["i'm a failure", "i'm stupid", "i'm worthless"],
    "overgeneralization": ["nothing ever", "everything", "everyone"],
    "mental filter": ["focus on my mistakes", "only see", "ignore the good"],
    "personalization": ["my fault", "because of me", "i caused"],
}


@app.get("/")
def root():
    return {"message": f"Welcome to {settings.app_name}"}


@app.post("/check-distortion")
def check_distortion(thought: str = Query(..., min_length=5)):
    found = []
    lower_thought = thought.lower()

    for distortion, keywords in distortion_keywords.items():
        for keyword in keywords:
            if keyword in lower_thought:
                found.append(distortion)
                break

    return {"input": thought, "distortion": found if found else []}
