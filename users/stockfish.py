import chess
from stockfish import Stockfish

class ChessAI:
    def __init__(self, path_to_engine):
        self.engine = Stockfish(path_to_engine)
        self.engine.set_skill_level(50)  # Bạn có thể điều chỉnh mức độ theo ý muốn

    def get_best_move(self, board):
        fen = board.fen()
        self.engine.set_fen_position(fen)
        return self.engine.get_best_move()

if __name__ == "__main__":
    
    board = chess.Board()
    ai = ChessAI(r"stockfish\stockfish-windows-x86-64-avx2.exe")  # Thay đổi đường dẫn tới Stockfish phù hợp

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            best_move = ai.get_best_move(board)
            board.push_san(best_move)
            print("AI's Move:", best_move)
        else:
            print(board)
            user_move = input("Enter your move (e.g., 'e2e4'): ")
            try:
                board.push_san(user_move)
            except ValueError:
                print("Invalid move. Try again.")

    # Game over, print the result
    print("Game Over. Result:", board.result())
