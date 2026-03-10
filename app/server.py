from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/feed.xml")
async def get_feed():
    return FileResponse("feed.xml", media_type="application/xml")