from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
Entity.default_shader = lit_with_shadows_shader


class Gun(Entity):
    def __init__(self, ):
        super().__init__(model='assets/thompson_submachine_gun/scene', 
                                 parent=camera, position =Vec3(0.352125, -0.219659, 0.445983), scale=(.3,.3,.3),
                                origin_z=-.5, rotation=Vec3(0.144472, -81.176, -353.45), on_cooldown=False)


class Controller(Entity):
    def __init__(self, **kwargs):
        super().__init__(ignore_paused = True, **kwargs)
        self.sky = Sky(texture='sky_sunset')
        self.ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
        self.player = FirstPersonController()
        self.gun = Gun()
        self.player.gun = self.gun
        
    def update(self):
        # Зміна кута обертання за допомогою клавіш
        rotation_speed = 100 * time.dt
        if held_keys['left arrow']:
            self.player.gun.rotation_y -= rotation_speed
        if held_keys['right arrow']:
            self.player.gun.rotation_y += rotation_speed
        if held_keys['up arrow']:
            self.player.gun.rotation_x -= rotation_speed
        if held_keys['down arrow']:
            self.player.gun.rotation_x += rotation_speed
        if held_keys['q']:
            self.player.gun.rotation_z -= rotation_speed
        if held_keys['e']:
            self.player.gun.rotation_z += rotation_speed


        # Зміна позиції за допомогою клавіш
        position_speed = 1 * time.dt
        if held_keys['f']:
            self.player.gun.x -= position_speed
        if held_keys['h']:
            self.player.gun.x += position_speed
        if held_keys['t']:
            self.player.gun.z += position_speed
        if held_keys['g']:
            self.player.gun.z -= position_speed
        if held_keys['r']:
            self.player.gun.y += position_speed
        if held_keys['y']:  
            self.player.gun.y -= position_speed

        # Друкування поточної ротації і позиції для легшого налаштування
        if held_keys['space']:
            print('Current gun rotation:', self.player.gun.rotation)
            print('Current gun position:', self.player.gun.position)


window.title = "shoot and run"
window.fullscreen = True
window.exit_button.visible = False
game = Controller()
app.run()