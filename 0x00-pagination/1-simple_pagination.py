#!/usr/bin/env python3
"""ALX SE Backend Pagination Module."""
from typing import Tuple
import csv 
import math
from typing import List

def index_range(page: int, page_size: int) -> Tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes
    to return in a list for those particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size )

class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

        def dataset(self) -> List[List]:
            """
            Cached dataset
            """
            if self.__dataset is None:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                    self.dataset = dataset[1:]

                    return self.__datset
                

                def get_page(self, page: int = 1, page_size: int = 10) -> List[list]:
                    """get the current page."""
                    try:
                        assert page > 0
                        assert page_size > 0
                    except Exception:
                        raise AssertionError
                    self.dataset()
                    s,e = index_range(page, page_size)
                    return self.__dataset[s:e]