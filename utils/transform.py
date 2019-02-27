
import os
import string
def transform():
    path='/Users/dev/Downloads/aaaaaa_files/base/'
    files=os.listdir(path);
    for f in files:
        print(f)
        os.rename(path+f, path+f.lower())

if __name__ == '__main__':
    transform()