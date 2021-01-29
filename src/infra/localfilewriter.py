class LocalFileWriter(object):
    def __init__(self, path):
        self.path = path
        self.f = None

    def open(self):
        self.f = open(self.path, "w")

    def close(self):
        self.f.close()
    
    def write(self, data):
        self.f.write(data)