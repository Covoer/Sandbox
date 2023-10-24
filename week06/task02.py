class Monster:
    def __init__(self,name = mike,teeth = 0, colour = blue):
        self.name = name
        self.teeth = teeth
        self.colour = colour
    def is_scary(self):
        if self.teeth > 16 or self.colour.lower() == "red":
            return True
        return False

def run_test():
    