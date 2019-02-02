from queue import Queue

from core.database.initialization import initialization

# Body of Main program
if __name__ == "__main__":
    # make database initialization
    initialization()
    # shared queue for
    # Threads that load data from markets (ninja)
    # and
    # Thread that saves data to database (samurai)
    dataQueue = Queue()
