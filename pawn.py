import pygame

class Pawn:
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

        if self.color == "white":
            # Ruch do przodu o jedno pole
            if y > 0 and not is_occupied((x, y - 1)):
                possible_moves.append((x, y - 1))
                # Ruch do przodu o dwa pola
                if y == 6 and not is_occupied((x, y - 2)):
                    possible_moves.append((x, y - 2))
            # Bicie na ukos
            if x > 0:
                piece = is_occupied((x - 1, y - 1))
                if piece and piece.color != self.color:
                    possible_moves.append((x - 1, y - 1))
            if x < 7:
                piece = is_occupied((x + 1, y - 1))
                if piece and piece.color != self.color:
                    possible_moves.append((x + 1, y - 1))
        elif self.color == "black":
            # Ruch do przodu o jedno pole
            if y < 7 and not is_occupied((x, y + 1)):
                possible_moves.append((x, y + 1))
                # Ruch do przodu o dwa pola
                if y == 1 and not is_occupied((x, y + 2)):
                    possible_moves.append((x, y + 2))
            # bicie na ukos
            if x > 0:
                piece = is_occupied((x - 1, y + 1))
                if piece and piece.color != self.color:
                    possible_moves.append((x - 1, y + 1))
            if x < 7:
                piece = is_occupied((x + 1, y + 1))
                if piece and piece.color != self.color:
                    possible_moves.append((x + 1, y + 1))

        return possible_moves
