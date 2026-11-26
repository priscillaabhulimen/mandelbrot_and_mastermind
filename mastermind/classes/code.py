import random
from ..utils import colours,ntocol_dict,colton_dict

class Code():
    def __init__(self):
        pass

    def generate_code(self, c_length: int = 6 ) -> list:
        return [random.randint(1,len(colours)) for _ in range(c_length)]

    def get_color(self, i: int) -> str:
        return ntocol_dict[i]

    def get_number(self, color: str) -> int:
        return colton_dict[color]