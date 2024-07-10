import numpy as np
from utils import dot, normalize


class Plane:
    def __init__(self, point, normal, color, reflection=0.25):
        self.point = np.array(point)
        self.normal = normalize(np.array(normal))
        self.color = np.array(color)
        self.reflection = reflection

    def intersect(self, ray):
        denom = dot(ray.direction, self.normal)
        if abs(denom) > 1e-6:
            t = dot(self.point - ray.origin, self.normal) / denom
            if t >= 0:
                hit = ray.origin + ray.direction * t
                return (hit, self.normal)
        return None
