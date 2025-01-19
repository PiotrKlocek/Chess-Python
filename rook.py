import pygame

class Rook:
    def __init__(self, color, position, image_path):
        self.color = color
        self.position = position
        self.image = pygame.image.load(image_path)

    def draw(self, screen):
        x, y = self.position
        screen.blit(self.image, (x * 80, y * 80))

    def get_possible_moves(self, pieces):
        possible_moves = []
        x, y = self.position

        def is_occupied(pos):
            for piece in pieces:
                if piece.position == pos:
                    return piece
            return None

        # Ruchy w górę
        for i in range(1, 8 - y):
            new_pos = (x, y + i)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append(new_pos)

        # Ruchy w dół
        for i in range(1, y + 1):
            new_pos = (x, y - i)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append(new_pos)

        # Ruchy w lewo
        for i in range(1, x + 1):
            new_pos = (x - i, y)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append(new_pos)

        # Ruchy w prawo
        for i in range(1, 8 - x):
            new_pos = (x + i, y)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append(new_pos)

        return possible_moves
