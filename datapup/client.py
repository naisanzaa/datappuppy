from datapup.config import PupConfig
from datapup.reader import PupReader


class PupClient(object):
    def __init__(self):
        self.config = PupConfig()

    @staticmethod
    def read_csv(stream: open):
        return PupReader(stream).csv()

    @staticmethod
    def read_stream(stream: open):
        return PupReader(stream).queue()

    @staticmethod
    def df(stream: open):
        return PupReader(stream).df()
