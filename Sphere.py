import numpy as np
from utils import dot, normalize


class Sphere:
    def __init__(self, center, radius, color, reflection=0.5):
        self.center = np.array(center)
        self.radius = radius
        self.color = np.array(color)
        self.reflection = reflection

    def intersect(self, ray):
        L = self.center - ray.origin
        tca = dot(L, ray.direction)
        d2 = dot(L, L) - tca * tca
        if d2 > self.radius * self.radius:
            return None
        thc = np.sqrt(self.radius * self.radius - d2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0 and t1 < 0:
            return None
        t = min(t0, t1)
        if t < 0:
            t = max(t0, t1)
        if t < 0:
            return None
        hit = ray.origin + ray.direction * t
        normal = normalize(hit - self.center)
        return (hit, normal)
