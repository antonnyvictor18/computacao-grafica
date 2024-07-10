import numpy as np
from utils import normalize


class Ray:
    def __init__(self, origin, direction):
        self.origin = np.array(origin)
        self.direction = normalize(np.array(direction))
