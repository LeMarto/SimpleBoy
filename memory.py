class Memory:
    def __init__(self):
        self.__data = []
        self.Reset()
    
    def Reset(self):
        for address in range(0xFFFF):
            self.__data.append(0xFF)
    
    def Set(self, address, value):
        self.__data[address] = value

    def Get(self, address):
        return self.__data[address]

memory = Memory()