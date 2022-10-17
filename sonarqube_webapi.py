import requests
import json

base_url = "https://sonarqube.cloudeq.com/api"
token = "ddb0fa86be8470f76f83c4436f457e4601e71700"

## Create Quality Gate
### api/qualitygates/create
def create_quality_gate(name):
    url = base_url + "/" + "qualitygates/create?name="+ name
    req = requests.post(url, auth=(token, ''))
    print(req)
    print(req.json())
    return req.json()
print(create_quality_gate("mkqualitygate"))


## Add Metric to Quality Gate
### api/qualitygates/create_condition
def add_metric_to_qualitygate(gateName,metric,error,op):
    url = base_url + "/" + "qualitygates/create_condition?gateName=" + gateName+ "&metric="+ metric + "&error="+ error + "&op="+op
    req = requests.post(url, auth=(token, ''))
    # print(req)
    # print(req.json())
    return req.json()
print(add_metric_to_qualitygate("mk-qualitygate","coverage","80","LT"))


## Create Quality Profile
### api/qualityprofiles/create
def create_quality_profile(language,name):
    url = base_url + "/" + "qualityprofiles/create?language="+ language + "&name="+ name
    req = requests.post(url, auth=(token, ''))
    # print(req)
    # print(req.json())
    return req.json()
print(create_quality_profile("py","mkprofile"))