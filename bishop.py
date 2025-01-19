import pygame

class Bishop:
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

        # Ruchy w górę-lewo (lewa przekątna)
        for i in range(1, min(x, y) + 1):
            new_pos = (x - i, y - i)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append((x - i, y - i))

        # Ruchy w górę-prawo (prawa przekątna)
        for i in range(1, min(8 - x, y) + 1):
            new_pos = (x + i, y - i)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append((x + i, y - i))

        # Ruchy w dół-lewo (lewa przekątna)
        for i in range(1, min(x, 8 - y) + 1):
            new_pos = (x - i, y + i)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append((x - i, y + i))

        # Ruchy w dół-prawo (prawa przekątna)
        for i in range(1, min(8 - x, 8 - y) + 1):
            new_pos = (x + i, y + i)
            piece = is_occupied(new_pos)
            if piece:
                if piece.color != self.color:
                    possible_moves.append(new_pos)
                break
            possible_moves.append((x + i, y + i))

        return possible_moves
