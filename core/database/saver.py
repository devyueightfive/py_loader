from threading import Thread


class MarketDataLoader(Thread):
    # Constructor
    def __init__(self, sharedQueue, h5File):
        super().__init__(daemon=True)
        # link to shared queue
        self.queue = sharedQueue
        # link to h5.database
        self.file = h5File

    # Thread does useful work
    def run(self):
        while True:
            # get item from shared queue
            item = self.queue.get()
            # save item to database
            self.saveData(item)
            # inform queue that we complete work with item
            self.queue.task_done()

    # Save data(as item) from market to database (as toFile).
    # Item should contains specific data:
    # item['group'] ~ as path to 'trades' table.
    def saveData(self, item):

        # get a table for data saving
        table = self.file.get_node(item['group'], 'trades')
        # find the last row in the table
        if table.nrows:
            lastRow = table[-1]['tid']
        else:
            lastRow = 0

        # table filling from last row
        tableRow = table.row
        for trade in item['trades']:
            if trade['tid'] > lastRow:
                fields = ['tid', 'type', 'timestamp', 'amount', 'price']
                for f in fields:
                    tableRow[f] = trade.get(f)
                tableRow.append()

        # save data to h5.file (to hdd)
        table.flush()
