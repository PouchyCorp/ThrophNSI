from placeable import Placeable
from coord import Coord
from pygame import Surface, transform

class Inventory:
    def __init__(self) -> None:
        '''list of owned items'''
        self.inv : list[Placeable] = []

        #showed placeables when opened
        self.showed_objects : list[Placeable] = []
        #false if closed, true if opened
        self.is_open = False
        self._page = 0

    def open(self):
        self.showed_objects = self.inv[self._page*8:]

        for ind , obj in enumerate(self.showed_objects):
            #8 element at a time ( or else too big)
          
            biggest_side = max([obj.rect.width, obj.rect.height])
            scale_ratio = 180/biggest_side

            minimized_surf = transform.scale_by(obj.surf, scale_ratio)
            minimized_rect = minimized_surf.get_rect()

            #placement
            if ind % 2 == 0:
                minimized_rect.x = 50
            else:
                minimized_rect.x = 50+180+20

            minimized_rect.y = 50+(200*(ind//2))
            
            minimized_placeable = Placeable(obj.name, Coord(obj.coord.room, minimized_rect.topleft), minimized_surf)
            minimized_placeable.pixelise()

            self.showed_objects[ind] = minimized_placeable

            

    def close(self):
        #to optimize if needed
        self.showed_objects = []

    def toggle(self):
        self.is_open = not self.is_open

        if self.is_open:
            self.open()               
        else:
            self.close()

    def draw(self, win : Surface, mouse_pos : Coord):
        if self.is_open:
            self.mouse_highlight(win, mouse_pos)
            win.blits([(plcb.surf, plcb.rect) for plcb in self.showed_objects])
        else:
            win.blit(Surface((60,60)), (0,60))
    
    def mouse_highlight(self, win : Surface, mouse_pos : Coord):
        for placeable in self.showed_objects:
            if placeable.rect.collidepoint(mouse_pos.xy):
                placeable.draw_outline(win)


    def select_item(self, mouse_pos : Coord) -> str | None:
        """return the name of the item selected
        returns None if no items"""
        for placeable in self.showed_objects:
            if placeable.rect.collidepoint(mouse_pos.xy):
                return placeable.name
        return None
    
    def search_by_name(self, name : str) -> Placeable:
        '''returns the first placeable matching the name'''
        for obj in self.inv:
            if obj.name == name:
                return obj

    def __repr__(self):
        return str(self.__dict__)

# tests
if __name__ == '__main__':
    pass