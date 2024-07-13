import pygame

imagesW = [pygame.image.load("images/wR1.png"),pygame.image.load("images/wN1.png"),
           pygame.image.load("images/wB1.png"),pygame.image.load("images/wQ1.png"),
           pygame.image.load("images/wK1.png"),pygame.image.load("images/wB2.png"),
           pygame.image.load("images/wN2.png"),pygame.image.load("images/wR2.png")]

imagesB = [pygame.image.load("images/bR1.png"),pygame.image.load("images/bN1.png"),
           pygame.image.load("images/bB1.png"),pygame.image.load("images/bQ1.png"),
           pygame.image.load("images/bK1.png"),pygame.image.load("images/bB2.png"),
           pygame.image.load("images/bN2.png"),pygame.image.load("images/bR2.png")]
pawnB = pygame.image.load("images/bP1.png")
pawnW = pygame.image.load("images/wP1.png")

piece_pos = {
    "wR1": "a1", "wN1": "b1", "wB1": "c1", "wQ1": "d1", "wK1": "e1", "wB2": "f1", "wN2": "g1", "wR2": "h1",
    "bR1": "a8", "bN1": "b8", "bB1": "c8", "bQ1": "d8", "bK1": "e8", "bB2": "f8", "bN2": "g8", "bR2": "h8",
    "wP1": "a2", "wP2": "b2", "wP3": "c2", "wP4": "d2", "wP5": "e2", "wP6": "f2", "wP7": "g2", "wP8": "h2",
    "bP1": "a7", "bP2": "b7", "bP3": "c7", "bP4": "d7", "bP5": "e7", "bP6": "f7", "bP7": "g7", "bP8": "h7"
}