def get_layers(pixels, width, height):
    """ Return the 'bitmap' divided into layers of width * height pixel sub-maps. """
    result = []
    layer_size = width * height

    for i in range(0, len(pixels), layer_size):
        result.append(pixels[i:i+layer_size])

    return result


def get_flattened_layer(layers):
    result = [2 for a in layers[0]]

    for i in range(len(layers[0])):
        for layer in layers:
            result[i] = int(layer[i])

            # Flattened result is top-most non-transparent pixel.
            if result[i] != 2:
                break

    return result


def print_img(pixels, width):
    for i in range(0, len(pixels), width):
        print(str(pixels[i:i+width]).replace('0', ' ').replace('1', 'X'))


def part_1():
    width = 25
    height = 6
    pixels = open("resources/08input.txt").read().strip()
    my_layers = get_layers(pixels, width, height)
    counts = (width * height, width * height, width * height)

    for layer in my_layers:
        zero_count = layer.count('0')
        one_count = layer.count('1')
        two_count = layer.count('2')

        if zero_count < counts[0]:
            counts = (zero_count, one_count, two_count)

    return counts[1] * counts[2]


def part_2():
    width = 25
    height = 6
    pixels = open("resources/08input.txt").read().strip()
    return get_flattened_layer(get_layers(pixels, width, height))


def main():
    print("Day 8 part 1 answer: ", part_1())
    img = part_2()
    print("Day 8 part 2 answer: ", part_2())
    print_img(img, 25)


if __name__ == "__main__":
    main()







