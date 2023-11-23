#   // {"move": "rock" || "paper" || "scissors"}
  
#   //Send result to compute
#   //POST backendurl/RPS/saveResults
  
# { 
#   Player1Move: r || p || s, 
#   Player2Move: r || p || s, 
#   result:      0 || 1 || 2 
# }

from fastapi import FastAPI
import numpy as np
from RPS.RPS_Game import get_result

app = FastAPI()

@app.get('/RPS/random')
async def get_random_move():
    """
    Bla
    """
    return {'move': np.random.choice(['rock','paper','scissors'])}

@app.post("/RPS/save_results")
async def save_result(json_data : dict):
    """
    Bla
    """
    player_1_move = json_data['Player1Move']
    player_2_move = json_data['Player2Move']
    result = get_result(player_1_move,player_2_move)
    return {
        "status" : "SUCCESS",
        "player_1_move": player_1_move,
        "player_2_move": player_2_move,
        "result": result
    }
