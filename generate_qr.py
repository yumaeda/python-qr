import os

try:
    url = 'https://github.com/yumaeda/python-qr'
    srcImg = 'src.jpg'
    output = 'target.gif'
    contrast = 1.5
    brightness = 1.6
    cmd = 'myqr {0} -v 10 -l H -n {1} -p {2} -c'.format(url, output, srcImg)
    optionalParams = '-con {0} -bri {1}'.format(contrast, brightness)

    os.system('{0} {1}'.format(cmd, optionalParams))
except:
    import traceback
    traceback.print_exc()
