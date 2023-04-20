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
            print(s["id"])
            #TODO mangler et lag sunjects mere...
            #TDO Nej tag eet lag ad gangen

payload_get_subject = {
    "subjects": [
        "2",
        "3429",
        "20318"
    ],
    "pastdays": 1,
    "includeinactive": "true"
}

# def get_subject(subjectID):
def get_subject():
    rr = requests.post('https://api.statbank.dk/v1/subjects', data=payload_get_subject).json()
    # print(rr)

get_subject()


def get_table_name():
    payload_get_table_name = {
        "subjects": [
            "3542"
        ]
    }
    rr = requests.post('https://api.statbank.dk/v1/tables', data=payload_get_table_name).json()
    for table in rr:
        pass
        # print(table)
        # print(table['id'], table['variables'])

get_table_name()

def get_table_metadata():
    payload = {
    "table": "formue11",
    "format": "JSON"
    }
    result = requests.post('https://api.statbank.dk/v1/tableinfo', json=payload).json()
    for meta in result['variables']:
        print(meta['id'])
        for val in meta["values"]:
            print(val)
    


get_table_metadata()

def get_table_data():
    payload = {
        "table": "FORMUE11",
        "format": "CSV",
        "variables": [
            {
                "code": "FORM1",
                "values": ["FGNF2020"]
            },
            {
                "code": "ENHED",
                "values": ["200"]
            },
            {
                "code": "ALDER",
                "values": ["2529"]
            },
            {
                "code": "POPU",
                "values": ["5005"]
            },
            {
                "code": "KØN",
                "values": "MOK"
            }
        ],

    }
    result = requests.post('https://api.statbank.dk/v1/data/', json=payload)
    result = result.text
    print(result)
    # print(result.content)

get_table_data()