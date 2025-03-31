from django.shortcuts import render
from users.algorithms import Board as alpha_beta_Board
from users.stockfish import ChessAI
from django.http import JsonResponse
from django.http import HttpResponse
import json
import chess
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def handle_moves(request):
    return render(request, 'index.html')
def reset_board(request):
    global board
    global alpha_beta_board
    alpha_beta_board = alpha_beta_Board()
    board = chess.Board()
    return JsonResponse({'success': True, 'message': 'Board reset successfully'})
alpha_beta_board = alpha_beta_Board()
board = chess.Board()

def test(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            
            moves = data.get('moves', [])
            n = len(moves)
            if len(moves) > 0:
                text = moves[n-1]
                alpha_beta_board.make_move(text)
                best_move, best_value = alpha_beta_board.get_bestMove(depth=4, maximize=False)
                alpha_beta_board.make_move(best_move)
                # Process the moves array as needed
                # For this example, we'll just echo the best move back in the response
                response_data = {'success': True, 'best_move': best_move}
            else:
                response_data = {'success': False, 'error': 'Empty moves array'}

            return JsonResponse(response_data)
        
        except json.JSONDecodeError as e:
            # Handle JSON decoding error
            response_data = {'success': False, 'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)
    # If the request method is not POST, return an error response
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# Tạo instance của ChessAI ở đâu đó có thể truy cập được, ví dụ ở đầu file
chess_ai = ChessAI(r"stockfish\stockfish-windows-x86-64-avx2.exe")

def stockfish_moves(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            moves = data.get('moves', [])
            n = len(moves)
            if len(moves) > 0:
                text = moves[n-1]
                board.push_san(text)  # Giả sử `board` là một instance của `chess.Board` đang được theo dõi
                best_move = chess_ai.get_best_move(board)  # Sử dụng Stockfish để lấy nước đi tốt nhất
                board.push_san(best_move)  # Thực hiện nước đi
                response_data = {'success': True, 'best_move': best_move}
            else:
                response_data = {'success': False, 'error': 'Empty moves array'}
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            response_data = {'success': False, 'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
def match_moves(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            moves = data.get('moves', [])
            if alpha_beta_board.board.turn == chess.WHITE:
                best_move, best_value = alpha_beta_board.get_bestMove(depth=3, maximize=True)
                white_move = best_move
                alpha_beta_board.make_move(white_move)
                response_data = {'success': True, 'best_move': white_move}
            else:
                best_move, best_value = alpha_beta_board.get_bestMove(depth=3, maximize=False)
                black_move = best_move
                alpha_beta_board.make_move(black_move)
                response_data = {'success': True, 'best_move': black_move}
            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            response_data = {'success': False, 'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)