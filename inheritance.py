from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# Abstract class, if we define any abstract method in class
# we can not instantiate object from abstract class
class Stream():
    def __init__(self, region):
        self.opened = False
        self.region = region

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already opened')
        else:
            self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed')
        else:
            self.opened = False

    # abstract method should be implemented by its subclasses
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def __init__(self, region):
        super().__init__(region)

    def read(self):
        print(f'Reading data from file stream in  {self.region} region')


class NetworkStream(Stream):
    def __init__(self):
        super().__init__('EU')
        self.upTime = '2 ms'

    def read(self):
        print(f'Reading data from network stream in {self.region} region with up time {self.upTime}')


fileStream = FileStream('Asia')
fileStream.read()

networkStream = NetworkStream()
networkStream.read()
