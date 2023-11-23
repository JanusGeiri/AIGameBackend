from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def yomama():
    return "Yomama so fat"

