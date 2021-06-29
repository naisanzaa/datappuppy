import asyncio

import pandas as pd
from queue import Queue
from io import StringIO


class PupReader(object):
    def __init__(self, stream: open):
        self.stream = stream

    def csv(self):
        return PupCsv(self.stream).df()

    def df(self):
        return self.csv

    def queue(self):
        q = Queue()
        for log in self.stream.read().splitlines():
            q.put_nowait(StringIO(log))
        return q


class PupCsv:
    def __init__(self, csv: open):
        self.csv = pd.read_csv(csv)
        self.DF = self.csv

    def __repr__(self):
        return f'{self.DF}'

    def df(self):
        return self.DF


class PupLog:
    def __init__(self, log: str):
        self.log = log

    def __repr__(self):
        return f'{self.__dict__}'
