import ctypes, math

class Vector2(ctypes.Structure):
   _fields_ = [("x", ctypes.c_double), 
               ("y", ctypes.c_double)]

   def __str__(self):
      return "(" + str(self.x) + ", " + str(self.y) + ")"

class Vector3(ctypes.Structure):
   _fields_ = [("x", ctypes.c_double), 
               ("y", ctypes.c_double),
               ("z", ctypes.c_double)]

   def __str__(self):
      return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

   def __iadd__(self, rhs):
      return Vector3(self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)

   def __isub__(self, rhs):
      return Vector3(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)

   def __sub__(self, rhs):
      return Vector3(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)

   def magnitude(self):
      mX = math.pow(self.x, 2)
      mY = math.pow(self.y, 2)
      mZ = math.pow(self.z, 2)

      return math.sqrt(mX+mY+mZ)

   def get_normalised(self):
      normaliser = 1/self.magnitude()

      nX = self.x * normaliser
      nY = self.y * normaliser
      nZ = self.z * normaliser

      return Vector3(nX, nY, nZ)

class Array(ctypes.Structure):
   _fields_ = [("data", ctypes.c_void_p), 
               ("length", ctypes.c_int)]


