import sys, platform, random
from src.gameobjs.player import Player
from src.Injan import Injan
from src.InjanStructures import Vector2, Vector3
from src.InjanKeycodes import *


print("Loading Engine...")

engine = Injan()
engine.Initialise()

print("Engine Loaded!")

print("Setting up Camera...")

camera = engine.CreateOrthographicCamera(-1.0, 1.0)
camera.Move(Vector3(-50, -50, 0))
cameraX = 0
cameraY = 0
cameraZ = 0

print("Camera Setup Complete!")

print("Create Background...")
#Set background
print("Background created!")

print("Creating Game Objects...")

player = Player(engine)

print("Game Objects created!")

print("Commence funtime...")

timer = 0

while engine.IsWindowOpen():
   dt = engine.Update()
   timer += dt

   # Player Update
   player.handle_input()
   player.update_position(dt)

    #Final Draw
   engine.Draw()
