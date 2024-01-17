class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, new_width):
        self._width = new_width

    def set_height(self, new_height):
        self._height = new_height

    def get_area(self):
        return self._width * self._height

    def get_perimeter(self):
        return 2*self._width + 2*self._height

    def get_diagonal(self):
        return (self._width**2 + self._height**2) ** 0.5

    def get_picture(self):
        return 'Too big for picture.' if self._width > 50 or self._height > 50 else (f'{"*"*self._width}\n' * self._height)

    def get_amount_inside(self, shape):
        amount = 0
        height_inside = self._height // shape._height
        width_inside = self._width // shape._width
        amount = height_inside*width_inside
        return amount
    def __str__(self):
        return f'Rectangle(width={self._width}, height={self._height})'


class Square(Rectangle):

    def __init__(self, size):
        super().__init__(width=size, height=size)

    def set_side(self, new_size):
        super().set_width(new_size)
        super().set_height(new_size)

    def __str__(self):
        return f'Square(side={self._width})'

