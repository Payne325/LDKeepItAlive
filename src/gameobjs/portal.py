from pygame import mixer
from src.gameobjs.player import Player
from src.InjanStructures import Vector2, Vector3

class Portal:
   def __init__(self, engine, pos):
      self.pos = pos
      self.collidedWithPlayer = False
      self.levelEndSFX = "" #none made rn
      self.playedSFX = False

      spriteID = engine.CreateTexture("assets/sprites/portal.png", Vector2(0, 0), Vector2(32, 32))
      self.sprite = engine.CreateSprite(Vector3(self.pos.x + 16, self.pos.y + 16, 1.0), Vector2(32 ,32), spriteID)
      self.sprite.SetDrawable(True)

   def player_has_reached_portal(self, player):
      playerPos = player.get_position()

      diffX = abs(self.pos.x - playerPos.x)
      diffY = abs(self.pos.y - playerPos.y)

      self.collidedWithPlayer = diffX < 30 and diffY < 30
      return self.collidedWithPlayer

   def playSFX(self):
      if self.collidedWithPlayer and not self.playedSFX:
         mixer.music.load(self.levelEndSFX)
         mixer.music.play(0)
         self.playedSFX = True