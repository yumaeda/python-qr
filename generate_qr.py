import os
from MyQR import myqr

url = 'https://github.com/yumaeda/python-qr'
srcImg = 'src.jpg'
output = 'target.gif'
outDir = os.getcwd()

try:
    version, level, qr_name = myqr.run(
	url,
	version = 10,
	level = 'H',
	picture = srcImg,
	colorized = True,
	contrast = 1.0,
	brightness = 1.0,
	save_name = output,
	save_dir = outDir
    )
except:
    import traceback
    traceback.print_exc()

