from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import uvicorn
from RPS.RPS_Game import get_result

# APP configurations
app = FastAPI()
host = '127.0.0.1'
port = 8000 

origins = [
    "http://127.0.0.1:3001",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/')
async def index():
    routes = app.openapi()["paths"]
    endpoints = [route for route in routes.keys()]
    return endpoints

@app.get('/RPS')
async def index():
    return {
        "/random",
        "/save_result"
    }

@app.get('/RPS/random')
async def get_random_move():
    """
    Bla
    """
    return {'move': np.random.choice(['rock', 'paper', 'scissors'])}


@app.post("/RPS/save_results")
async def save_result(json_data: dict):
    """
    Bla
    """
    print("here")
    print(json_data)
    player_1_move = json_data['Player1Move']
    player_2_move = json_data['Player2Move']
    result = get_result(player_1_move, player_2_move)
    return {
        "player_1_move": player_1_move,
        "player_2_move": player_2_move,
        "result": result
    }

if __name__ == "__main__":
    print(f'running on http://{host}:{port}')
    uvicorn.run("main:app", host=host, port=port, reload=True)