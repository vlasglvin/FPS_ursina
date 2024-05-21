from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

class Controller(Entity):
    def __init__(self, **kwargs):
        super().__init__(ignore_paused = True, **kwargs)
        #self.sky = Sky(texture='sky_sunset')
        self.ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
        self.backrooms = Entity(model="assets\level\scene.gltf", parents=scene, scale=0.1, collider="box", origin_y=0)
        self.player = FirstPersonController()
        self.enemy = Entity(model="assets/bacteria_backrooms/scene", parent=scene, scale=0.7, collider="mesh", origin_y=0, color=color.black)
        self.enemy2 = Entity(model="assets\partygoer_from_backrooms\scene.gltf", parent=scene, scale=2.2, collider="mesh", origin_y=0)
        self.enemy2.x = 5
        self.player.gun = Entity(model='assets/thompson_submachine_gun/scene', 
                                 parent=camera, position =Vec3(0.352125, -0.219659, 0.445983), scale=(.3,.3,.3),
                                origin_z=-.5, rotation=Vec3(0.144472, -81.176, -353.45), on_cooldown=False)
        


        

window.title = "shoot and run"
window.fullscreen = True
window.exit_button.visible = False
game = Controller()
app.run()