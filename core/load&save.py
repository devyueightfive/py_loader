from queue import Queue

import tables

from core.database.initialization import initialization
from core.database.saver import MarketDataLoader

# Body of Main program
if __name__ == "__main__":
    # make database initialization
    pathToH5 = initialization()
    # shared queue for
    # Threads that load data from markets (ninja)
    # and
    # Thread that saves data to database (samurai)
    dataQueue = Queue()
    h5file = tables.open_file(filename=pathToH5, mode='w', title='Crypto Trades')
    samurai = MarketDataLoader(dataQueue, h5file)
