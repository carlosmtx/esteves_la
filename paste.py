import Image
import glob
from os.path import basename


source = Image.open("source.png")
for file in glob.glob('./pasteInto/*'):
    pasteInto = Image.open(file)
    pasteInto.paste(source, (pasteInto.size[0] - source.size[0], pasteInto.size[1]-source.size[1]), source)
    pasteInto.save('./final/'+basename(file)+'.png', "PNG")


