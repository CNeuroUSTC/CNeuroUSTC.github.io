import requests

def  get(DOI):
    "输入DOI获取文章title，author，url链接等信息"
     
    url ='https://doi2bib.org/2/doi2bib?id='+DOI
    strhtml = requests.get(url)
    #错误会返回字符串 Invalid DOI
    return strhtml.text

# print(get('10.1103/PhysRevE.72.061919'))#
# print(type(get('xx')))