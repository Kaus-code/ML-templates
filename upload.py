from google.colab import files
uploaded = files.upload() 

import pandas as pd
df = pd.read_csv('StressLevelDataset.csv')
df.head()
