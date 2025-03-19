from code.Entity import Entity
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED


class Satellite(Entity):
    
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
    
    def shot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return SatelliteShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


