from src.gameobjs.asteroid import Asteroid
from src.InjanStructures import Vector3
from random import seed, uniform
import time

class AsteroidSpawner:
   def __init__(self, engine):
      self.engine = engine

      self.spawnRate = .5
      self.weight = 128
      
      self.weightIncrement = 24
      self.spawnRateIncrement = .01
      self.timer = 0

   def NextLevel(self):
      self.spawnRate -= self.spawnRateIncrement
      self.weight += self.weightIncrement

   def Spawn(self, dt):      
      self.timer += dt

      asteroids = []
      if self.timer >= self.spawnRate:
         self.timer = 0

         seedVal = time.time_ns()
         seed(seedVal)
         xPos = uniform(0.0, 750.0)
         asteroids.append(Asteroid(self.engine, Vector3(xPos, 568.0, 0.0), self.weight))

      return asteroids