class Geometry:
    
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
            
        except ValueError:
            print("ValueError: Nothing but numbers are accepted as arguments for any value.")
            
    # def __str__(self):
    #     return f"{self.x}, {self.y}"
    
    def __repr__(self):
        return f"Shape: Position at (x={self.x}, y={self.y})"
    
    def translate(self, x, y):
        self.x += float(x)
        self.y += float(y)
    
    def is_inside(self, x, y):
        pass
        