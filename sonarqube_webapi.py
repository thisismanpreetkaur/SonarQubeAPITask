import imp
import requests
import json
import sys

base_url = "https://sonarqube.cloudeq.com/api"
token = ""

name = sys.argv[1]

# input box for name
# name = input('Enter quality gate name')

# input box for metric conditon
# metric = input('Enter metric for condition metric')
# error = input('Enter error for condition error threshold')
# op = input('Enter op for condition operator')

## Create Quality Gate
### api/qualitygates/create
def create_quality_gate(name):
    url = base_url + "/" + "qualitygates/create?name="+ name
    req = requests.post(url, auth=(token, ''))
    print(req)
    print(req.json())
    return req.json()
print(create_quality_gate(name))


## Add Metric to Quality Gate
### api/qualitygates/create_condition
def add_metric_to_qualitygate(gateName,metric,error,op):
    url = base_url + "/" + "qualitygates/create_condition?gateName=" + gateName+ "&metric="+ metric + "&error="+ error + "&op="+op
    req = requests.post(url, auth=(token, ''))
    # print(req)
    # print(req.json())
    return req.json()
print(add_metric_to_qualitygate(name,"coverage","80","LT"))


## Create Quality Profile
### api/qualityprofiles/create
# def create_quality_profile(language,name):
#     url = base_url + "/" + "qualityprofiles/create?language="+ language + "&name="+ name
#     req = requests.post(url, auth=(token, ''))
#     # print(req)
#     # print(req.json())
#     return req.json()
# print(create_quality_profile("py","mkprofile"))
