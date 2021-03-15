#!/usr/bin/python

##########################################################
# Converts an XML file the JSON file
# Usage:
#  jsonToXml.py -j <json input file> -x [xml output file]
##########################################################

from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import sys
import getopt


def usage():
    print('jsonToXml.py -j <json input file> -x [xml output file]')
    sys.exit(2)


def parseArgument(argv):
    input_file = None
    output_file = None
    try:
        opts, args = getopt.getopt(argv, "hj:x:", ["json=", "xml="])
    except getopt.GetoptError as e:
        print(e)
        usage()

    for opt, arg in opts:
        if opt == '-h':
            print('Converts JSON file to XML file')
            usage()
        elif opt in ("-j", "--json"):
            input_file = arg
        elif opt in ("-x", "--xml"):
            output_file = arg
    if not input_file:
        usage()
    return input_file, output_file


def convert(input_file, output_file):
    with open(input_file, 'r') as json_file:
        json_lines = json_file.read()
        data = readfromstring(json_lines)
        xml_result = json2xml.Json2xml(data).to_xml()
        if output_file:
            with open(output_file, 'w') as out:
                out.writelines(xml_result)
        else:
            print(xml_result)


if __name__ == "__main__":
    json_file, xml_file = parseArgument(sys.argv[1:])
    convert(json_file, xml_file)
