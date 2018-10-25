import pandas as pd
data_cds=pd.read_stata('cds_spread5y_2001_2016.dta')
data_cds.describe()
data_assign4=pd.read_stata('dataassign4.dta')
data_assign4.describe()
datatt=pd.merge(data_cds,data_assign4,left_on=['gvkey','mdate'],right_on=['gvkey','datadate'],how='left')
datatt

#this didn't meet the requirement that match the month with the previous quarter, im thinking about duplicate each records of the quarter data and then merge it