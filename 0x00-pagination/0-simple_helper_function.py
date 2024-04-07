#!/usr/bin/env python3
'''page and page size
'''

from typing import Tuple


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
