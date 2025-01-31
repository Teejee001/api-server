from fastapi import FastAPI
from datetime import datetime
import os
import uvicorn

app = FastAPI()

@app.get("/")
def get_info():
    return {
        "email": "Olatunjibalogun025@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Teejee001/api-server"
    }

if _name_ == "_main_":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)



