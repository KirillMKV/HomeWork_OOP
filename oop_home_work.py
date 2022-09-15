class Rectangle:
    def __init__(self, side_a, side_b, color='black'):
        self.side_a = int(side_a)
        self.side_b = int(side_b)
        self.color = color

    def info(self):
        print(f' Rectangle with sides: a = {self.side_a}, b = {self.side_b}), color is {self.color}')

    def area(self):
        return f' Rectangle area is: {self.side_b * self.side_a}'

    def change_color(self, new_color):
        self.new_color = new_color
        if new_color == self.color:
            print(f' Rectangle color already is {self.color}')
        else:
            self.color = new_color
            print(f' Rectangle color is changed to {self.new_color}')

    # имеет ли смысл дублировать, если есть метод info ?
    def __repr__(self):
        return f' Rectangle with sides: a = {self.side_a}, b = {self.side_b}), color is {self.color}'


class Triangle(Rectangle):
    def __init__(self, side_a, side_b, side_c, color='black'):
        super().__init__(side_a, side_b, color)
        self.side_c = int(side_c)

    def info(self):
        print(f' Triangle with sides: a = {self.side_a}, b = {self.side_b}), c = {self.side_c}, color is {self.color}')

    def area(self):
        p = (self.side_c + self.side_a + self.side_b)/2
        return f' Triangle area is: {(p*(p-self.side_c)*(p-self.side_a)*(p-self.side_b))**0.5}'

# test:

rect = Rectangle(5, 7)
rect.info()
print(rect)
print(rect.area())
rect.change_color('black')
rect.change_color('red')
rect.info()

triangle = Triangle(3, 5, 7, 'green')
triangle.info()
print(triangle.area())
triangle.change_color('black')
triangle.change_color('red')




