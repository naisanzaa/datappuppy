from pandas import DataFrame
import pandas

pandas.set_option("display.max_columns", None)
pandas.set_option("display.max_colwidth", 50)
pandas.set_option("large_repr", "truncate")
pandas.set_option('display.expand_frame_repr', False)


class PupPanda(DataFrame):
    def __init__(self):
        self.df = None
        self.headers = None

    def create_df(self):
        self.df = pandas.DataFrame()
        return self.df

    def set_header(self, headers: list):
        self.headers = headers

    def append_df(self, row: open):
        if self.headers:
            self.df.append(self.read_csv(row, names=self.headers))
        else:
            return False

    @staticmethod
    def read_csv(stream: open, **kwargs):
        return pandas.read_csv(stream, **kwargs)
