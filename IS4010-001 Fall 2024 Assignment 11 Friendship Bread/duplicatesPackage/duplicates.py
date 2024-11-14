#duplicates.py


import pandas as pd 
import requests

class Duplicates:
    def remove_duplicates(duplicates):
        duplicates.data = duplicates.data.drop_duplicates()

    
