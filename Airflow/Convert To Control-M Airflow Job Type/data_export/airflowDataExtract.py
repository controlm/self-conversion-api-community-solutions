#!/usr/bin/python

import sys
import getopt
import requests
import urllib3
import json
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
from requests.auth import HTTPBasicAuth

def usage():
    print('Extract Airflow dags from Airflow REST API and convert them to an XML file')
    print(f'Usage: {sys.argv[0]} -u <airflow username> -p <airflow password> -e <airflow endpoint> -o [output file]')
    print(f'Example: {sys.argv[0]} -u user -p password -e https://airflow.example.com:8080 -o /home/result.xml')
    sys.exit(2)

def parse_arguments(argv, username=None, password=None, endpoint=None, output_file=None):
    try:
        opts, args = getopt.getopt(argv, 'hu:p:e:o:', ['user=', 'password=', 'out=', 'endpoint='])
        for opt, arg in opts:
            if opt == '-h':
                usage()
            elif opt in ('-u', '--user'):
                username = arg
            elif opt in ('-p', '--password'):
                password = arg
            elif opt in ('-o', '--out'):
                output_file = arg
            elif opt in ('-e', '--endpoint'):
                endpoint = arg
        if not username or not password or not endpoint:
            raise getopt.GetoptError('Missing mandatory argument')
        return username, password, endpoint, output_file
    except getopt.GetoptError as e:
        print(e)
        usage()

def convert_to_xml(dags, output_file):
    data = readfromstring(dags)
    xml_result = json2xml.Json2xml(data).to_xml()    
    if output_file:
        with open(output_file, 'w') as out:
            out.writelines(xml_result)
    else:
        print(xml_result)
            
def disable_insecure_ssl_warnings():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_airflow_dags(username, password, endpoint):
    disable_insecure_ssl_warnings()
    url = f'{endpoint}/api/v1/dags'
    verify_ssl = False
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password), verify=verify_ssl)
        response.raise_for_status()
        data = json.loads(response.text)
        return json.dumps(data['dags'])
    except requests.exceptions.HTTPError as err:
        print(err)
        sys.exit(3)


if __name__ == '__main__':
    username, password, endpoint, output_file = parse_arguments(sys.argv[1:])
    dags = extract_airflow_dags(username, password, endpoint)
    convert_to_xml(dags, output_file)
