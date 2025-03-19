import random
from code.AlienShot import AlienShot
from code.Satellite import Satellite
from code.Alien import Alien
from code.Background import Background
from code.Const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent):
        if isinstance(ent, Satellite):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, AlienShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interection = False
        if isinstance(ent1, Satellite) and isinstance(ent2, AlienShot):
            valid_interection = True
        elif isinstance(ent1, AlienShot) and isinstance(ent2, Satellite):
            valid_interection = True

        if valid_interection:
            if (ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name
    
    @staticmethod
    def __give_score(enemy: Satellite, entity_list):
        if enemy.last_dmg == 'Alien1Shot':
            for ent in entity_list:
                if ent.name == 'Alien1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Alien2Shot':
            for ent in entity_list:
                if ent.name == 'Alien2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Satellite):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
