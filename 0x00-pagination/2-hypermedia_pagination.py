#!/usr/bin/env python3
"""ALX SE Backend Pagination Module."""
import csv
import math
from typing import List, Dict, Tuple, Any


def index_range(page: int, page_size: int) -> Tuple:
    """
       Return a tuple of size two containing a start index and an end index
       corresponding to the range of indexes
       to return in a list for those particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)


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
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the current page."""
        try:
            assert page > 0
            assert page_size > 0
        except Exception:
            raise AssertionError
        self.dataset()
        s, e = index_range(page, page_size)
        return self.__dataset[s:e]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get the current page using HATEOAS."""
        curr_page = self.get_page(page, page_size)
        tot_page = len(self.__dataset)
        page_size = 0 if len(curr_page) == 0 else page_size
        prev_p = None if (page - 1) < 1 else page - 1
        next_p = None if (page + 1) > tot_page or page_size == 0 else page + 1
        hyper: Dict = {
                'page_size': page_size,
                'page': page,
                'data': curr_page,
                'next_page': next_p,
                'prev_page': prev_p,
                'total_pages': tot_page
                }
        return hyper