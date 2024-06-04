from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader

from models import Backrooms, Player, Partygoer, Bacteria, RedBackrooms
from ursina.prefabs.health_bar import HealthBar

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

class Controller(Entity):
    def __init__(self, **kwargs):
        super().__init__(ignore_paused = True, **kwargs)
        #self.sky = Sky(texture='sky_sunset')
        self.ground = Entity(model='plane', collider='box', scale=120, texture='grass', texture_scale=(4,4))
        #self.backrooms = Backrooms()
        self.backrooms = RedBackrooms()
        self.music = Audio("assets/sounds/MyVeryOwnDeadShip.ogg",  volume = 0.3)
        self.player = Player(self)  
        #self.enemy = Bacteria(self.player)
        self.enemy2 = Partygoer(Vec3(3.69454, 0 , 35.7391), self.player)
        self.enemy3 = Partygoer(Vec3(8.32528, 0.12, 32.6679), self.player)



    def input(self, key):
        if key == "g":
            print(self.player.position)


        

window.title = "shoot and run"
window.fullscreen = True
window.exit_button.visible = False
game = Controller()
app.run()