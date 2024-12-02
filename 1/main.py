# load the list as two columns, sort the columns individually, then create a 
# new column with the difference between the two columns

import pandas as pd

data = pd.read_csv('list.tsv', sep='\s{3}', engine='python', header=None)
data.columns = ['col1', 'col2']
data['col1'] = data['col1'].sort_values().values
data['col2'] = data['col2'].sort_values().values
data['diff'] = abs(data['col1'] - data['col2'])

#sum of the differences
print(data['diff'].sum())
