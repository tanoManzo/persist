#%%

# dataframe from patient

import pandas as pd
df_patient_CHUL=pd.read_pickle('df_patient.pkl')
df_patient_CHUL.info()


#%%

# credential to access ovh

import requests
from requests.auth import HTTPBasicAuth
import json

auth=HTTPBasicAuth('gaetano-manzo','restPersist21!')

#%%


# get cancer type from resource Condition
FHIRresource="Condition"

for idx_patient in range(len(df_patient_CHUL)-1):
    url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/{FHIRresource}?subject=Patient/{df_patient_CHUL["patientid"][idx_patient]}'
    asw=requests.get(url,auth=auth).json()

    if 'entry' in asw:
        for item in asw['entry']:
            if 'code' in item["resource"].keys():
                code=item["resource"]['code']['coding'][0]['code']
                df_patient_CHUL["cancer_type_code"][idx_patient]=code
                
                if 'C50' in code:
                    df_patient_CHUL["cancer_type"][idx_patient]="breast"
                    break

                if 'C18' in code:
                    df_patient_CHUL["cancer_type"][idx_patient]="colon"
                    break

df_patient_CHUL.info()


# %%

# get cancer stage from Observation
FHIRresource="Observation"

id_test=df_patient_CHUL[df_patient_CHUL['cancer_type']=='breast']\
    ['patientid'][0]

print(id_test)

url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/{FHIRresource}?subject=Patient/{id_test}'

asw=requests.get(url,auth=auth).json()
print()
# %%
if 'entry' in asw:
        for item in asw['entry']:
            if 'component' in item["resource"].keys():
                test_var=item["resource"]['component']

print(json.dumps(test_var, indent=4, sort_keys=True))  
# %%
df_patient_CHUL.to_pickle("df_patient.pkl")