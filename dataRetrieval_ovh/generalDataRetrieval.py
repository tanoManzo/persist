#%%

# dataframe from patient
import math
import pandas as pd
df_patient_CHUL=pd.read_pickle('df_patient.pkl')
df_patient_CHUL.info()


# credential to access ovh

import requests
from requests.auth import HTTPBasicAuth
import json

auth=HTTPBasicAuth('gaetano-manzo','restPersist21!')

#%%


# (1) get cancer type from resource Condition
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

# (2) get cancer stage from Observation



FHIRresource="Observation"

df_patient_CHUL_brst=df_patient_CHUL[df_patient_CHUL['cancer_type']=='breast'].copy().reset_index(drop=True)

df_patient_CHUL_brst.info()

dict_clin_path={'clinical':'106248000','pathologic':'106249008'}
list_tumor_cat=['T_cat','N_cat','M_cat']

for key in dict_clin_path.keys():
    for cat in list_tumor_cat:
        df_patient_CHUL_brst[f'tumor_stage_{cat}_{key}']=None
        df_patient_CHUL_brst[f'tumor_stage_{cat}_{key}_code']=None

for idx_pat in range(2318):
    id_pat=df_patient_CHUL_brst['patientid'][idx_pat]
    for key in dict_clin_path.keys():
        url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/{FHIRresource}?subject=Patient/{id_pat}&code={dict_clin_path[key]}'
        asw=requests.get(url,auth=auth).json()    
        if 'entry' in asw:
            item=asw['entry'][0]
            for idx_list_cat in range(len(list_tumor_cat)):        
                try:
                    cancer_info=item["resource"]["component"][idx_list_cat]\
                        ["valueCodeableConcept"]["coding"][0]
                    df_patient_CHUL_brst[f'tumor_stage_{list_tumor_cat[idx_list_cat]}_{key}'][idx_pat]=cancer_info["display"]
                    df_patient_CHUL_brst[f'tumor_stage_{list_tumor_cat[idx_list_cat]}_{key}_code'][idx_pat]=cancer_info["code"]
                except:
                    print("None")    
          
                            
                        

df_patient_CHUL_brst.info() 
                
# %%
df_patient_CHUL_brst.to_pickle("df_patient_CHUL_brst.pkl")

# %%
import math

id_pat=df_patient_CHUL_brst['patientid'][1]
url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/{FHIRresource}?subject=Patient/{id_pat}&_count=500&page={1}'
asw=requests.get(url,auth=auth).json()

print(json.dumps(asw,indent=4,sort_keys=True))