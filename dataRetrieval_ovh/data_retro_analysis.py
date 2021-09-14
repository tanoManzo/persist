#%%

# dataframe from patient
import math
import pandas as pd
df_patient_CHUL_brst=pd.read_pickle('df_patient_CHUL_brst.pkl')
df_patient_CHUL_brst.info()

#%%
import sweetviz as sv

my_report = sv.analyze(df_patient_CHUL_brst)
my_report.show_html() # Default arguments will generate to "SWEETVIZ_REPORT.html"