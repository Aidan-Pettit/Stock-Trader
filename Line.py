class Line:
    def __init__(self, slope, length, vertical):
        self.slope = slope
        self.length = length
        self.vertical = slope * length + vertical
