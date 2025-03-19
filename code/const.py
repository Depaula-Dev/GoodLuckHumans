# C
import pygame


COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

EVENT_TIMEOUT = pygame.USEREVENT + 2


ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6, 
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Alien1' :3,
    'Alien1Shot' :2,
    'Alien2' :3, 
    'Alien2Shot' :3,
    'Satellite1': 5,
    'Satellite1Shot': 5,
    'Satellite2': 5,
    'Satellite2Shot': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Alien1': 300,
    'Alien1Shot': 1,
    'Alien2': 300,
    'Alien2Shot': 1,
    'Satellite1': 50,
    'Satellite1Shot': 1,
    'Satellite2': 60,
    'Satellite2Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Alien1': 1,
    'Alien1Shot': 25,
    'Alien2': 1,
    'Alien2Shot': 20,
    'Satellite1': 1,
    'Satellite1Shot': 20,
    'Satellite2': 1,
    'Satellite2Shot': 15,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Alien1': 0,
    'Alien1Shot': 0,
    'Alien2': 0,
    'Alien2Shot': 0,
    'Satellite1': 100,
    'Satellite1Shot': 0,
    'Satellite2': 125,
    'Satellite2Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Alien1': 20,
    'Alien2': 15,
    'Satellite1': 100,
    'Satellite2': 100,
}


# M
MENU_OPTION = ('New Game 1 ALIEN',
               'New Game 2 ALIENS - COOPERATIVE',
               'New Game 2 ALIENS - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Alien1': pygame.K_UP,
                 'Alien2': pygame.K_w}
PLAYER_KEY_DOWN = {'Alien1': pygame.K_DOWN,
                   'Alien2': pygame.K_s}
PLAYER_KEY_LEFT = {'Alien1': pygame.K_LEFT,
                   'Alien2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Alien1': pygame.K_RIGHT,
                    'Alien2': pygame.K_d}
PLAYER_KEY_SHOT = {'Alien1': pygame.K_m,
                    'Alien2': pygame.K_LCTRL}

# S
SPAWN_TIME = 800



# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 15000  # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

