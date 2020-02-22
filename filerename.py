import os
from PIL import Image

for f in os.listdir():
    if f.startswith('Solus'):
        
        nf = f.replace(" ",'-')
        print(f,nf)
        os.rename(f,nf)
        try:
            foo = Image.open(f)
            width,height = foo.size
            nwidth = int(width*0.75)
            nheight = int(height*0.75)
            foo = foo.resize((nwidth,nheight),Image.ANTIALIAS)
            foo.save(f,quality=95)
        except Exception as e:
            print(e)
