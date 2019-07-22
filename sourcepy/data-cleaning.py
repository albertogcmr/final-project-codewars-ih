# imports 

import pandas as pd
import numpy as np
import requests
import json
from bs4 import BeautifulSoup
from IPython.display import display
import time

INPUT_FILE_PATH = './output/codewar_users.csv' 


df = pd.read_csv(INPUT_FILE_PATH, index_col=0)
print(df.columns)
