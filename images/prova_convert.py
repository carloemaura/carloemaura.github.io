from sys import argv
from glob import glob
import os

jpegs = glob('*.jpg')

for jpg in jpegs:
    os.system('convert '+jpg+' -strip -sampling-factor 4:2:0 -resize 30% -quality 8 -quantize RGB New_'+jpg+'.png')
