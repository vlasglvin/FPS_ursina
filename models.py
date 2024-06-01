
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Bullet(Entity):
    def __init__(self, player_pos, dir_pos, **kwargs):
        super().__init__(
            model="sphere", color=color.orange, collider="mesh", scale=0.023, position = player_pos + Vec3(1, 1.1, 3),
            **kwargs)
        # self.position += dir_pos
        self.direction = dir_pos
        self.speed = 20

    def update(self):
        self.position += self.direction * self.speed * time.dt

class Gun(Entity):
    def __init__(self, ):
        super().__init__(model='assets/thompson_submachine_gun/scene', 
                                 parent=camera, position =Vec3(0.352125, -0.219659, 0.445983), scale=(.3,.3,.3),
                                origin_z=-.5, rotation=Vec3(0.144472, -81.176, -353.45), on_cooldown=False)
        
        self.shot_sound = Audio("assets/sounds/10 Guage Shotgun-SoundBible.com-74120584.wav", autoplay=False)


    def shot(self):
        if self.on_cooldown:
            self.rotation=Vec3(0.144472, -71.176, -333.45)
        else:
            self.rotation=Vec3(0.144472, -81.176, -353.45)




class Player(FirstPersonController):
    
    def __init__(self, game):
        super().__init__()
        self.gun = Gun()
        self.game = game
    

    
    def input(self, key):
        super().input(key)
        if key == "left mouse down":
            self.shoot()

                 

    def check_collisions(self):
        forward = self.forward * self.speed * time.dt
        hit_check = raycast(self.position, self.forward, distance = self.speed*time.dt, ignore=[self])
        if hit_check.hit:
            print("Collision!!!", hit_check.entity)

    def backrooms_collisions(self):
        if self.intersects(self.game.backrooms).hit:
            print("Backrooms Collision!")


    
    def update(self):
        super().update()
        if held_keys["shift"]:
            self.speed = 10
        else:
            self.speed = 5

        if self.y < -30:
            self.position = self.start_pos

        self.check_collisions()
        self.backrooms_collisions()

    def shoot(self):
        if not self.gun.on_cooldown:
            print('shoot')
            self.gun.on_cooldown = True
            self.gun.shot()
            self.gun.shot_sound.play()
            invoke(setattr, self.gun, 'on_cooldown', False, delay=.1)
            if mouse.hovered_entity and hasattr(mouse.hovered_entity, 'hp'):
                mouse.hovered_entity.hp -= 10
                print(mouse.hovered_entity, mouse.hovered_entity.hp)
                mouse.hovered_entity.blink(color.red)


class Backrooms(Entity):
    def __init__(self, ):
        super().__init__(model="assets/original_backrooms", parent=scene, scale=2, collider="mesh", origin_y=0)

        self.collider = self.model

class RedBackrooms(Entity):
    def __init__(self, ):
        super().__init__(model="assets\level\scene.gltf", parent=scene, scale=0.1, collider="box", origin_y=0)

        self.collider = self.model

class Enemy(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=scene, collider="box", origin_y=0, **kwargs)
        self.health_bar = Entity(parent=self, y=6.5, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp

    def update(self):
        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
        self.health_bar.alpha = 1

class Bacteria(Enemy):
    def __init__(self):
        super().__init__(model="assets/bacteria_backrooms/scene", scale=0.7, color=color.black)
        self.position = (4, 0, 7)
class Partygoer(Enemy):
    def __init__(self):
        super().__init__(model="assets/partygoer_from_backrooms/scene.gltf", scale=2.2, )
        self.position = (-3, 0 ,5)
        self.health_bar.y = 2.5