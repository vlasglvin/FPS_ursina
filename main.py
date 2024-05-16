from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

class Controller(Entity):
    def __init__(self, **kwargs):
        super().__init__(ignore_paused = True, **kwargs)
        self.sky = Sky(texture='sky_sunset')
        self.ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
        self.player = FirstPersonController()
        self.player.gun = Entity(model='assets/thompson_submachine_gun/scene', 
                                 parent=camera, position=(.5,-.25,.25), scale=(.3,.2,1),
                                origin_z=-.5, rotation=(0,0,0), on_cooldown=False)




window.title = "shoot and run"
window.fullscreen = True
window.exit_button.visible = False
game = Controller()
app.run()