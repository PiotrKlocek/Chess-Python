import pygame


class Knight:
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

        if 0 <= x + 1 < 8 and 0 <= y - 2 < 8:
            new_pos = (x + 1, y - 2)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if 0 <= x + 2 < 8 and 0 <= y - 1 < 8:
            new_pos = (x + 2, y - 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if 0 <= x + 2 < 8 and 0 <= y + 1 < 8:
            new_pos = (x + 2, y + 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if 0 <= x + 1 < 8 and 0 <= y + 2 < 8:
            new_pos = (x + 1, y + 2)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if 0 <= x - 1 < 8 and 0 <= y + 2 < 8:
            new_pos = (x - 1, y + 2)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if 0 <= x - 2 < 8 and 0 <= y + 1 < 8:
            new_pos = (x - 2, y + 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if 0 <= x - 2 < 8 and 0 <= y - 1 < 8:
            new_pos = (x - 2, y - 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if 0 <= x - 1 < 8 and 0 <= y - 2 < 8:
            new_pos = (x - 1, y - 2)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        return possible_moves
