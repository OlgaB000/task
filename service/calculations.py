from functools import reduce
import logging
logging.basicConfig(level=logging.INFO)


class BasicStatistic:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_total(self):
        if not self.numbers:
            logging.info('There are no numbers to summarise')
            return 0
        return reduce(lambda a, b: a + b, self.numbers, 0)
