class Packet:

    def __init__(self, target, args = list()):
        self.target = target
        self.args = args

    def do(self, ctx = dict()):
        raise NotImplementedError()