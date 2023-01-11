#!/usr/bin/python3
class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    def area(self) -> float:
        return self.side_length ** 2

    def perimeter(self) -> float:
        return 4 * self.side_length
