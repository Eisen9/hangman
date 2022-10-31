import math
# 1. Create a Cylinder class
class Cylinder:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.surface_area = None
        self.volume = None
    

    def get_surface_area(self):
        '''
        updates the attribute @surace_area and returns the value rounded to 2.d.p.
        '''
        self.surface_area = 2*(math.pi* self.radius * self.height) + 2*(math.pi * self.radius**2) 
        return self.surface_area

    def get_volume(self):
        '''
        updates the attribute volume and retruns the value rounded to 2.d.p.
        '''
        self.volume = math.pi * self.radius**2 * self.height
        return self.volume

    
# create an instance of the cylinder class
cylinder_1 = Cylinder(2, 3)
print(f"{cylinder_1.get_surface_area()} is the surface area of the cylinder")
print(f"{cylinder_1.get_volume()} is the volume of the cylinder")