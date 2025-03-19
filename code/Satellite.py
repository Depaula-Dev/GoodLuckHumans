from code.Entity import Entity
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED


class Satellite(Entity):
    
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Movimento contínuo para a esquerda
    
