from code.Alien import Alien
from code.AlienShot import AlienShot
from code.Satellite import Satellite
from code.Entity import Entity
from code.Const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
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
        elif isinstance(ent1, Alien):
            valid_interection = False

        if valid_interection: 
            if (ent1.rect.right >= ent2.rect.left and ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >= ent2.rect.top and ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def verify_collision(entity_list):
        """Itera sobre a lista de entidades e verifica colisões"""
        for ent in entity_list:
            EntityMediator.__verify_collision_window(ent)

        for i in range(len(entity_list)):
            for j in range(i + 1, len(entity_list)):
                EntityMediator.__verify_collision_entity(entity_list[i], entity_list[j])

    @staticmethod
    def verify_health(entity_list):
        """Remove entidades cuja saúde chegou a zero"""
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]
