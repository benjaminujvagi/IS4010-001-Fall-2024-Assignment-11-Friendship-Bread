#cleanedData.py

import pandas as pd 
import requests

class cleanedData:
    def save_cleaned_data(self): 
        self.data.to_csv('Data/cleanedData.csv', index=False)
