
class BaseStation:
    def __init__(self, base_name, x, y, r):
        self.id = base_name        
        self.pos = (x, y)
        self.radius = r
