import imageio
images = []
filenames = [
    '1.png',
    '1.png',
    '1.png',
    '2.png',
    '2.png',
    '2.png',
    '3.png',
    '3.png',
    '3.png',
    '4.png',
    '4.png',
    '4.png',
    '5.png',
    '5.png',
    '5.png',
    '6.png',
    '6.png',
    '6.png',
    '7.png',
    '7.png',
    '7.png',
    '8.png',
    '8.png',
    '8.png',
]

for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('movie.gif', images)
