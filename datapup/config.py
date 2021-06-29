import os


class PupConfig(object):
    def __init__(self, stream=None):
        self.stream = stream or os.getenv('PUP_INPUT_STREAM')
