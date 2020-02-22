import os
from PIL import Image

for f in os.listdir():
    if f.startswith('Solus'):
        
        nf = f.replace(" ",'-')
        print(f,nf)
        os.rename(f,nf)
        try:
            foo = Image.open(f)
            print(foo.size)
            foo = foo.resize((160,300),Image.ANTIALIAS)
            foo.save(f,quality=95)
        except Exception as e:
            print(e)
