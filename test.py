import pandas as pd
from variables import loc_code

df = pd.read_csv('data/property_details.csv', index_col=None)

df['LocationCode'] = pd.Series(loc_code)
df['LocationCode'] = df['LocationCode'][0]

locations = pd.read_csv('data/location_lookup.csv', index_col=None)

df = pd.merge(df, locations, on=['LocationCode', 'LocationCode'], how='left')