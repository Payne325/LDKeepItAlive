import sys, platform, random
from src.Injan import Injan
from src.InjanStructures import Vector2, Vector3
from src.InjanKeycodes import *


print("Initialising.")

injan = Injan()
injan.Initialise()
# cameraID = injan.CreatePerspectiveCamera(45, 0.1, 1000.0)
camera = injan.CreateOrthographicCamera(-1.0, 1.0)
camera.Move(Vector3(-50, -50, 0))
cameraX = 0
cameraY = 0
cameraZ = 0
box = injan.CreateTexture("../Images/container.jpg", Vector2(0, 0), Vector2(512, 512))
grass = injan.CreateTexture("../Images/grass.jpg", Vector2(0, 0), Vector2(512, 512))
player = injan.CreateTexture("../Images/player.png", Vector2(0, 0), Vector2(512, 512))
playerSprite = injan.CreateSprite(Vector3(0, 0, 1.0), Vector2(32 ,32), player)

sprites = []

for i in range(0, 100):
   sprites.append(injan.CreateSprite(Vector3(0, 0, 0), Vector2(32, 32), grass))

tilemap = injan.CreateTileMap(Vector3(0, 0, 0.5), Vector2(10, 10), Vector2(32, 32))

count = 0
for i in range(0, 10):
   for j in range(0, 10):
      injan.SetTileMapSprite(tilemap, sprites[count].GetID(), Vector2(i, j))
      count += 1

obstacleList = [Vector2(1, 0), Vector2(1, 1), Vector2(2, 1), Vector2(3, 1)]
boxSprites = []

for i in range(0, 4):
   boxSprites.append(injan.CreateSprite(Vector3(0, 0, 1.0), Vector2(32, 32), box))


for i in range(0, len(obstacleList)):
   injan.SetTileMapSprite(tilemap, boxSprites[i].GetID(), obstacleList[i])
   injan.SetTileMapObstacle(tilemap, True, obstacleList[i])


pathfinder = injan.CreatePathfinder(tilemap)
path = pathfinder.FindPath(Vector2(0, 0), Vector2(2, 0))
pathlength = path.GetPathLength()

print("Path length = " + str(pathlength))

currPos = 0
timer = -3

for i in range(0, pathlength):
   vec = path.GetPoint(i)
   print(vec)

while injan.IsWindowOpen():
   dt = injan.Update()
   injan.Draw()

   timer += dt

   # CAMERA CONTROLS

   speed = Vector3(0, 0, 0)
   speedModifier = 100 * dt
   
   if injan.IsKeyDown(INJAN_KEY_LEFT_SHIFT):
      speedModifier *= 2

   if injan.IsKeyDown(INJAN_KEY_W):
      speed.y += 1 * speedModifier

   if injan.IsKeyDown(INJAN_KEY_A):
      speed.x -= 1 * speedModifier

   if injan.IsKeyDown(INJAN_KEY_S):
      speed.y -= 1 * speedModifier

   if injan.IsKeyDown(INJAN_KEY_D):
      speed.x += 1 * speedModifier

   camera.Move(speed)


   # SPRITE CONTROLS

   speed = Vector3(0, 0, 0)

   if injan.IsKeyDown(INJAN_KEY_UP):
      speed.y += 1 * speedModifier

   if injan.IsKeyDown(INJAN_KEY_LEFT):
      speed.x -= 1 * speedModifier

   if injan.IsKeyDown(INJAN_KEY_DOWN):
      speed.y -= 1 * speedModifier

   if injan.IsKeyDown(INJAN_KEY_RIGHT):
      speed.x += 1 * speedModifier

   if timer > 1 and currPos != pathlength - 1:
      timer = 0
      currPos += 1

      pos = path.GetPoint(currPos)
      playerSprite.SetPosition(Vector3(pos.x * 32, pos.y * 32, 1.0))

injan.CleanUp()
print("Exiting.")
