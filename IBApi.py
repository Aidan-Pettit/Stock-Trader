from ibapi.client import EClient
from ibapi.wrapper import EWrapper


class IBApi(EClient, EWrapper):
    def __init__(self, _self):
        EClient.__init__(self, _self)


class Bot:
    ib = None

    def __init__(self):
        ib = IBApi(self)
        ib.connect('127.0.01', 1000, 1)
        ib.run()


bot = Bot()
