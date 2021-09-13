
#%%

def execute(item):
    try:
        procid=item['id']   
    except:
        procid=None
 
    try:
        performedDateTime=item['performedDateTime']
    except:
        performedDateTime=None
    
    try:
        patientid=item['subject']['reference'].split('/',1)[1]
    except:
        patientid=None

    try:
        procode=item['code']['coding'][0]['code']
    except:
        procode=None

    try:
        protype=item['code']['coding'][0]['display']
    except:
        protype=None

    try:
        procodesystem=item['code']['coding'][0]['system']
    except:
        procodesystem=None
    



    try:
        probodysitecode=item['bodySite'][0]['coding'][0]['code']
    except:
        probodysitecode=None
        
    try:
        probodysitetype=item['bodySite'][0]['coding'][0]['display']
    except:
        probodysitetype=None

    try:
        probodysitesystem=item['bodySite'][0]['coding'][0]['system']
    except:
        probodysitesystem=None



    return {
        "procid": procid,
        "patientid":patientid,
        "performedDateTime":performedDateTime,
        "procode":procode,
    	"protype":protype,
        "procodesystem":procodesystem,
        "probodysitecode":probodysitecode,
        "probodysitetype":probodysitetype,
        "probodysitesystem":probodysitesystem,
        "_type": "Procedure"
    }


# %%
import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

# authentication 
auth=HTTPBasicAuth('gaetano-manzo','restPersist21!')
url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/Procedure/_search'
asw=requests.post(url,auth=auth).json()

# test Patient query 
sample_per_page=asw['total']
current_page=1

# test POST Procedure
url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/Procedure/_search?&_count={sample_per_page}&page={current_page}'
asw=requests.post(url,auth=auth).json()

l_procedure=[]

for entry_idx in range(sample_per_page):
    item=asw["entry"][entry_idx]['resource'] 
    l_procedure.append(execute(item).copy())

import pandas as pd
df_procedure = pd.DataFrame(l_procedure)
df_procedure.head()




# %%
len(df_procedure['patient_id'].unique())