from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader

from models import Backrooms, Player, Partygoer, Bacteria, RedBackrooms

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

class Controller(Entity):
    def __init__(self, **kwargs):
        super().__init__(ignore_paused = True, **kwargs)
        #self.sky = Sky(texture='sky_sunset')
        self.ground = Entity(model='plane', collider='box', scale=120, texture='grass', texture_scale=(4,4))
        #self.backrooms = Backrooms()
        self.backrooms = RedBackrooms()
        self.player = Player(self)  
        self.enemy = Bacteria()
        self.enemy2 = Partygoer()
        self.enemy2.x = 5
        


        

window.title = "shoot and run"
window.fullscreen = True
window.exit_button.visible = False
game = Controller()
app.run()