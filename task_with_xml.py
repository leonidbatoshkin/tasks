from xml.etree import ElementTree
import os
# os.chdir('C:\\Users\Leonid\Desktop\Phyton\Python Using\Scripts')
# print(os.getcwd())

use_root = ElementTree.fromstring('<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>')

colors = {
    'red': 0,
    'green': 0,
    'blue': 0
}


def get_children(root, level=1):
    colors[root.attrib['color']] += level
    level += 1
    for child in root:
        get_children(child, level)


get_children(use_root)

for color, value in colors.items():
    print(color, value)
print()
for color, value in colors.items():
    print(value, end=' ')
