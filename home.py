# -*- coding: utf-8 -*-
# @Time    : 3/19/2019 11:00 AM
# @Author  : Carl
# @Email   : carl.chen@hp.com
# @File    : home.py
# @project : test
from flask import Flask,render_template
from format_data import fdata
import jinja2
information={'Category':' HPDM		#跨多个类别用/分割',
             'Version':' 4.7 SP5	#自动探测',
             'Start Time':' 2017-12-28 14:58:27',
             'Duration':' 00:00:03	#仅保留秒',
             'Note':'为了RC的最后一次的回归测试		#可选填',
            }
ffdata=fdata()['fdata']
passCount=fdata()['passCount']
failCount=fdata()['failCount']
norunCount=fdata()['norunCount']
count=fdata()['count']
# total=[PassingRate,Pass,Fail,NoRun,Count]
total={'Passing rate':100*passCount/count,'Pass':passCount,'Fail':failCount,'NoRun':norunCount,'Count':count}

data = [{'value': total['Pass'], 'name': 'Pass','itemStyle':{'color':'#5cb85c'}},
        {'value': total['Fail'], 'name': 'Fail','itemStyle':{'color':'#d9534f'}},
      {'value': total['NoRun'], 'name': 'No Run', 'itemStyle': {'color': 'grey'}},
       ]

app = Flask(__name__,)
@app.route('/')
def test_report():
    return render_template('base.html',**{'data':data,
                                               'fdata':ffdata,
                                               'total':total,
                                               'information':information,
                                               })
if __name__ == "__main__":
    app.run()