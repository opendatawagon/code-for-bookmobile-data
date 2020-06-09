import pandas as pd
bkmbdata = pd.read_csv('bookmobiledata.csv')

#View data using head, and look at data types using info.

bkmbdata.head()

bkmbdata.info()

bkmbdata['datetime-byhour'] = bkmbdata['datetime']

bkmbdata.dtypes

bkmbdata

#Copy datetime to new column and convert to data type datetime64.

pd.to_datetime(bkmbdata['datetime'])

bkmbdata['datetime-byhour'] = pd.to_datetime(bkmbdata['datetime'])

bkmbdata

bkmbdata.dtypes

#Now use dt.round to aggregate/round timestamps in new column, and H to aggregate/round to hour.

timebyhour = bkmbdata['datetime-byhour']
pd.Series(timebyhour).dt.round("H")

bkmbdata['datetime-byhour'] = pd.Series(timebyhour).dt.round("H")

bkmbdata

#Delete the old timestamp column.

del bkmbdata['datetime']

bkmbdata

bkmbdata.to_csv('bookmobiledata-NEW.csv')