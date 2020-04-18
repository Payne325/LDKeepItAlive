class Camera:
   def __init__(self, injan, id):
      self.injan = injan
      self.id = id

   def SetPosition(self, position):
      self.injan.SetCameraPosition(self.id, position)

   def Move(self, vector):
      self.injan.MoveCamera(self.id, vector)

