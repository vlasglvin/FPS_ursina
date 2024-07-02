from ursina import *
from ursina import Default, camera

class MenuButton(Button):
    def __init__(self, text, action, x, y, parent, **kwargs):
        super().__init__(text,  on_click = action,parent=parent,
                         color=color.rgb(107, 107, 107),
                         texture="assets/buttons.png",
                         scale = (1, 0.1),
                         text_size = 4,
                         text_scale = 4,
                         text_color=color.white,
                         y = y, x = x, origin=(0,0),
                         ignore_paused = True,
                         **kwargs)
        
        self.text_entity.world_scale = 50


class Menu(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused = True, **kwargs)
        #self.menu_music = Audio("assets/b423b42.wav", loop = True)  
        self.background = Sprite(parent = self, scale = 0.1, texture = "assets\Backrooms_model.jpg", color = color.gray, z = 100)
        Text.default_font = "assets/Jersey25Charted-Regular.ttf"

        Text("Escape the Backrooms", scale=3, parent=self, origin = (0,0), x = 0, y = 0.4)

        self.btns = [
            MenuButton("New Game", game.new_game, x=0,y=0.125   , parent=self),
            #MenuButton("Continue", game.load_game, x=0,y=0.01, parent=self),
            #MenuButton("Save Game", game.save_game, x=0,y=-0.105, parent=self),
            MenuButton("Exit", application.quit, x=0,y=-0.22, parent=self),
        ]