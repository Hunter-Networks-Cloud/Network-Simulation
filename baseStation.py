
class BaseStation:
    def __init__(self, x, y,base_name):
        self.x = x
        self.y = y
        self.id = base_name
        self.adjacent = {}