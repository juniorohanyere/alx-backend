#!/usr/bin/env python3
'''page and page size
'''

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''takes two integer arguments

    Args:
        page: first integer argument
        page_size: second integer argument

    Return:
        return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters
    '''

    a = 0
    b = 0

    for i in range(page):
        a = b
        b += page_size

    return (a, b)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''initialise
        '''

        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get page
        '''

        assert type(page) is int and type(page_size) is int and page > 0 and \
            page_size > 0
        data = self.dataset()

        try:
            i = index_range(page, page_size)
            return data[i[0]: i[1]]
        except IndexError:
            return []
