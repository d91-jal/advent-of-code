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


def print_img(pixels, width, height):
    for i in range(0, len(pixels), width):
        print(str(pixels[i:i+width]).replace('0', ' ').replace('1', 'X'))


def part1(pixels, width, height):
    my_layers = get_layers(pixels, width, height)
    counts = (width * height, width * height, width * height)

    for layer in my_layers:
        zero_count = layer.count('0')
        one_count = layer.count('1')
        two_count = layer.count('2')

        if zero_count < counts[0]:
            counts = (zero_count, one_count, two_count)

    return counts[1] * counts[2]


def part2(pixels, width, height):
    return get_flattened_layer(get_layers(pixels, width, height))


img_width = 25
img_height = 6
my_input = open("08input.txt").read().strip()
print(part1(my_input, img_width, img_height))
img = part2(my_input, img_width, img_height)
print_img(img, img_width, img_height)





