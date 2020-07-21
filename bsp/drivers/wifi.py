from wireless import wifi
from broadcom.bcm43362 import bcm43362 as bcm
def init():
    bcm.auto_init()
    return drv

def interface():
    return wifi

