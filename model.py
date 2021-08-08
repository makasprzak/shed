from dataclasses import dataclass


@dataclass
class Element:
    collection: str
    name: str
    x: float
    y: float
    z: float

    def is_5_by_10(self):
        return 0.05 in self.dims() and 0.1 in self.dims()

    def dims(self):
        return [self.x, self.y, self.z]

    def len(self):
        return max(*self.dims())


@dataclass
class LumberOption:
    elements_per_piece: int
    waste_per_piece: float
    waste_on_last_piece: float
    pieces_needed: int
    standard_length: float
    price: float
    count_needed: int
    length_needed: float
