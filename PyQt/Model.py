import numpy as np

def line_colours():
    colour_table = ["red", "blue", "black"]
    return colour_table

class DataGenerator(object):
    def __init__(self):
        self.x_data = np.linspace(0.0, 10.0, 100)
        self.y_data = []

    def genData(self, freq, phi):
        self.y_data = np.sin(freq * self.x_data + phi)

    def getXData(self):
        return self.x_data

    def getYData(self):
        return self.y_data
