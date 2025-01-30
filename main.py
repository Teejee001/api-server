from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def get_info():
    return {
        "email": "Olatunjibalogun025@gmail.com",  
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Teejee001/api-server" 
    }

