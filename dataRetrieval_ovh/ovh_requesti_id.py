id='UL11-pat-1617785672.422706'

##
import requests
from requests.auth import HTTPBasicAuth


ids=[]
r=[]
auth=HTTPBasicAuth('gaetano-manzo','restPersist21!')

print(requests.get(url='https://prod.ohc.projectpersist.eu/internal-fhir/org1/Patient?_id=UL11-pat-1617785672.422706',auth=auth).json())
print("##################")
print(requests.get(url='https://prod.ohc.projectpersist.eu/internal-fhir/org1/Patient/UL11-pat-1617785672.422706',auth=auth).json())
print("##################")
print(requests.get(url='https://prod.ohc.projectpersist.eu/internal-fhir/org1/Patient/UL11-pat-1617785672.422706/_history',auth=auth).json())
print("##################")
print(requests.post(url='https://prod.ohc.projectpersist.eu/internal-fhir/org1/Patient/_search&count=2',auth=auth).json())
print("##################")
print(requests.post(url='https://prod.ohc.projectpersist.eu/internal-fhir/org1/Condition/_search?&_count=100&page=1',auth=auth).json())
print("##################")