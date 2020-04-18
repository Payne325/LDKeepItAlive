import ctypes

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

class Array(ctypes.Structure):
   _fields_ = [("data", ctypes.c_void_p), 
               ("length", ctypes.c_int)]


