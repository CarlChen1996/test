# -*- coding: utf-8 -*-
# @Time    : 4/22/2019 1:56 PM
# @Author  : Carl
# @Email   : carl.chen@hp.com
# @File    : format_data.py
# @Project : test
import yaml

def fdata(file='result.yaml'):
    passCount = 0
    failCount = 0
    norunCount = 0
    data_dict={}
    test_list=[]
    fdata=[]
    f=open(file,encoding='utf-8')
    a=yaml.safe_load(f.read())
    # print(a)
    for v in a:
        if v[0] not in test_list:
            test_list.append(v[0])
    # print(test_list)

    for l in test_list:
        fdata.append([l,[],0,0,0,0])
    # print(fdata)

    for v in a:
        for k in fdata:
            if v[0]==k[0]:
                index=fdata.index(k)
                fdata[index][1].append(v)
                if v[-1]=='Pass':
                    fdata[index][2]+=1
                    passCount+=1
                if v[-1]=='Fail':
                    fdata[index][3]+=1
                    failCount+=1
                if v[-1]=='Norun':
                    fdata[index][4]+=1
                    norunCount+=1
                fdata[index][5]+=1
    count = passCount + failCount + norunCount
    data_dict['fdata']=fdata
    data_dict['passCount']=passCount
    data_dict['failCount']=failCount
    data_dict['norunCount']=norunCount
    data_dict['count']=count
    return data_dict

if __name__=='__main__':
    print(fdata())

