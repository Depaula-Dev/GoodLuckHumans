from tkinter.font import Font
import pygame
from pygame import Rect, Surface

from code.const import COLOR_YELLOW, MENU_OPTION, SCORE_POS


class Score:

    def __init__(self, window: pygame.Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass


    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.score_text(48, 'YOU WIN!!', COLOR_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                text = 'Player 1 enter your name(4 characters):'
                
            pygame.display.flip()
            pass



    def show(self):
        pygame.mixer_music.load('./assets/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
