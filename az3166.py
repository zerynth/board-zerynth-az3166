from base import *
from devices import *
from jtag import *
import time
import re

class AZ3166(Board):

    @staticmethod
    def match(dev):
        return dev["vid"]=="0483" and dev["pid"]=="374B"

    def reset(self):
        pass
    
    def burn(self,bin,outfn=None):
        fname = fs.get_tempfile(bin)
        if not self.disk:
            return False,"Can't find device disk! Have you mounted the ST Link device?"
        fs.copyfile2(fname,fs.path(self.disk,"az3166.bin"))
        fs.del_tempfile(fname)
        time.sleep(6) # sleep to avoid returning before finishing the copy
        return True,"Ok"

   

    
