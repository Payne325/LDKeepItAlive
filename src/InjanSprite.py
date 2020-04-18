class Sprite:
   def __init__(self, injan, id):
      self.injan = injan
      self.id = id

   def SetPosition(self, position):
      self.injan.SetSpritePosition(self.id, position)

   def Move(self, vector):
      self.injan.MoveSprite(self.id, vector)

   def SetDrawable(self, b):
      self.injan.SetSpriteDrawable(self.id, b)

   def GetID(self):
      return self.id

