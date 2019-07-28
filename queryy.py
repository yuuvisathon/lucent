import requests
import json
import os

def get_object_yuuvis(machine_id, data_type):
    headerDict = {}
    paramDict = {}

    query = {    
        "query": {
        "statement": "SELECT * FROM enaio:object WHERE machineid = '%s' AND datatype = '%s';"%(machine_id, data_type),
        "skipCount": 0,
        "maxItems": 50
    }}
    baseUrl = 'https' + '://' + 'api.yuuvis.io'

    header_name = 'Content-Type'

    headerDict['Content-Type'] = 'application/json'

    header_name = 'Ocp-Apim-Subscription-Key'

    headerDict['Ocp-Apim-Subscription-Key'] = os.environ["YUUVIS"]

    session = requests.Session()

    #relative path to your new query file
    queryFilePath = './query.json'
    response = session.post(str(baseUrl+'/dms/objects/search'), data=json.dumps(query), headers=headerDict)
    
    return response.json()


def get_data_yuuvis(return_blob):
    objectid= str(return_blob['objects'][0]['properties']['enaio:objectId']['value'])

    headerDict = {}
    paramDict = {}
    baseUrl = 'https' + '://' + 'api.yuuvis.io'

    headerDict['Ocp-Apim-Subscription-Key'] = ''

    session = requests.Session()
    response = session.get(str(baseUrl+'/dms/objects/%s/contents/file'%objectid), headers=headerDict)
    
    return response

