from __future__ import annotations

import pandas as pd

df = pd.read_excel('raw/osm_data.xlsx', sheet_name=None)
for key in df.keys():
    df[key].to_csv(f'processed/{key}.csv')
