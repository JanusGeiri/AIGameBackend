def get_result(player1,player2):
    """
    Calculates which player wins at RPS
    0 -- Draw
    1 -- Player1 wins
    2 -- Player2 wins
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
