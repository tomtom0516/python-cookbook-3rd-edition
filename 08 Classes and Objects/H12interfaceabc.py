from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


import io

IStream.register(io.IOBase)
f = open('H04__slot__.py')
print(isinstance(f, IStream))
