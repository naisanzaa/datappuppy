from automon.helpers.sleeper import Sleeper
from automon.helpers.dates import Dates
from automon.log.logger import Logging, INFO, DEBUG, ERROR

from datapup.client import PupClient
from datapup.stats import PupPanda
from datapup.enrich import PupBlacklistCheck

logging = Logging('stream', level=INFO)
Logging('automon.helpers.sleeper', level=ERROR)


def main():
    c = PupClient()
    stream = c.read_stream(open('traffic.csv'))
    headers = stream.get()

    df = PupPanda.read_csv(headers)
    df['blacklisted'] = None

    alerts = []

    while not stream.empty():
        log = stream.get()

        df = df.append(PupPanda.read_csv(log, names=list(df.columns)))
        df.loc[:, 'blacklisted'].iloc[-1:] = df.loc[:, 'ip'].iloc[-1:].apply(lambda x: PupBlacklistCheck(x))
        logging.debug(f'\n{df}')
        logging.info(f'\n{df.iloc[-1:]}')

        # check every 15 seconds
        if len(df) % 15 == 0:
            logging.info(f'\n\n{df.describe()}\n\n')

        if df.loc[:, 'blacklisted'].iloc[-1]:
            alerts.append(df.iloc[-1:])

        Sleeper.seconds('emulate stream', 1)


if __name__ == "__main__":
    main()
