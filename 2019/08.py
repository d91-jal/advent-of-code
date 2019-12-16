width = 25
height = 6
my_input = open("08input.txt").read().strip()


def get_layers(pixels, width, height):
    """ Return the 'bitmap' divided into layers of width * height sub-maps. """
    result = []

    for j in range(0, len(pixels), width * height):
        layer = []

        for i in range(j, j + (width * height), width):
            layer.append(pixels[i:i + width])

        result.append(layer)

    return result


print(get_layers(my_input, width, height))



