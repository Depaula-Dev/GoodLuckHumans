import random
from code.Satellite import Satellite
from code.Alien import Alien
from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range (4):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range (5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            
            case 'Alien1':
                return Alien('Alien1', (10, WIN_HEIGHT/2 -30))
            case 'Alien2':
                return Alien('Alien2', (10, WIN_HEIGHT/2 +30))
            case 'Satellite1':
                return Satellite('Satellite1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Satellite2':
                return Satellite('Satellite2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            