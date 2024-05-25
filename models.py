
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Gun(Entity):
    def __init__(self, ):
        super().__init__(model='assets/thompson_submachine_gun/scene', 
                                 parent=camera, position =Vec3(0.352125, -0.219659, 0.445983), scale=(.3,.3,.3),
                                origin_z=-.5, rotation=Vec3(0.144472, -81.176, -353.45), on_cooldown=False)

class Player(FirstPersonController):
    
    def __init__(self, game):
        super().__init__()
        self.gun = Gun()
        self.game = game
    
    def input(self, key):
        super().input(key)
                 

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

class Backrooms(Entity):
    def __init__(self, ):
        super().__init__(model="assets\level\scene.gltf", parents=scene, scale=2, collider="mesh", origin_y=0)

        self.collider = self.model

class RedBackrooms(Entity):
    def __init__(self, ):
        super().__init__(model="", parents=scene, scale=2, collider="mesh", origin_y=0)

        self.collider = self.model

class Bacteria(Entity):
    def __init__(self):
        super().__init__(model="assets/bacteria_backrooms/scene", parent=scene, scale=0.7, collider="mesh", origin_y=0, color=color.black)


class Partygoer(Entity):
    def __init__(self):
        super().__init__(model="assets/partygoer_from_backrooms/scene.gltf", parent=scene, scale=2.2, collider="mesh", origin_y=0)