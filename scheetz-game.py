# Jacob Scheetz
# CPS499 - Game Development
# Simple 2D game with python (cocos2d game engine)

import cocos
from cocos import sprite 
from cocos import scene
from cocos.director import Director, director
from cocos.layer import Layer, ColorLayer
from cocos.scenes.transitions import FadeTransition, FadeUpTransition, JumpZoomTransition, SplitColsTransition, ZoomTransition
from cocos.sprite import Sprite
from cocos.actions import *
from cocos.text import Label
from pyglet.window.key import symbol_string


# Welcome Stage
class WelcomeScreen(ColorLayer):
    is_event_handler = True #set event handler True

    def __init__(self):
        super(WelcomeScreen, self).__init__(72, 59, 241, 1000)
        welcomeScreenLabel = Label("Welcome, Press the ENTER key to play!", 
        font_name= "Times New Roman", 
        font_size = 20, 
        anchor_x = 'center', 
        anchor_y = 'center')
        welcomeScreenLabel.position = 320, 240
        self.add(welcomeScreenLabel) 

    def on_key_press(self, key, modifiers):
        if symbol_string(key) == "ENTER":
            director.replace(ZoomTransition(scene.Scene(FirstStage())))
#=== END WELCOME STAGE ===


# First stage
class FirstStage(ColorLayer):
    is_event_handler = True #set event handler True
    def __init__(self):
        super(FirstStage, self).__init__(255, 86, 14, 1000)
        self.sprite = Sprite('mario.png', scale=0.15)
        self.sprite.position = director._window_virtual_width / 2, director._window_virtual_height / 2
        self.sprite.opacity = 0
        self.add(self.sprite)
        self.sprite.do(FadeIn(1))

        goalSprite = Sprite('goal.png', scale=0.15)
        goalSprite.position = (director._window_virtual_width / 2) + 250, (director._window_virtual_height / 2) + 175
        self.add(goalSprite)

    #=== Event Handlers (user input) ===

    def on_key_press(self, key, modifiers):
        # only need to define one move in the x and y directions because we can use Reverse()
        move_left = MoveBy((-20, 0), .25)
        move_up = MoveBy((0, 20), .25)

        #handle moving the sprite
        if symbol_string(key) == "LEFT":
            self.sprite.do(move_left)

        elif symbol_string(key) == "RIGHT":
            self.sprite.do(Reverse(move_left))

        elif symbol_string(key) == "UP":
            self.sprite.do(move_up)

        elif symbol_string(key) == "DOWN":
            self.sprite.do(Reverse(move_up))

        #handle the users has made it to the goal
        elif symbol_string(key) == "SPACE":
            director.replace(FadeUpTransition(scene.Scene(FinalStage())))
# === END FIRST STAGE ===


# Final Stage
class FinalStage(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(FinalStage, self).__init__(155, 89, 182, 1000)
        self.sprite = Sprite('mario.png', scale=0.15)
        self.sprite.position = director._window_virtual_width / 2, director._window_virtual_height / 2
        self.sprite.opacity = 0
        self.add(self.sprite)
        self.sprite.do(FadeIn(2))

        goalSprite = Sprite('goal.png', scale=0.15)
        goalSprite.position = (director._window_virtual_width / 2) - 250, (director._window_virtual_height / 2) + 130
        self.add(goalSprite)


    #=== Event Handlers (user input) ===

    def on_key_press(self, key, modifiers):
        # only need to define one move in the x and y directions because we can use Reverse()
        move_left = MoveBy((-20, 0), .25)
        move_up = MoveBy((0, 20), .25)

        #handle moving the sprite
        if symbol_string(key) == "LEFT":
            self.sprite.do(move_left)

        elif symbol_string(key) == "RIGHT":
            self.sprite.do(Reverse(move_left))

        elif symbol_string(key) == "UP":
            self.sprite.do(move_up)

        elif symbol_string(key) == "DOWN":
            self.sprite.do(Reverse(move_up))

        #handle the users has made it to the goal
        elif symbol_string(key) == "SPACE":
            director.replace(SplitColsTransition(scene.Scene(CongratsScreen())))
# === END FINAL STAGE ===

# Congrats Screen
class CongratsScreen(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(CongratsScreen, self).__init__(51, 153, 255, 1000)

        winLabel = Label("Congratulations you have beaten the game!", 
        font_name= "Times New Roman", 
        font_size = 16, 
        anchor_x = 'center', 
        anchor_y = 'center')
        winLabel.position = 320, 240
        self.add(winLabel)

        instructLabel = Label ("Press ENTER to play again or BACKSPACE to return to the menu...",
        font_name= "Times New Roman", 
        font_size = 14)
        instructLabel.position = winLabel.position[0] - 210, winLabel.position[1] - 100
        self.add(instructLabel)

    def on_key_press(self, key, modifiers):
        if symbol_string(key) == "ENTER":
            director.replace(FadeTransition(scene.Scene(FirstStage())))
        
        elif symbol_string(key) == "BACKSPACE":
            director.replace(JumpZoomTransition(scene.Scene(WelcomeScreen())))
            



# === "Main" ===
director.init()
director.run(scene.Scene(WelcomeScreen()))

