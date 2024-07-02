from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader

from models import Backrooms, Player, Partygoer, Bacteria, RedBackrooms
from ursina.prefabs.health_bar import HealthBar
from ui import Menu

app = Ursina()
Entity.default_shader = lit_with_shadows_shader

class Controller(Entity):
    def __init__(self, **kwargs):
        super().__init__(ignore_paused = True, **kwargs)
        #self.sky = Sky(texture='sky_sunset')
        self.player = Player(self)  
        self.ground = Entity(model='plane', collider='box', scale=(30, 3, 325), texture='grass', texture_scale=(4,4))
        #self.backrooms = Backrooms()
        self.backrooms = RedBackrooms()
        self.music = Audio("assets/sounds/MyVeryOwnDeadShip.ogg",  volume = 0.3)
        self.enemy_list = []
        self.menu = Menu(self)
        self.toggle_menu()
        mouse.locked = False
        mouse.visible = True
        self.start = False

    def toggle_menu(self):
        application.paused = not application.paused
        self.menu.enabled = application.paused
        self.menu.visible = application.paused
        self.player.health_bar.enabled = not application.paused
        mouse.locked = not mouse.locked
        mouse.visible = not mouse.visible
        self.player.cursor.enabled = not application.paused
    
    
    def new_game(self):       
        for enemy in self.enemy_list:
            destroy(enemy)
            
        
        #self.enemy = Bacteria(self.player)
        self.enemy3 = Partygoer(Vec3(-3.50633, 0.12, 39.8768), self.player)
        self.enemy_list.append(self.enemy3)
        self.player.position = self.player.start_pos
        self.player.hp = self.player.max_hp
        self.player.health_bar = Entity(parent=camera.ui, model='quad', color=color.green, scale = (0.5, 0.05), origin=(-0.5, 0), position= (-0.8, -0.45), z=-50)
        self.start = True
        self.spawn_enemy()
        self.toggle_menu()


    def input(self, key):
        if key == "escape" and self.start:
            self.toggle_menu()

    def spawn_enemy(self):
        if not self.start:
            return
        new_enemy = Partygoer(Vec3(3.71027, 0.12, 39.667), self.player)
        self.enemy_list.append(new_enemy)

        next_spawn_time = random.uniform(2,5)
        invoke(self.spawn_enemy, delay=next_spawn_time)


        

window.title = "shoot and run"
window.fullscreen = True
window.exit_button.visible = False
game = Controller()
app.run()