import sys
import qrcode

filename, *rest = sys.argv
if len(rest) >= 2:
    content, image, *_ = rest
    qrcode.make(content).save(image)