import os
from collections import Counter
from PIL import Image
from imageai.Detection import ObjectDetection


def rle_encode(image):
    img = Image.open(image)
    hex_pixels = []
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            hexa = rgb2hex(r, g, b)
            hex_pixels.append(hexa)

    encoded_pixels = []
    count = 1
    current_pixel = hex_pixels[0]

    for i in range(1, len(hex_pixels)):
        if hex_pixels[i] == current_pixel:
            count += 1
        else:
            encoded_pixels.append((current_pixel, count))
            current_pixel = hex_pixels[i]
            count = 1

    encoded_pixels.append((current_pixel, count))

    output_filename = image.split('.')[0] + '.txt'
    output_file = open(output_filename, 'w')
    for pixel, count in encoded_pixels:
        output_file.write(f'{pixel} {count}\n')

    print(f'{output_filename} created')


def rgb2hex(r, g, b):
    hex_value = '#{:X}{:X}{:X}'.format(r, g, b)
    return hex_value


def reduce_colors(image):
    img = Image.open(f'{image}')
    width, height = img.size
    new_img = Image.new("RGB", (width, height))

    for x in range(img.width):
        for y in range(img.height):
            color = img.getpixel((x, y))
            closest = closest_color(color)
            new_img.putpixel((x, y), closest)

    new_img.save(f'new_{image}')
    print(f'new_{image} created')


def color_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    distance = ((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2) ** 0.5
    return distance


def closest_color(color):
    basic_colors = [(255, 255, 255), (0, 0, 0),
                    (255, 0, 0), (0, 255, 0),
                    (0, 0, 255), (255, 255, 0),
                    (255, 0, 255), (0, 255, 255)]
    closest = None
    min_distance = float('inf')
    for basic_color in basic_colors:
        distance = color_distance(color, basic_color)
        if distance < min_distance:
            min_distance = distance
            closest = basic_color
    return closest


def object_detection(image):
    try:
        execution_path = os.getcwd()
        detector = ObjectDetection()
        detector.setModelTypeAsTinyYOLOv3()
        detector.setModelPath(os.path.join(execution_path, "tiny-yolov3.pt"))
        detector.loadModel()

        detections, objects_path = detector.detectObjectsFromImage(
            input_image=os.path.join(execution_path, image),
            minimum_percentage_probability=30,
            extract_detected_objects=True
        )

        o_list = []
        for eachObject in detections:
            if eachObject["percentage_probability"] > 90:
                o_list.append(eachObject["name"])

        counts = Counter(o_list)
        sort = sorted(counts.items())
        for name, count in sort:
            print(f"{count} {name}")

    except:
        print("No objects found!")


def main():
    input_str = input().lower().strip()
    try:
        img = Image.open(input_str)
    except:
        print('there went something wrong!')
        exit()
    rle_encode(input_str)
    reduce_colors(input_str)
    object_detection(input_str)


if __name__ == "__main__":
    main()
