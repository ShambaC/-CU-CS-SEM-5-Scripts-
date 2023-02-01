import os

directory = './'

for filename in os.scandir(directory) :
    if filename.is_file() :
        name = filename.name
        if name.find('.py') == -1 :
            print(filename.path)
            name = name.replace(".png", "")
            n = len(name)
            name = name.zfill(4 - n)
            name = name + ".png"
            os.rename(filename.path, f"./{name}")
