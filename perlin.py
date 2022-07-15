import PIL, random, sys, argparse, math
from PIL import Image, ImageDraw
import noise
def main():
    random.seed()
    offset = random.randint(1, 100) * random.randint(1, 1000)

    width, height = 500, 500
    octaves = 6
    persistence = .5
    lacunarity = 2.0
    scale = 50.0
    base = 0
    alter = 0
    max_distance = 300

    pil_image = Image.new('RGBA', (width, height),(0, 0, 0))

    for i in range(pil_image.size[0]):
        for j in range(pil_image.size[1]):
            # Generates a value from -1 to 1
            pixel_value = noise.pnoise2((offset+i)/scale,
                                        (offset+j)/scale,
                                        octaves,
                                        persistence,
                                        lacunarity,
                                        width,
                                        height,
                                        base)
                                        
            c = int(pixel_value * 255.0)
            #pixels[i, j] = (255,255,255, c)
            pil_image.putpixel((i,j), (c,c,c))

    pil_image.save("perlin"+str(offset)+ ".png")

if __name__ == "__main__":
    main()

    # 52 minutes - Definitely my maybe
    # -> 1:07

    # watch endsceen -> credits
