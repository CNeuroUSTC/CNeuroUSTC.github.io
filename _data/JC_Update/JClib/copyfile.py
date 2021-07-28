import shutil
import os
from ruamel import yaml


def copy_rename(srcpath, srcname, dstpath, dstname, dsttype):
    '''
        复制文件并重命名
        srcpath : 源目录
        srcname : 源文件
        dstpath : 目录目录
        dstname : 目标文件名
        dstype : 目标文件扩展名
        目标文件存在则会加上 "_1"复制后重命名
    '''
    if not isinstance(srcpath, str):
        return "源目录不存在"
    if not isinstance(srcname, str):
        return "源文件不存在"
    if not isinstance(dstpath, str):
        return "目标目录不存在"
    if not isinstance(dstname, str):
        return "目标文件不存在"
    if isinstance(dsttype, int):  # 格式是数字名转换为字符串
        dsttype = str(dsttype)
    if not isinstance(dsttype, str):
        return "目标文件格式不正确"

    src = os.path.join(srcpath, srcname)
    if os.path.isdir(srcpath) == 1:  # 源目录存在
        if os.path.isfile(src) == 1:  # 源文件存在
            if os.path.isdir(dstpath):  # 目标目录存在
                dst = os.path.join(dstpath, dstname + dsttype)
                if os.path.isfile(dst):  # 目标文件存在
                    dstname = dstname + '_1'
                    return copy_rename(srcpath, srcname, dstpath, dstname, dsttype)
                else:
                    shutil.copy(src, dst)
                    return os.path.realpath(dst)
            else:
                return "目标目录不存在"
        else:
            return "源文件不存在"

    else:
        return "源目录不存在"


def copy_rename_2(srcpath, dstpath, dstname, dsttype):
    '''
        复制文件并重命名
        srcpath : 源目录文件
        dstpath : 目录目录
        dstname : 目标文件名
        dstype : 目标文件扩展名
        目标文件存在则会加上 "_1"复制后重命名
    '''
    if not isinstance(srcpath, str):
        return "源文件不存在"
    if not isinstance(dstpath, str):
        return "目标目录不存在"
    if not isinstance(dstname, str):
        return "目标文件不存在"
    if isinstance(dsttype, int):  # 格式是数字名转换为字符串
        dsttype = str(dsttype)
    if not isinstance(dsttype, str):
        return "目标文件格式不正确"

    if os.path.isfile(srcpath) == 1:  # 源文件存在
        if os.path.isdir(dstpath):  # 目标目录存在
            dst = os.path.join(dstpath, dstname + dsttype)
            if os.path.isfile(dst):  # 目标文件存在
                dstname = dstname + '_1'
                return copy_rename_2(srcpath, dstpath, dstname, dsttype)
            else:
                shutil.copy(srcpath, dst)
                return os.path.realpath(dst)
        else:
            return "PDF not found"
    else:
        return "PDF not found"


def mkdir(pdir, subdir):  # 创建目录
    if os.path.isdir(pdir):  # 父目录存在
        path = os.path.join(pdir, subdir)
        if os.path.isdir(path):  # 此目录已经存在
            return "目录已存在"
        else:
            os.makedirs(path)
            return path
    else:
        return "父目录不存在"


def mkfile(dstpath, dstname, dsttype):  # 创建空文件夹
    if os.path.isdir(dstpath):  # 目标目录存在
        dst = os.path.join(dstpath, dstname + dsttype)
        if os.path.isfile(dst):  # 目标文件存在
            dstname = dstname + '_1'
            return mkfile(dstpath, dstname, dsttype)
        else:
            file = open(dst, 'w')
            file.close()
            return os.path.realpath(dst)
    else:
        return "目标目录不存在"


# 将字典写入yaml文件
def writeyml(filepath, filename, fileType, list):
    if os.path.isdir(filepath):  # 目标目录存在
        dst = os.path.join(filepath, filename + fileType)
        if os.path.isfile(dst):  # 目标文件存在 就写在最前面
            with open(dst, "w+", encoding="utf-8") as f:
                # yaml.safe_dump(list, f, default_style='"', explicit_start=False, default_flow_style=False)
                # yaml.dump(list, f, default_style='"', Dumper=yaml.RoundTripDumper)
                list = quotes_list_dic(list, 'paper', 'url', 'pdf', 'authors')  # 要加双引号
                for i in range(len(list)):
                    f.write('- ')
                    # 'paper', 'url', 'pdf', 'authors' 要加双引号
                    kstr = add_blank(list[i], 2)
                    for j in range(len(list[i])):
                        if j == 0:
                            f.write(kstr[j].lstrip())  # 去掉开头的两个空格
                            f.write('\n')
                            continue
                        f.write(kstr[j])
                        f.write('\n')
                    f.write('\n')
            return dst
        else:  # 不存在就创建文件
            mkfile(filepath, filename, fileType)
            return writeyml(filepath, filename, fileType, list)
    else:
        return "目标目录不存在"


def add_blank(lstr, arg):
    blank = ''
    for i in range(arg):
        blank = blank + ' '
    kstr = []
    for key in lstr:
        kstr.append(blank + key + ': ' + lstr[key])
    return kstr


def readyml_2(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            result = yaml.load(f.read(), Loader=yaml.Loader)  # 加上Loader=yaml.Loader 避免警告
        return result
    else:
        return "目标文件不存在"


def readyml(filepath, filename, fileType):
    if os.path.isdir(filepath):
        dst = os.path.join(filepath, filename + fileType)
        if os.path.isfile(dst):
            with open(dst, 'r', encoding='utf-8') as f:
                result = yaml.load(f.read(), Loader=yaml.Loader)  # 加上Loader=yaml.Loader 避免警告
            return result
        else:
            return "目标文件不存在"
    else:
        return "目标目录不存在"


def quotes_str(lstr):  # 给字符串加上 双引号""
    qlist = ''.join(("\"", lstr, "\""))
    return qlist


def quotes_list_dic(list, *arg):  # 给字典中的 指定元素加上双引号
    for i in range(len(list)):
        for j in range(len(arg)):
            list[i][arg[j]] = quotes_str(list[i][arg[j]])
    return list


def slash2slashs(list, stra, strb):
    for i in range(len(list)):
        for key in list[i]:
            list[i][key] = eval(repr(list[i][key]).replace(stra, strb))
    return list



