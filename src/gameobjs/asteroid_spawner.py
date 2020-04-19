from src.gameobjs.asteroid import Asteroid
from src.InjanStructures import Vector3

class AsteroidSpawner:
   def __init__(self, engine):
      self.engine = engine

      self.spawnRate = 5
      self.weight = 128
      
      self.weightIncrement = 5
      self.spawnRateIncrement = 50
      self.timer = 0

   def NextLevel(self):
      self.spawnRate += self.spawnRateIncrement
      self.weight += self.weightIncrement

   def Spawn(self, dt):      
      self.timer += dt

      asteroids = []
      if self.timer >= self.spawnRate:
         self.timer = 0
         asteroids.append(Asteroid(self.engine, Vector3(320.0, 500.0, 0.0), self.weight))

      return asteroids