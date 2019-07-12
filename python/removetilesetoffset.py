import png
import sys
import itertools

inputPath = sys.argv[1]
outputPath = sys.argv[2]

offsetX = int(sys.argv[3]) + 1
offsetY = int(sys.argv[4]) + 1

print("input: {0} output: {1}\n offsetX: {2}, offsetY: {3}"
      .format(inputPath, outputPath, offsetX - 1, offsetY - 1))

input = png.Reader(inputPath).read()

# Excessive list conversion because byte arrays
imageRows = list(map(list, list(input[2])))

rowsMinusOffset = []
for row in enumerate(imageRows):
    if (row[0] + 1) % 17 == 0:
        continue
    rowsMinusOffset.append(row[1])


finalImage = []

for row in enumerate(rowsMinusOffset):
    # Get a list of lists containing the 4 color values per pixel
    pixels = [row[1][x:x+4] for x in range(0, len(row[1]), 4)]

    pixelsMinusOffset = []
    for pixel in enumerate(pixels):
        if (pixel[0] + 1) % 17 == 0:
            continue
        pixelsMinusOffset.append(pixel[1])

    finalImage.append(
        list(itertools.chain.from_iterable(pixelsMinusOffset))
    )

outputFile = open(outputPath, 'wb')
writer = png.Writer(int(len(finalImage[0]) / 4), len(finalImage), alpha=True)
writer.write(outputFile, finalImage)
outputFile.close()
