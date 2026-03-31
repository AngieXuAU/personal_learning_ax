
import sys

legal_moves = {"scissors", "paper", "rock"}

def determine_winner(p1_move, p2_move):
    if p1_move == "scissors" and p2_move == "paper":
        return "Player 1"
    elif p1_move == "rock" and p2_move == "scissors":
        return "Player 1"
    elif p1_move == "paper" and p2_move == "rock":
        return "Player 1"
    
    return "Player 2"

if len(sys.argv) == 3:

    p1 = sys.argv[1]
    p2 = sys.argv[2]

    if p1 not in legal_moves or p2 not in legal_moves:
        print("Enter legal moves (scissors, paper or rock) only!")
        exit()

    if p1 == p2:
        print("It's a tie!")
    else:
        print(f"{determine_winner(p1, p2)} wins!")

else:
    print("Invalid input. Make sure you enter two arguments")
