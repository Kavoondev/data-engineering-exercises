import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = pd.DataFrame(data)
    def get_page(self, page_size: int, page_num: int) -> pd.DataFrame:
        start = page_size * (page_num - 1)
        end = start + page_size
        return self.data.iloc[start:end]
 