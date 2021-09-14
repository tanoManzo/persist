
#%%
from datetime import datetime

def execute(item):
    try:
        patientid = item["id"]
    except:
        patientid = None
    try:
        identifier = item["identifier"][:]
        idlist = list()
        for each in identifier:
            idlist.append(each["value"])
    except:
        idlist = None
    try:
        active = item["active"]
    except:
        active = None
    try:
        name = item["name"][0]["family"]+item["name"][0]["given"][0]
    except:
        name = None
    try:
        gender = item["gender"]
    except:
        gender = None
    try:
        birthdate = item["birthDate"]
    except:
        birthdate = None

    try:
        deceaseddatetime = item["deceasedDateTime"]
    except:
        deceaseddatetime = None
    try:
        managingOrganization = item["reference"]
    except:
        managingOrganization = None
    try:
        address = item["address"][0]["line"][0]+" "+item["address"][0]["city"]
    except:
        address = None
    try:
        postalcode = item["address"][0]["postalCode"]
    except:
        postalcode = None
    try:
        country = item["address"][0]["country"]
    except:
        country = None
    try:
        state = item["address"][0]["state"]
    except:
        state = None

    return{
        "_type": "patient",
        "patientid": patientid,
        "active": active,
        "gender": gender,
        "birthdate": birthdate,
        "deceaseddatetime": deceaseddatetime,
        "managingOrganization": managingOrganization,
        "country": country,
        "state": state
    }


import requests
from requests.auth import HTTPBasicAuth
import pandas as pd

# authentication 
auth=HTTPBasicAuth('gaetano-manzo','restPersist21!')
resource='Patient'

# POST request
url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/{resource}/_search'
asw=requests.post(url,auth=auth).json()
# sample size

sample_per_page= asw['total']
url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/{resource}/_search?&_count={sample_per_page}&page={1}'
asw=requests.post(url,auth=auth).json()


l_patient=[]
for entry_idx in range(sample_per_page):
    item=asw["entry"][entry_idx]['resource']
    l_patient.append(execute(item).copy())



df_patient = pd.DataFrame(l_patient)
df_patient.head()
df_patient.info()

df_patient.to_pickle("df_patient.pkl")
#%%

df_patient_CHUL=df_patient[df_patient["patientid"].str.contains("CHUL")].copy().reset_index(drop=True)
df_patient_CHUL.head(10)

# %%




id_p="CHUL_8792e190119f9b2e2263bde2888499ce8e3f528a93222dfaae7120b95716d6d3"
url=f'https://prod.ohc.projectpersist.eu/internal-fhir/org1/{resource}/_search?&_count={sample_per_page}&page={50}'
asw=requests.post(url,auth=auth).json()
print(asw)