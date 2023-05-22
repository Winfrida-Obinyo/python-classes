class Fruit:
     category = "Food"

     def __init__(self, name, color, taste):
         self.name = name
         self.color = color
         self.taste = taste

     def ripe(self):
        return f"Name{self.name}, Color{self.color}, Taste {self.taste}"


