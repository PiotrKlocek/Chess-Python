import pygame
import tkinter as tk
from tkinter import messagebox
from pawn import Pawn
from queen import Queen
from king import King
from rook import Rook
from knight import Knight
from bishop import Bishop

pygame.init()

size = (640, 640)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chess")
icon = pygame.image.load('images/black_king.png')
pygame.display.set_icon(icon)
block_size = 80
selected_square = None
selected_piece = None
possible_moves = []

white = (255, 255, 255)
black = (0, 0, 0)
green = (60, 165, 60)
light_grey = (220, 220, 220)

pieces = []
removed_white_pieces = []
removed_black_pieces = []


for col in range(8):
    pieces.append(Pawn("white", (col, 6), 'images/white_pawn.png'))

for col in range(8):
    pieces.append(Pawn("black", (col, 1), 'images/black_pawn.png'))

pieces.append(Queen("black", (3, 0), 'images/black_queen.png'))
pieces.append(Queen("white", (3, 7), 'images/white_queen.png'))
pieces.append(King("white", (4, 7), 'images/white_king.png'))
pieces.append(King("black", (4, 0), 'images/black_king.png'))
pieces.append(Rook("black", (0, 0), 'images/black_rook.png'))
pieces.append(Rook("black", (7, 0), 'images/black_rook.png'))
pieces.append(Rook("white", (0, 7), 'images/white_rook.png'))
pieces.append(Rook("white", (7, 7), 'images/white_rook.png'))
pieces.append(Knight("white", (1, 7), 'images/white_knight.png'))
pieces.append(Knight("white", (6, 7), 'images/white_knight.png'))
pieces.append(Knight("black", (1, 0), 'images/black_knight.png'))
pieces.append(Knight("black", (6, 0), 'images/black_knight.png'))
pieces.append(Bishop("black", (5, 0), 'images/black_bishop.png'))
pieces.append(Bishop("black", (2, 0), 'images/black_bishop.png'))
pieces.append(Bishop("white", (5, 7), 'images/white_bishop.png'))
pieces.append(Bishop("white", (2, 7), 'images/white_bishop.png'))

current_turn = "white"


def draw_board():
    screen.fill(light_grey)
    font = pygame.font.SysFont(None, 30)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = ['8', '7', '6', '5', '4', '3', '2', '1']

    for row in range(8):
        for col in range(8):
            color = white if (row + col) % 2 == 0 else green
            pygame.draw.rect(screen, color, pygame.Rect(col * block_size, row * block_size, block_size, block_size))

            if col == 0:
                label = font.render(numbers[row], True, black if color == white else white)
                screen.blit(label, (col * block_size + 5, row * block_size + 5))
            if row == 7:
                label = font.render(letters[col], True, black if color == white else white)
                screen.blit(label, (col * block_size + block_size - 15, row * block_size + block_size - 30))

    pygame.draw.rect(screen, black, pygame.Rect(0, 0, 8 * block_size, 8 * block_size), 2)

    if selected_square:
        row, col = selected_square
        pygame.draw.rect(screen, black, pygame.Rect(col * block_size, row * block_size, block_size, block_size), 2)

    for piece in pieces:
        piece.draw(screen)

    for move in possible_moves:
        x, y = move
        if current_turn == "black":
            pygame.draw.circle(screen, (0, 0, 0), (x * block_size + block_size // 2, y * block_size + block_size // 2),
                               8)
        else:
            pygame.draw.circle(screen, (128, 128, 128),
                               (x * block_size + block_size // 2, y * block_size + block_size // 2), 8)


def get_square(pos):
    x, y = pos
    col = x // block_size
    row = y // block_size
    return row, col


def remove_captured_piece(row, col):
    for piece in pieces:
        if piece.position == (col, row):
            if piece.color == "white":
                removed_white_pieces.append(piece)
            else:
                removed_black_pieces.append(piece)
            pieces.remove(piece)
            break


def is_in_check(king_color, pieces):
    king_position = None
    for piece in pieces:
        if isinstance(piece, King) and piece.color == king_color:
            king_position = piece.position
            break

    if not king_position:
        return False

    for piece in pieces:
        if piece.color != king_color and king_position in piece.get_possible_moves(pieces):
            return True

    return False


def is_checkmate(king_color, pieces):
    if not is_in_check(king_color, pieces):
        return False

    for piece in pieces:
        if piece.color == king_color:
            valid_moves = get_possible_moves_with_check_prevention(piece, pieces)
            if valid_moves:
                return False

    return True


def get_possible_moves_with_check_prevention(piece, pieces):
    possible_moves = piece.get_possible_moves(pieces)
    valid_moves = []

    for move in possible_moves:
        original_position = piece.position
        captured_piece = None
        for p in pieces:
            if p.position == move:
                captured_piece = p
                pieces.remove(p)
                break

        piece.position = move
        if not is_in_check(piece.color, pieces):
            valid_moves.append(move)

        piece.position = original_position
        if captured_piece:
            pieces.append(captured_piece)

    return valid_moves


def show_winner(current):
    root = tk.Tk()
    root.withdraw()
    if current == "white":
        messagebox.showinfo("Koniec gry", f"Mat! Czarne wygrywają!")
    else:
        messagebox.showinfo("Koniec gry", f"Mat! Białe wygrywają!")
    root.destroy()


def change_pawn_to_queen(pawn):
    global pieces
    col, row = pawn.position
    pieces.remove(pawn)
    color = pawn.color
    if (color == "white"):
        new_queen = Queen(pawn.color, (col, row), f'main/images/white_queen.png')
    else:
        new_queen = Queen(pawn.color, (col, row), f'main/images/black_queen.png')
    pieces.append(new_queen)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row, col = get_square(pos)
            if selected_piece is None:
                selected_square = None
                for piece in pieces:
                    if piece.position == (col, row) and piece.color == current_turn:
                        selected_square = (row, col)
                        selected_piece = piece
                        possible_moves = get_possible_moves_with_check_prevention(piece, pieces)
                        break
            else:
                if (col, row) in possible_moves:
                    remove_captured_piece(row, col)
                    selected_piece.position = (col, row)

                    if isinstance(selected_piece, Pawn):
                        if (selected_piece.color == "white" and selected_piece.position[1] == 0) or (
                                selected_piece.color == "black" and selected_piece.position[1] == 7):
                            change_pawn_to_queen(selected_piece)

                    if current_turn == "white":
                        current_turn = "black"
                    else:
                        current_turn = "white"

                    if is_checkmate(current_turn, pieces):
                        draw_board()
                        pygame.display.flip()
                        show_winner(current_turn)

                selected_piece = None
                selected_square = None
                possible_moves = []

    draw_board()
    pygame.display.flip()

pygame.quit()
