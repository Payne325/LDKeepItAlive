import ctypes
from InjanStructures import Vector2, Vector3, Array
from InjanCamera import Camera
from InjanSprite import Sprite
from InjanPathfinder import Pathfinder, Path

class Injan:
   def __init__(self):
      try:
         self.injanDLL = ctypes.cdll.LoadLibrary("../x64/Release/Injan")
         
         self.initialise = self.injanDLL.Initialise
         self.isWindowOpen = self.injanDLL.IsWindowOpen
         self.isKeyDown = self.injanDLL.IsKeyDown
         self.draw = self.injanDLL.Draw
         self.update = self.injanDLL.Update
         self.cleanUp = self.injanDLL.CleanUp
         self.createPerspectiveCamera = self.injanDLL.CreatePerspectiveCamera
         self.createOrthographicCamera = self.injanDLL.CreateOrthographicCamera
         self.setCameraPosition = self.injanDLL.SetCameraPosition
         self.moveCamera = self.injanDLL.MoveCamera
         self.createTexture = self.injanDLL.CreateTexture
         self.createSprite = self.injanDLL.CreateSprite
         self.setSpritePosition = self.injanDLL.SetSpritePosition
         self.moveSprite  = self.injanDLL.MoveSprite
         self.createTileMap = self.injanDLL.CreateTileMap
         self.setTileMapSpriteAll = self.injanDLL.SetTileMapSpriteAll
         self.setTileMapSprite = self.injanDLL.SetTileMapSprite
         self.setTileMapObstacle = self.injanDLL.SetTileMapObstacle
         self.createPathfinder = self.injanDLL.CreatePathfinder
         self.findPath = self.injanDLL.FindPath
         self.getPathPointAt = self.injanDLL.GetPathPointAt

         self.isKeyDown.argtypes = [ctypes.c_int]
         self.createPerspectiveCamera.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
         self.createOrthographicCamera.argtypes = [ctypes.c_double, ctypes.c_double]
         self.setCameraPosition.argtypes = [ctypes.c_int, Vector3]
         self.moveCamera.argtypes = [ctypes.c_int, Vector3]
         self.createTexture.argtypes = [ctypes.c_char_p, Vector2, Vector2]
         self.createSprite.argtypes = [Vector3, Vector2, ctypes.c_int]
         self.setSpritePosition.argtype = [ctypes.c_int, Vector3]
         self.moveSprite.argtype = [ctypes.c_int, Vector3]
         self.createTileMap.argtype = [ctypes.c_int, Vector3, Vector2, Vector2]
         self.setTileMapSprite.argtype = [ctypes.c_int, ctypes.c_int, Vector2]
         self.setTileMapObstacle.argtype = [ctypes.c_int, ctypes.c_bool, Vector2]
         self.createPathfinder.argtype = [ctypes.c_int]
         self.findPath.argtype = [Vector2, Vector2]
         self.getPathPointAt.argtype = [Array, ctypes.c_int]

         self.update.restype = ctypes.c_double
         self.createPerspectiveCamera.restype = ctypes.c_int
         self.createOrthographicCamera.restype = ctypes.c_int
         self.createTexture.restype = ctypes.c_int
         self.createSprite.restype = ctypes.c_int
         self.createTileMap.restype = ctypes.c_int
         self.createPathfinder.restype = ctypes.c_int
         self.findPath.restype = Array
         self.getPathPointAt.restype = Vector2

         self.loaded = True
      except OSError:
          print("Unable to load the system C library")
          self.loaded = False


   # Initialise Function
   def Initialise(self):
      if self.loaded == False: return

      self.initialise()


   # IsWindowOpen Function
   def IsWindowOpen(self):
      if self.loaded == False: return

      return self.isWindowOpen()


   # IsKeyDown Function
   def IsKeyDown(self, key):
      if self.loaded == False : return

      return self.isKeyDown(key)


   # Update Function
   def Update(self):
      if self.loaded == False: return

      dt = self.update()

      return dt


   # Draw Function
   def Draw(self):
      if self.loaded == False: return

      self.draw()


   # CleanUp Function
   def CleanUp(self):
      if self.loaded == False: return

      self.cleanUp()


   # CreatePerspectiveCamera Function
   def CreatePerspectiveCamera(self, fov, near, far):
      if self.loaded == False: return -1

      cameraID = self.createPerspectiveCamera(fov, near, far)

      return Camera(self, cameraID)


   # CreateOrthographicCamera Function
   def CreateOrthographicCamera(self, near, far):
      if self.loaded == False: return -1

      cameraID = self.createOrthographicCamera(near, far)

      return Camera(self, cameraID)


   # SetCameraPosition Function
   def SetCameraPosition(self, camera, position):
      if self.loaded == False: return

      self.setCameraPosition(camera, position)


   # MoveCamera Function
   def MoveCamera(self, camera, vector):
      if self.loaded == False: return

      self.moveCamera(camera, vector)


   # CreateTexture Function
   def CreateTexture(self, image, minBound, maxBound):
      if self.loaded == False: return -1

      return self.createTexture(image.encode('utf-8'), minBound, maxBound)


   # CreateSprite Function
   def CreateSprite(self, position, size, texture):
      if self.loaded == False: return -1

      spriteID = self.createSprite(position, size, texture)

      return Sprite(self, spriteID)


   # CreateTexture Function
   def SetSpritePosition(self, sprite, pos):
      if self.loaded == False: return

      self.setSpritePosition(sprite, pos)


   # CreateSprite Function
   def MoveSprite(self, sprite, vec):
      if self.loaded == False: return

      self.moveSprite(sprite, vec)


   # CreateTileMap Function
   def CreateTileMap(self, start, mapSize, tileSize):
      if self.loaded == False: return

      return self.createTileMap(start, mapSize, tileSize)


   # SetTileMapSprite function
   def SetTileMapSprite(self, tilemap, sprite, loc):
      if self.loaded == False: return

      self.setTileMapSprite(tilemap, sprite, loc)


   # SetTileMapObstacle function
   def SetTileMapObstacle(self, tilemap, isObstacle, loc):
      if self.loaded == False: return

      self.setTileMapObstacle(tilemap, isObstacle, loc)


   # CreatePathfinder Function
   def CreatePathfinder(self, tilemap):
      if self.loaded == False: return

      id = self.createPathfinder(tilemap)

      return Pathfinder(self, id)


   # FindPath Function
   def FindPath(self, pathfinder, start, end):
        if self.loaded == False: return

        id = pathfinder.GetID()

        path = self.findPath(id, start, end)

        return Path(self, path)


   # GetPathPointAt Function
   def GetPathPointAt(self, path, index):
        if self.loaded == False: return

        return self.getPathPointAt(path, index)