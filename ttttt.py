import os
import time
import pandas as pd
import yaml

def time_now():
    return time.time()

def generate_test_plan(count):
    start_time = time_now()
    time.sleep(2)
    for i in range(count):
        plan = pd.read_excel('TEST_PLAN_2.xlsx', sheet_name=None)
        plan['config']['VALUE'][0] += '_' + str(i+1)
        writer = pd.ExcelWriter('xlsx/TEST_PLAN_p{}.xlsx'.format(i+1))
        for sheet in plan:
            pd.DataFrame(plan[sheet]).to_excel(writer, index=False, header=True, sheet_name=sheet)
        writer.close()
    end_time = time_now()
    duration = end_time-start_time
    return duration


def generate_node(build_node_w_count,deploy_node_w_count,build_node_tp_count=2):
    data = []
    for i in range(build_node_w_count):
        build_node_w = {'name': 'Build_Node_W_{}'.format(i + 1),
                        'os': 'windows',
                        'function': 'build',
                        'hostname': 'Build_Node_W_{}'.format(i + 1),
                        'ip': '15.83.248.252',
                        'mac': '27832784292',
                        'version': '1.0',
                        'username': 'Automation',
                        'password': 'Shanghai2010',
                        'domain': 'sh'}
        data.append(build_node_w)
    for i in range(build_node_tp_count):
        build_node_tp = {'name': 'Build_Node_TP_{}'.format(i + 1),
                         'os': 'linux',
                         'function': 'build',
                         'hostname': 'Build_Node_TP_{}'.format(i + 1),
                         'ip': '15.83.248.253',
                         'mac': '27832784292',
                         'version': '1.0',
                         'username': 'automation',
                         'password': 'Shanghai2010',
                         'domain': 'sh'}
        data.append(build_node_tp)
    for i in range(deploy_node_w_count):
        deploy_node_w = {'name': 'Deploy_Node_{}'.format(i + 1),
                         'os': 'windows',
                         'function': 'deploy',
                         'hostname': 'Deploy_Node_{}'.format(i + 1),
                         'ip': '15.83.248.251',
                         'mac': '5666666',
                         'version': '1.0',
                         'username': 'Administrator',
                         'password': 'Shanghai2010',
                         'domain': ''}
        data.append(deploy_node_w)
    with open('test_server.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data, f)


if __name__ == '__main__':
    print(generate_test_plan(5))
    # generate_node(5,5)
