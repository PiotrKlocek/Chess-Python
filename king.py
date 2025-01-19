import pygame

class King:
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

        # ruchy poziome i pionowe
        if y > 0:
            new_pos = (x, y - 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if y < 7:
            new_pos = (x, y + 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)
        if x > 0:
            new_pos = (x - 1, y)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if x < 7:
            new_pos = (x + 1, y)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)


        # ruchy na przekątne
        if x > 0 and y > 0:
            new_pos = (x - 1, y - 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if x < 7 and y > 0:
            new_pos = (x + 1, y - 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if x > 0 and y < 7:
            new_pos = (x - 1, y + 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)

        if x < 7 and y < 7:
            new_pos = (x + 1, y + 1)
            piece = is_occupied(new_pos)
            if not piece or piece.color != self.color:
                possible_moves.append(new_pos)


        return possible_moves
