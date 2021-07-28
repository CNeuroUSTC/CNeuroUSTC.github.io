import copyfile
'''
#将Bibtex提取为字典
@article{Stagkourakis_2018,
    doi = {10.1038/s41593-018-0153-x},
	url = {https://doi.org/10.1038%2Fs41593-018-0153-x},
	year = 2018,
	month = {may},
	publisher = {Springer Science and Business Media {LLC}},
	volume = {21},
	number = {6},
	pages = {834--842},
	author = {Stefanos Stagkourakis and Giada Spigolon and Paul Williams and Jil Protzmann and Gilberto Fisone and Christian Broberger},
	title = {A neural network for intermale aggression to establish social hierarchy},
	journal = {Nature Neuroscience}
	}
'''

'''
- presenter: Xiaoya Chen & Daguang Li :<a href="https://github.com/CNeuroUSTC/CNeuroUSTC.github.io/blob/master/Weekly_JC_md/616-DaguangXiaoya.md" target="_blank">Summary</a>
  date: 2021/6/16, 19:00pm
  paper: "Chapter 3.3 in Theoretical neuroscience"
  url: "https://mitpress.mit.edu/books/theoretical-neuroscience"
  pdf: "https://www.jianguoyun.com/p/Ddn1UTsQuYjfBxiolvsD"
  authors: "Peter Dayan and L.F.Abbott"
  location: <a href="https://map.baidu.com/search/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6(%E8%A5%BF%E6%A0%A1%E5%8C%BA)-%E7%94%9F%E5%91%BD%E7%A7%91%E5%AD%A6%E5%A4%A7%E6%A5%BC/@13054067.545,3720295.44,19z?querytype=s&da_src=shareurl&wd=%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6(%E8%A5%BF%E6%A0%A1%E5%8C%BA)-%E7%94%9F%E5%91%BD%E7%A7%91%E5%AD%A6%E5%A4%A7%E6%A5%BC&c=127&src=0&wd2=%E5%90%88%E8%82%A5%E5%B8%82%E8%9C%80%E5%B1%B1%E5%8C%BA&pn=0&sug=1&l=13&b=(13043472.77821802,3712418.4285550946;13063946.357629184,3730135.2423363887)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&sug_forward=f2f7c92a9921ecdbb54f5426&device_ratio=2">208</a>

'''
def bib2dic(doitext):
    doitext2 = doitext.split(",\n\t", maxsplit=-1)  # 0,1,2,3
    lendoi = len(doitext2)
    dicdir = []
    diccon = []
    doidic = {}
    for i in range(lendoi):
        if i == 0:
            #continue
            singledic = doitext2[i].split("{", maxsplit = -1)
            doidic['citekey'] = singledic[1]
        else:
            singledic = doitext2[i].split("=", maxsplit = -1)
            # print(singledic[0], singledic[1])
            doidic[singledic[0].rstrip()] = singledic[1]
    return doidic

def delbracket(dicstr):  #删掉左右括号
    dicstr = dicstr.replace('{', '')
    dicstr = dicstr.replace('}', '')
    dicstr.rstrip()
    return dicstr.lstrip()    #去掉开头的空格，不知道什么bug

def addbracket(dicstr):   #增加左右括号
    dicstr = ''.join(['{', dicstr])
    dicstr = ''.join([dicstr, '}'])
    return dicstr

def getdate(datestr):  #date是字符串  2021/07/23, 10:00
    # 返回[2021,07,23]的 str list
    datestr = datestr.split(',', maxsplit = -1)
    datestr = datestr[0].split('/', maxsplit = -1)
    return datestr

def date2str(date, arg, datenum):
    #将 [2021,07,23,09]等 变为类似 '2021/07/23'这样的形式
    dates = ''
    for i in range(datenum):
        if i == 0:
            dates = date[i]
        else:
            dates = dates+arg+date[i]
    return dates

def getmarkdown_name(date, presenter):
    '''
    date : [2021,07,21]的list
    '''
    date = date[0]+date[1]+date[2]
    mkname = date+'-'+presenter
    mkname = mkname.replace(' ', '_')  ##空格和','都替换为'_'
    mkname = mkname.replace(',', '_')
    return mkname

def renamePDF(date, title):
    '''
    date : [2021,07,21]的list
    return 20210721-title
    '''
    date = date[0]+date[1]+date[2]
    return date+'-'+title

def getyamlfile(presenter, date, paper, url, pdf, authors, location, arg):
    '''
    输入的date:2021/07/23, 10:00
    '''
    doidic = {}
    doidic['date'] = date
    date = getdate(date)
    save_name = getmarkdown_name(date, presenter) + '.md'
    if arg == 1:  #Weekly_JC

        doidic['presenter'] = presenter + r' :<a href="https://github.com/CNeuroUSTC/CNeuroUSTC.github.io/blob/master/Weekly_JC_md/'+save_name + r'" target="_blank">Summary</a>'
    elif arg == 2:  #Theory_JC

        doidic['presenter'] = presenter + r' :<a href="https://github.com/CNeuroUSTC/CNeuroUSTC.github.io/blob/master/Theory_JC_md/'+save_name + r'" target="_blank">Summary</a>'
    elif arg == 3:  #WorkReport
        doidic['presenter'] = presenter

    doidic['url'] = url
    doidic['pdf'] = pdf
    doidic['paper'] = paper
    doidic['authors'] = authors
    location_l = r'<a href="https://map.baidu.com/search/%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6(%E8%A5%BF%E6%A0%A1%E5%8C%BA)-%E7%94%9F%E5%91%BD%E7%A7%91%E5%AD%A6%E5%A4%A7%E6%A5%BC/@13054067.545,3720295.44,19z?querytype=s&da_src=shareurl&wd=%E4%B8%AD%E5%9B%BD%E7%A7%91%E5%AD%A6%E6%8A%80%E6%9C%AF%E5%A4%A7%E5%AD%A6(%E8%A5%BF%E6%A0%A1%E5%8C%BA)-%E7%94%9F%E5%91%BD%E7%A7%91%E5%AD%A6%E5%A4%A7%E6%A5%BC&c=127&src=0&wd2=%E5%90%88%E8%82%A5%E5%B8%82%E8%9C%80%E5%B1%B1%E5%8C%BA&pn=0&sug=1&l=13&b=(13043472.77821802,3712418.4285550946;13063946.357629184,3730135.2423363887)&from=webmap&biz_forward=%7B%22scaler%22:2,%22styles%22:%22pl%22%7D&sug_forward=f2f7c92a9921ecdbb54f5426&device_ratio=2">'
    location_r = r'</a>'
    doidic['location'] = location_l + location + location_r
    # 将字典进行排序
    sortdic = {}
    sortdic['presenter'] = doidic['presenter']
    sortdic['date'] = doidic['date']
    sortdic['paper'] = doidic['paper']
    sortdic['url'] = doidic['url']
    sortdic['pdf'] = doidic['pdf']
    sortdic['authors'] = doidic['authors']
    sortdic['location'] = doidic['location']
    return sortdic, getmarkdown_name(date, presenter)

def changeyaml(ymlpath, list):
    oldyml = copyfile.readyml_2(ymlpath)   # <class 'list'>
    oldyml.insert(0, list)
    # oldyml = copyfile.quotes_list_dic(oldyml, 'paper', 'url', 'pdf', 'authors')   #加上双引号
    copyfile.writeyml('G:\Data\WenLab\JC_Update', 'meeting_info', '.yml', oldyml)
    return ymlpath


# def getyamlfile(presenter, date, paper, url, pdf, authors, location):
# newyml = getyamlfile('Daguang Li', '2021/07/23 19:00', 'paper', 'https://www.nature.com/articles/s41593-020-0607-9', 'https://www.nature.com/articles/s41593-020-0607-9', 'www.com', '329A', 1)

# ymlpath = changeyaml('G:\Data\WenLab\JC_Update\meeting_info.yml', newyml)
