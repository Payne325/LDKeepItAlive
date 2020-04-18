from InjanStructures import Vector2

class Pathfinder:
   def __init__(self, injan, id):
      self.injan = injan
      self.id = id

   def FindPath(self, pointA, pointB):
      return self.injan.FindPath(self, pointA, pointB)

   def GetID(self):
      return self.id


class Path:
   def __init__(self, injan, path):
      self.injan = injan
      self.path = path
      self.pathLength = path.length

   def GetPoint(self, index):
      if index >= self.pathLength:
         print("Index given greater than the path length!")
         return Vector2(0, 0)

      if index < 0:
         print("Index given less than 0!")
         return Vector2(0, 0)

      return self.injan.GetPathPointAt(self.path, index)

   def GetPathLength(self):
      return self.pathLength
