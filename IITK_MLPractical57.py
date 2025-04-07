import pandas as pd
dates = pd.date_range('20190114',periods=6,freq="D")
print(dates[6])