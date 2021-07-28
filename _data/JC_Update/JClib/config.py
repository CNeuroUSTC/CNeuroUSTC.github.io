# -*- coding: utf-8 -*-
def get(arg):
    config = {}
    config['nutstore_Weekly'] = r'H:\SoftWareData\NutStore\我的坚果云\Weekly JC Paper'
    config['nutstore_Theory'] = r'H:\SoftWareData\NutStore\我的坚果云\Theory JC Paper'
    config['markdown_Weekly']= r'G:\Data\WenLab\CNeuroUSTC.github.io\Weekly_JC_md'    #
    config['markdown_Theory'] = r'G:\Data\WenLab\CNeuroUSTC.github.io\Theory_JC_md'
    config['Weekly_place'] = r'329A'
    config['Theory_place'] = r'205'
    config['Weekly_Time']  = r'10:00'
    config['Report_Time']  = r'11:00'
    config['Theory_Time'] = r'19:00'

    config['ymlpath'] = r'G:\Data\WenLab\CNeuroUSTC.github.io\_data\meeting_info.yml'
    config['meeting_info_path'] = r'G:\Data\WenLab\JC_Update'
    config['metting_info_name'] = r'meeting_info'

    return config[arg]

def time2num(time):
    time = time.split(":", maxsplit=-1)  # 0,1,2,3
    if len(time) > 2:
        s = int(time[2])
    else:
        s = 0
    h = int(time[0])
    m = int(time[1])
    return h, m, s




# print(time2num("10:00"))



