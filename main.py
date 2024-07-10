import numpy as np
from PIL import Image
from Ray import Ray
from Sphere import Sphere
from Plane import Plane
from utils import dot, normalize, reflect


# Função de traçado de raios
def trace_ray(ray, objects, light, depth=3):
    color = np.array([0, 0, 0], dtype=np.float64)
    reflection = 1.0

    for _ in range(depth):
        closest_obj = None
        closest_hit = None
        closest_normal = None
        min_dist = float('inf')

        for obj in objects:
            result = obj.intersect(ray)
            if result:
                hit, normal = result
                dist = np.linalg.norm(hit - ray.origin)
                if dist < min_dist:
                    min_dist = dist
                    closest_obj = obj
                    closest_hit = hit
                    closest_normal = normal

        if closest_obj is None:
            break

        to_light = normalize(light - closest_hit)
        light_intensity = max(dot(to_light, closest_normal), 0)
        color += reflection * closest_obj.color * light_intensity
        reflection *= closest_obj.reflection

        ray = Ray(closest_hit + closest_normal * 1e-5, reflect(ray.direction, closest_normal))

    return np.clip(color, 0, 1)

# Função principal de renderização
def render(width, height):
    camera = np.array([0, 0, -1])
    screen = (-1, 1, 1, -1)  # left, top, right, bottom
    light = np.array([5, 5, -10])
    
    objects = [
        Sphere([0, 1, 3], 1, [1, 0, 0]),  # Esfera vermelha
        Sphere([2, 1, 4], 1, [0, 0, 1]), # Esfera azul
        Plane([0, -1, 0], [0, 1, 0], [1, 1, 1])  # Chão branco
    ]

    image = Image.new('RGB', (width, height))
    pixels = image.load()

    for i in range(width):
        for j in range(height):
            x = screen[0] + (screen[2] - screen[0]) * (i + 0.5) / width
            y = screen[1] - (screen[1] - screen[3]) * (j + 0.5) / height
            ray = Ray(camera, [x, y, 0] - camera)
            color = trace_ray(ray, objects, light)
            pixels[i, j] = tuple((color * 255).astype(int))

    image.show()
    image.save('rendered_scene.png')


if __name__ == '__main__':
    render(800, 600)
    