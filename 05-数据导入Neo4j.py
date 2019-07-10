import pandas as pd
data_df = pd.read_csv('./data/brand_series.csv')
data_df = data_df[['brand_name','brand_type','type']]
print(data_df.head())
