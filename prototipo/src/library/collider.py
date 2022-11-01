import pygame as pg
from abc import ABC

class ColliderShape(ABC):
    origin: pg.Vector3()
    size: pg.Vector3()

    def __init__(self, origin):
        self.__origin = origin if isinstance(origin, pg.Vector3) else pg.Vector3(origin)
        

    @property
    def origin(self) -> pg.Vector3:
        return self.__origin
    
    

class CubeCollider(ColliderShape):
    def __init__(self, origin, size):
        self.__size = pg.Vector3(size)

        super().__init__(origin)

    @property
    def size(self) -> pg.Vector3:
        return self.__size
    
    @property
    def x_min(self):
        return self.origin[0] -  self.__size[0] / 2

    @property
    def x_max(self):
        return self.origin[0] +  self.__size[0] / 2

    @property
    def y_min(self):
        return self.origin[1] -  self.__size[1] / 2

    @property
    def y_max(self):
        return self.origin[1] +  self.__size[1] / 2

    @property
    def z_min(self):
        return self.origin[2] -  self.__size[2] / 2

    @property
    def z_max(self):
        return self.origin[2] +  self.__size[2] / 2
    
    def test(self, cube: "CubeCollider"):
        return (
            self.x_min < cube.x_max and
            self.x_max > cube.x_min and
            self.y_min < cube.y_max and
            self.y_max > cube.y_min and
            self.z_min < cube.z_max and
            self.z_max > cube.z_min
        )



    @property
    def bottom_frontleft(self) -> pg.Vector3:
        ...

    @property
    def bottom_frontright(self) -> pg.Vector3:
        ...

    @property
    def bottom_backleft(self) -> pg.Vector3:
        ...
    
    @property
    def bottom_backright(self) -> pg.Vector3:
        ...
    
    @property
    def top_frontleft(self) -> pg.Vector3:
        ...
    
    @property
    def top_frontright(self) -> pg.Vector3:
        ...
    
    @property
    def top_backleft(self) -> pg.Vector3:
        ...
    
    @property
    def top_backright(self) -> pg.Vector3:
        ...

