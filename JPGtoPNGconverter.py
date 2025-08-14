from PIL import Image, ImageFilter
import os
import sys

# grab first and 2nrd args
fromDir = sys.argv[1] if len(sys.argv) > 1 else './Pokedex'
toDir = sys.argv[2] if len(sys.argv) > 2 else './new'

# check if new/ exists, if not create it
if not os.path.exists(toDir):
    os.makedirs(toDir)

# loop through all files in the current directory and convert them to PNG, then save them in the new directory
for filename in os.listdir(fromDir):
    if filename.endswith('.jpg') or filename.endswith('.jpeg'):
        img = Image.open(os.path.join(fromDir, filename))
        img = img.convert('RGB')  # Convert to RGB if not already
        new_filename = os.path.splitext(filename)[0] + '.png'
        img.save(os.path.join(toDir, new_filename), 'PNG')
