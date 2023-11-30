"""

Module - rps_game

This module holds functions associated with ingame running of Rock Paper Scissors (rps)

--------
METHODS

get_results:

"""

def get_result(player1: str,player2: str) -> int:
    """
    Calculates which player wins at RPS

    Args:
        player1 (str): 
        player2 (str):

    Returns (int):
        0: Draw
        1: Player1 wins
        2: Player2 wins
    """
    if player1 == player2:
        return 0
    if player1 == 'rock':
        if player2 == 'paper':
            return 2
        return 1
    if player1 == 'paper':
        if player2 == 'scissors':
            return 2
        return 1
    if player1 == 'scissors':
        if player2 == 'rock':
            return 2
        return 1
