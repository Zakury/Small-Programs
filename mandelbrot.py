from PIL import Image

def generate_mandelbrot(pixel_size, max_iterations):
    new_image = Image.new("HSV", (pixel_size, pixel_size))
    raw_image = new_image.load()

    def mandelbrot_iterations(z, c, i):
        if z.real > 2 or not i: return i

        real = (z.real * z.real) - (z.imag * z.imag) + c.real
        imag = 2 * (z.real * z.imag) + c.imag

        return mandelbrot_iterations(complex(real, imag), c, i - 1)

    def real(x):
        return -1.5 + (x * (2 / pixel_size))

    def imag(y):
        return -1.0 + (y * (2 / pixel_size))

    for x in range(pixel_size):
        for y in range(pixel_size):
            pixel_val = mandelbrot_iterations(complex(0, 0), complex(real(x), imag(y)), max_iterations)
            raw_image[x, y] = (int(pixel_val * (255 / max_iterations)), 255, 255)

    return new_image.convert("RGB")

generate_mandelbrot(200, 50).save("mandelbrot.png")