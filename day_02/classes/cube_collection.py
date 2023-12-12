class CubeCollection:
    def __init__(self, red=0, green=0, blue=0,):
        self.red = red
        self.blue = blue
        self.green = green
        
    def __str__(self):
        return f"Red: {self.red} Blue: {self.blue} Green: {self.green}"
    
    def is_possible(self, bag):
        return self.red <= bag.red and self.blue <= bag.blue and self.green <= bag.green
    
    def product(self):
        return self.red * self.blue * self.green