# pip install requests
import csv
import json
import requests
import codecs
# https://www.dst.dk/da/Statistik/brug-statistikken/muligheder-i-statistikbanken/api#tabellerogemner
# https://www.ft.dk/-/media/sites/statsrevisorerne/dokumenter/2020/beretning-3-2020-om-danmarks-statistiks-kvalitet-og-produktivitet.ashx

# Alternativer:
# https://kristianuruplarsen.github.io/pydst/build/html/index.html
# https://pypi.org/project/denstatbank/

# r = rq.get('https://api.statbank.dk/v1/tables?Borgere')
# print(r)
# print(r.content)
# print(dir(r))
# print(r.headers)
# print(r.text[1:1000])
# print(r.json())
# r_dict = r.json()
# print(r_dict['id'])

#    "delimiter": "Tab",

payload = {
    'table': 'galder',
    'format': 'CSV',
    "delimiter": "Semicolon",
    'valuePresentation': 'Value',
    'variables': [
    {
        'code': 'KOMK',
        'values': ['*']
    }
    ]
}

# payload = {
#    'table': 'galder',
#    'format': 'CSV',
#    'valuePresentation': 'Value',
#    'variables': [
#       {
#          'code': 'KOMK',
#          'values': ['*']
#       },
#       {
#          'code': 'Køn',
#          'values': ['*']
#       }
#    ]
# }

payload2 = {
'table': 'galder',
'format': 'CSV',
'valuePresentation': 'Value'
}

# rr =rq.post('https://api.statbank.dk/v1/data', data=payload)
# print(rr.text)
# print(rr)
# print(rr.headers)

# Brug json i stedet for data!!!!!!
result = requests.post('https://api.statbank.dk/v1/data/', json=payload)

# print(result.text)

# json={"key": "value"}

# KOMK
# 000 084 101 147 155 185 165 151 153 157 159 161 163 167 169 183 173 175 187 201 240 210 250 190 270 260 217 219 223 230 400 411 085 253 259 350 265 269 320 376 316 326 360 370 306 329 330 340 336 390 083 420 430 440 482 410 480 450 461 479 492 530 561 563 607 510 621 540 550 573 575 630 580 082 710 766 615 707 727 730 741 740 746 706 751 657 661 756 665 760 779 671 791 081 810 813 860 849 825 846 773 840 787 820 851 *

# KØN
# TOT M K *

# Tid
# 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 *


# def save_to_csv(data):
#     with open('data.csv', 'w', encoding='UTF-8') as wf:
#         # for line in data:
#         # print(type(data))
#         wf.write(data)

# # fjern carriage return:
# data = result.text.replace('\r','')

payload = {
    "recursive": 'true',
    "format": "JSON"
}

#subjects:
subjects = requests.post('https://api.statbank.dk/v1/subjects/', json=payload).json()
for sub in subjects:
    print(sub['id'])
    for s in sub["subjects"]:
        if len(s['subjects']) > 0:
            pass
            # print(s["id"])
            #TODO mangler et lag sunjects mere...
            #TDO Nej tag eet lag ad gangen



# def get_subject(subjectID):
def get_subject(subjectID):
    payload_get_subject = {
        "subjects": [
            f"{subjectID}"
        ]
    }
    rr = requests.post('https://api.statbank.dk/v1/subjects', data=payload_get_subject).json()
    # print('rr:', rr)
    return rr

# get_subject(2)


def get_table_name(table_id):
    payload_get_table_name = {
        "subjects": [
            f"{table_id}"
        ]
    }
    rr = requests.post('https://api.statbank.dk/v1/tables', data=payload_get_table_name).json()
    for table in rr:
        pass
        # print(table)
        # print(table['id'], table['variables'])
    return table['id']
    

# get_table_name()

# def get_table_metadata(table_name):
#     payload = {
#     "table": f"{table_name}",
#     "format": "JSON"
#     }
#     result = requests.post('https://api.statbank.dk/v1/tableinfo', json=payload).json()
#     vars = []
#     try:
#         for meta in result['variables']:
#             print(meta['id'])
#             vars.append(meta["id"])
#             for val in meta["values"]:
#                 print(val)
#                 pass
        
#     except:
#         pass
#     return vars

def get_table_metadata_field_types(table_name, field_id):
    payload = {
    "table": f"{table_name}",
    "format": "JSON"
    }
    result = requests.post('https://api.statbank.dk/v1/tableinfo', json=payload).json()
    table_field_types = []
    # print(result['variables'][0])
    try:
        for meta in result['variables']:
            # print(meta['id'])
            table_field_types.append(meta['id'])
            # for val in meta["values"]:                
            #     table_field_types.append(val)
    except:
        pass
    # print(len(table_field_types))
    # return table_field_types
    return result['variables'][int(f"{field_id}")]['values']

def get_table_metadata_fields(table_name):
    payload = {
    "table": f"{table_name}",
    "format": "JSON"
    }
    result = requests.post('https://api.statbank.dk/v1/tableinfo', json=payload).json()
    table_fields = []
    try:
        for meta in result['variables']:
            print(meta['id'])
            table_fields.append(meta["id"])
            for val in meta["values"]:
                print(val)
            #     pass
    except:
        pass
    return table_fields
# get_table_metadata()

#TODO: Denne skal bruge args som nr 2 argument, hvori variables bor, json herunder skal skabes dynamisk...
def get_table_data(payload):
    # payload = {
    #     "table": f"{table_name}",
    #     "format": "CSV",
    #     "variables": [
    #         {
    #             "code": "BRANCHE07",
    #             "values": ["CG"]
    #         },
    #         {
    #             "code": "OMSTYPE",
    #             "values": ["SAMLET"]
    #         },
    #         {
    #             "code": "Tid",
    #             "values": ["*"]
    #         }
    #     ],

    # }
    print("running get_table_data")
    result = requests.post('https://api.statbank.dk/v1/data/', json=payload)
    result = result.text
    # print(result)

    print(result)

# get_table_data()