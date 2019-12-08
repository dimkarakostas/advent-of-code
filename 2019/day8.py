inp = open('input8').read().strip()
width, height = 25, 6
pic_size = width * height

layers = [inp[i:i + pic_size] for i in range(0, len(inp), pic_size)]
zero_digits = [l.count('0') for l in layers]
min_zero = zero_digits.index(min(zero_digits))
print 'Part 1:', layers[min_zero].count('1') * layers[min_zero].count('2')

image = [' ' for _ in range(pic_size)]
for pixel in range(pic_size):
    for idx, l in enumerate(layers):
        if l[pixel] == '1':
            image[pixel] = '1'
        if l[pixel] != '2':
            break

print 'Part 2:'
print '\n'.join([''.join(image[i:i + width]) for i in range(0, pic_size, width)])
