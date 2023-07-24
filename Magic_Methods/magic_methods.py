'''
create a rectangle class which implements:

an __init__ method which sets the rectangles height and width
a __str__ method which returns a string which is an ascii-art drawing of the rectangle
an __int__ method which returns the rectangle's area

Feel free to play around with implementing any of the other magic methods if you want to
'''

class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__ (self):
        rectangle_str = ''
        for _ in range(self.height):
            rectangle_str += "*" * self.width + "\n"
        return rectangle_str

    def __int__(self):
        height = self.height
        width = self.width
        return height*width

if __name__ == '__main__':
    Rectangle = rectangle(3,8)
    Rectangle2 = rectangle(5,10)
    print(Rectangle)
    print(int(Rectangle))
    print(Rectangle2)
    print(int(Rectangle2))