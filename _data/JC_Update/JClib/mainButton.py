__author__ = 'Rong_kang_Xiong'
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.join(os.getcwd(), "JClib"))  #添加lib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime
from PyQt5 import QtWidgets, QtCore
from JCGUI import Ui_MainWindow
from functools import partial
from openUrl import openurl
import get_Inf_from_DOI
from Bibtex2dic import *
from JClib import config


class mainButton(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(mainButton, self).__init__(parent)
        self.setupUi(self)
        #初始化参数
        self.Presenter = ''
        self.title = ''
        self.authors = ''
        self.URLLink = ''
        self.rawPDF = ''
        self.PDFLink = ''
        self.date = ''
        self.time = ''
        self.datetime = ''
        self.location = ''
        self.doidic = []   # Bibtex需要形如 这样取出值 self.title = delbracket(bib2dic(doitext)['title'])
        self.ymlall = []
        self.ymlnew = {}
        self.markdow_Name = ''

        self.nutstore_Weekly = config.get('nutstore_Weekly')
        self.nutstore_Theory = config.get('nutstore_Theory')
        self.markdown_Weekly = config.get('markdown_Weekly')
        self.markdown_Theory = config.get('markdown_Theory')
        self.Weekly_place = config.get('Weekly_place')
        self.Theory_place = config.get('Theory_place')
        self.Weekly_Time = config.get('Weekly_Time')
        self.Report_Time = config.get('Report_Time')
        self.Theory_Time = config.get('Theory_Time')

    #将相应函数绑定到指定Button
        self.commandLinkButton_webJC_1.clicked.connect(partial(openurl, "https://cneuroustc.github.io/"))  #
        self.commandLinkButton_meeting_md_1.clicked.connect(partial(openurl, "https://github.com/Wenlab/Administration/blob/master/groupMeeting.md"))
        self.commandLinkButton_homepage_1.clicked.connect(partial(openurl, "http://www.wenlab.org/"))

        #链接 "获取Bibtex" button
        self.pushButton_get_info_1.clicked.connect(self.btnpress_getBibtex_inf_1)
        self.pushButton_get_info_2.clicked.connect(self.btnpress_getBibtex_inf_2)
        #链接 "复制Bibtex" button
        self.pushButton_copyBibtex_1.clicked.connect(self.btnpress_copy2blackboard_1)
        self.pushButton_copyBibtex_2.clicked.connect(self.btnpress_copy2blackboard_2)
        #链接 "打开DOI链接" button
        self.pushButton_openDOI_1.clicked.connect(self.btnpress_openDOI_1)
        self.pushButton_openDOI_2.clicked.connect(self.btnpress_openDOI_2)
        #链接 "选择文件" button
        self.file_pushButton_1.clicked.connect(partial(self.open_file, 'nutstore_Weekly'))  #pdf的路径
        self.file_pushButton_2.clicked.connect(partial(self.open_file, 'nutstore_Theory'))
        #链接 "打开URL Link" button
        self.pushButton_URL_Link_1.clicked.connect(self.btnpress_openURL_1)
        self.pushButton_URL_Link_2.clicked.connect(self.btnpress_openURL_2)
        #链接 "打开PDF 坚果云" button
        self.pushButton_PDF_Link_1.clicked.connect(self.btnpress_openPDF_1)
        self.pushButton_PDF_Link_2.clicked.connect(self.btnpress_openPDF_2)
        #链接 "清空日志"
        self.pushButton_clear_log_1.clicked.connect(self.btnpress_clear_log_1)
        self.pushButton_clear_log_2.clicked.connect(self.btnpress_clear_log_2)
        self.pushButton_clear_log_2.clicked.connect(self.btnpress_clear_log_2)

        #链接 "日历" 控件
        # 如果我们从部件选择一个日期,点击[QDate]发出信号。我们将这个信号连接到用户定义的show_Date()方法
        self.calendarWidget_1.setGridVisible(True)   #有网格
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_3.setGridVisible(True)
        self.calendarWidget_1.clicked[QDate].connect(self.onDateChanged)
        self.calendarWidget_2.clicked[QDate].connect(self.onDateChanged)
        self.calendarWidget_3.clicked[QDate].connect(self.onDateChanged)

        #时间控件
        # 时间改变时触发
        #设置默认时间
        year_time = self.getCurrentDateTime()
        Weekly_time = config.time2num(config.get('Weekly_Time'))
        self.timeEdit_1.setDateTime(QtCore.QDateTime(QtCore.QDate(int(year_time[0]), int(year_time[1]), int(year_time[2])), QtCore.QTime(Weekly_time[0], Weekly_time[1], Weekly_time[2]))) #设置默认时间
        self.timeEdit_1.timeChanged.connect(self.onTimeChanged)

        Theory_time = config.time2num(config.get('Theory_Time'))
        self.timeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(int(year_time[0]), int(year_time[1]), int(year_time[2])), QtCore.QTime(Theory_time[0], Theory_time[1], Theory_time[2])))
        self.timeEdit_2.timeChanged.connect(self.onTimeChanged)

        Report_time = config.time2num(config.get('Report_Time'))
        self.timeEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(int(year_time[0]), int(year_time[1]), int(year_time[2])), QtCore.QTime(Report_time[0], Report_time[1], Report_time[2])))
        self.timeEdit_3.timeChanged.connect(self.onTimeChanged)

        #链接 "更新信息" button
        self.pushButton_refresh_info_1.clicked.connect(self.btn_refresh_info_1)
        self.pushButton_refresh_info_2.clicked.connect(self.btn_refresh_info_2)
        self.pushButton_refresh_info_3.clicked.connect(self.btn_refresh_info_3)


        # 链接 "更新JC" button
        self.update_JC_1.clicked.connect(self.btnpress_update_JC_1)
        self.update_JC_2.clicked.connect(self.btnpress_update_JC_2)
        self.update_JC_3.clicked.connect(self.btnpress_update_JC_3)

        #链接 "清除内存信息"
        self.clear_Info_pushButton.clicked.connect(self.clearAllInfo)


    def show_msg(self, msg):   #在消息框中输出消息
        if not isinstance(msg, str):
            self.text_paper_Browser_1.append("参数非字符串")
            self.text_paper_Browser_2.append("参数非字符串")
            self.text_paper_Browser_3.append("参数非字符串")
        else:
            # msg = '\n'+msg +'\n'+str(self.getCurrentDateTime())  #空一行再写入消息
            msg = '\n'+msg + '\n'+'消息时间:'+self.DateTime2str(self.getCurrentDateTime(), 6)
            self.text_paper_Browser_1.append(msg)
            self.text_paper_Browser_2.append(msg)
            self.text_paper_Browser_3.append(msg)


    def show_Date(self, date):   #显示日期
        self.show_msg("日期:"+date.toString("yyyy-MM-dd"))
        # return date.toString("yyyy-MM-dd")

    #时间改变时显示信息
    def onTimeChanged(self, time):
        self.time = time.toString('hh:mm')
        self.show_msg(time.toString('hh:mm'))

    #日期改变时显示信息
    def onDateChanged(self, date):
        # 年:月:日 [星期]
        self.date = date.toString('yyyy/MM/dd')
        self.show_msg(self.date)
        self.show_msg(date.toString('yyyy/MM/dd [ddd]'))

    #时间日期改变时显示信息
    def onDateTimeChanged(self, dateTime):
        self.datetime = dateTime.toString('yyyy/MM/dd, hh:mm:ss')
        self.show_msg(dateTime.toString('yyyy:MM:dd [ddd] hh:mm:ss'))

    def getCurrentDateTime(self):   #返回当前时间(0,1,2,3)
        #获得当前时间
        timestr = str(QDateTime.currentDateTime())
        timestr = timestr.replace('PyQt5.QtCore.QDateTime(', '')  #去掉左边括号和字符串
        timestr = timestr.replace(')', '')   #去掉右边括号和字符串
        timestr = timestr.split(',', maxsplit=-1)
        for i in range(len(timestr)):
            timestr[i] = timestr[i].rstrip()
            timestr[i] = timestr[i].lstrip()
        return timestr

    def QtDate2str(self, arg):   #返回PyQt5.QtCore.QDate(2021, 7, 31)形式日期的字符串list
        timestr = str(arg)
        timestr = timestr.replace('PyQt5.QtCore.QDate(', '')  # 去掉左边括号和字符串
        timestr = timestr.replace(')', '')  # 去掉右边括号和字符串
        timestr = timestr.split(',', maxsplit=-1)
        for i in range(len(timestr)):
            timestr[i] = timestr[i].rstrip()
            timestr[i] = timestr[i].lstrip()
        return timestr

    def QtTime2ampm(self, arg):  #10:00:00
        time = str(arg)
        time = time.split(':', maxsplit=-1)
        if int(time[0])<12:
            ampm = 'am'
        else:
            ampm = 'pm'
        return time[0]+':'+time[1]+ampm

    def DateTime2str(self, DateTime, dtlen = 7):  #将时间转换为字符串 例如2021/7/23/19/20/05/345
        dtstr = ''
        if dtlen > len(DateTime):
            dtlen = len(DateTime)
        else:
            for i in range(dtlen):
                if i == 0:
                    dtstr = dtstr + DateTime[i]
                else:
                    dtstr = dtstr + r'/' + DateTime[i]
        return dtstr


    def default_config(self, arg):
        return config.get(arg)

    def open_file(self, arg):
        '''
        fileName = 'G:/Data/WenLab/JC_Update/SD.pdf'
        fileType = '*.pdf'
        '''
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(), "All Files(*.pdf)")
        self.rawPDF = fileName
        #复制文件到目录
        self.show_msg("选择文件："+self.rawPDF)
        self.show_msg("坚果云路径：" + config.get(arg))

        return fileName

    # def btnpress_ref_info_1(self):
    #     self.show_msg(QTime)

    #更新信息
    def btn_refresh_info_1(self):
        #更新坚果云链接信息，还有时间日期，Presenter，place

        self.PDFLink = self.PDF_link_1.toPlainText().strip()
        self.show_msg('PDF Link:'+self.PDFLink)
        date = self.QtDate2str(self.calendarWidget_1.selectedDate())
        self.date = date2str(date, r'/', 3)  # [2021,07,23]的list
        self.show_msg('date:'+self.date)
        self.time = self.timeEdit_1.time().toString('hh:mm')
        self.show_msg('time:'+self.time)
        self.datetime = self.date + ', ' + self.time
        self.show_msg('Datetime:'+self.datetime)

        self.location = self.place_1.toPlainText()
        self.show_msg('Place:'+self.location)
        self.Presenter = self.Presenter_1.toPlainText()
        self.show_msg('Presenter:'+self.Presenter)

        self.markdownname = getmarkdown_name(date, self.Presenter)
        self.show_msg('Markdown name:'+self.markdownname)
        self.show_msg('参数更新成功')

    def btn_refresh_info_2(self):
        #更新坚果云链接信息，还有时间日期，Presenter，place

        self.PDFLink = self.PDF_link_2.toPlainText().strip()
        self.show_msg('PDF Link:' + self.PDFLink)
        date = self.QtDate2str(self.calendarWidget_2.selectedDate())
        self.date = date2str(date, r'/', 3)  # [2021,07,23]的list
        self.show_msg('date:' + self.date)
        self.time = self.timeEdit_2.time().toString('hh:mm')
        self.show_msg('time:' + self.time)
        self.datetime = self.date + ', ' + self.time
        self.show_msg('Datetime:' + self.datetime)

        self.location = self.place_2.toPlainText()
        self.show_msg('Place:' + self.location)
        self.Presenter = self.Presenter_2.toPlainText()
        self.show_msg('Presenter:' + self.Presenter)

        self.markdownname = getmarkdown_name(date, self.Presenter)
        self.show_msg('Markdown name:' + self.markdownname)
        self.show_msg('参数更新成功')

    def btn_refresh_info_3(self):
        #更新坚果云链接信息，还有时间日期，Presenter，place

        self.PDFLink = 'None'
        self.show_msg('PDF Link:'+self.PDFLink)
        date = self.QtDate2str(self.calendarWidget_3.selectedDate())
        self.date = date2str(date, r'/', 3)  # [2021,07,23]的list
        self.show_msg('date:'+self.date)
        self.time = self.timeEdit_3.time().toString('hh:mm')
        self.show_msg('time:'+self.time)
        self.datetime = self.date + ', ' + self.time
        self.show_msg('Datetime:'+self.datetime)

        self.location = self.place_3.toPlainText()
        self.show_msg('Place:'+self.location)
        self.Presenter = self.Presenter_3.toPlainText()
        self.show_msg('Presenter:'+self.Presenter)
        self.show_msg('参数更新成功')

    #更新JC
    def btnpress_update_JC_1(self):
        presenter = self.Presenter
        date = self.QtDate2str(self.calendarWidget_1.selectedDate())
        date = date[0]+'/'+date[1]+'/'+date[2]
        time = self.QtTime2ampm(self.timeEdit_1.time().toString())
        datetime = date+', '+time

        paper = self.title
        url = self.URLLink
        pdf = self.PDFLink
        author = self.authors

        location = self.location
        self.show_msg(presenter)
        self.show_msg(datetime)
        self.show_msg(paper)
        self.show_msg(url)
        self.show_msg(author)
        newymlone, markdowname = getyamlfile(presenter, datetime, paper, url, pdf, author, location, 1)

        #写入yml文件
        ymlpath = config.get('ymlpath')
        ymlpath = changeyaml(ymlpath, newymlone)

        #新建Markdown文件
        mdpath = config.get('markdown_Weekly')
        mdpath = copyfile.mkfile(mdpath, self.markdownname, '.md')
        self.show_msg(mdpath)

        self.show_msg(ymlpath)
        self.show_msg('更新JC成功！')
        return 0

    def btnpress_update_JC_2(self):
        presenter = self.Presenter
        date = self.QtDate2str(self.calendarWidget_2.selectedDate())
        date = date[0] + '/' + date[1] + '/' + date[2]
        time = self.QtTime2ampm(self.timeEdit_2.time().toString())
        datetime = date + ', ' + time


        paper = self.title
        url = self.URLLink
        pdf = self.PDFLink
        self.show_msg('pdf nut link'+pdf)
        author = self.authors

        location = self.location
        self.show_msg(presenter)
        self.show_msg(datetime)
        self.show_msg(paper)
        self.show_msg(url)
        self.show_msg(author)
        newymlone, markdowname = getyamlfile(presenter, datetime, paper, url, pdf, author, location, 2)

        ymlpath = config.get('ymlpath')
        ymlpath = changeyaml(ymlpath, newymlone)

        # 新建Markdown文件
        mdpath = config.get('markdown_Theory')
        mdpath = copyfile.mkfile(mdpath, self.markdownname, '.md')


        self.show_msg(mdpath)
        self.show_msg(ymlpath)

        self.show_msg('更新JC成功！')
        return 0

    def btnpress_update_JC_3(self):
        presenter = self.Presenter
        date = self.QtDate2str(self.calendarWidget_3.selectedDate())
        date = date[0] + '/' + date[1] + '/' + date[2]
        time = self.QtTime2ampm(self.timeEdit_3.time().toString())
        datetime = date + ', ' + time

        paper = self.title
        url = 'None'
        pdf = 'None'
        author = 'None'
        location = self.location
        self.show_msg(presenter)
        self.show_msg(datetime)
        self.show_msg(paper)
        self.show_msg(url)
        self.show_msg(author)
        newymlone, markdowname = getyamlfile(presenter, datetime, paper, url, pdf, author, location, 3)

        ymlpath = config.get('ymlpath')
        ymlpath = changeyaml(ymlpath, newymlone)
        self.show_msg(ymlpath)
        return 0


    #从DOI获取Bibtex
    def btnpress_getBibtex_inf_1(self):  #点击按钮后获取Bibtex信息，然后将其输出到右边的文本框中
        self.doitext = get_Inf_from_DOI.get(self.DOI_1.toPlainText())
        doitext = self.doitext
        if doitext == 'Invalid DOI': #doitext 是空的
            self.show_msg('DOI格式不正确,请断开网络代理 或 重新输入')
        else:
            self.show_msg('获取Bibtex')
            self.text_JC_Browser_1.setPlainText(doitext)  #将Bibtex输出到右侧

            self.title = delbracket(bib2dic(doitext)['title'])
            self.title_1.setPlainText(self.title)  #输出标题到title_1
            self.show_msg("文章标题:" + self.title)

            self.URLLink = delbracket(bib2dic(doitext)['url'])  #
            self.show_msg("文章URL:" + self.URLLink)
            self.URL_link_1.setPlainText(self.URLLink)   #输出URLLink到URL_link_1
            #

    def btnpress_getBibtex_inf_2(self):  #点击按钮后获取Bibtex信息，然后将其输出到右边的文本框中
        self.doitext = get_Inf_from_DOI.get(self.DOI_2.toPlainText())
        doitext = self.doitext
        if doitext == 'Invalid DOI':  # doitext 是空的
            self.show_msg('DOI格式不正确,请断开网络代理 或 重新输入')
        else:
            self.show_msg('获取Bibtex')
            self.text_JC_Browser_2.setPlainText(doitext)  # 将Bibtex输出到右侧

            self.title = delbracket(bib2dic(doitext)['title'])
            self.title_2.setPlainText(self.title)  # 输出标题到title_1
            self.show_msg("文章标题:" + self.title)

            self.URLLink = delbracket(bib2dic(doitext)['url'])  #
            self.show_msg("文章URL:" + self.URLLink)
            self.URL_link_2.setPlainText(self.URLLink)  # 输出URLLink到URL_link_1

    #复制Bibtex文本
    def btnpress_copy2blackboard_1(self):  # 复制Bibtex文本
        clipboard = QApplication.clipboard()
        self.show_msg("复制Bibtex到剪贴板")
        clipboard.setText(self.text_JC_Browser_1.toPlainText())

    def btnpress_copy2blackboard_2(self):  # 复制Bibtex文本
        clipboard = QApplication.clipboard()
        self.show_msg("复制Bibtex到剪贴板")
        clipboard.setText(self.text_JC_Browser_2.toPlainText())

    #在页面1 中打开DOI链接
    def btnpress_openDOI_1(self):
        doitext = self.text_JC_Browser_1.toPlainText()  #类型是str
        if doitext.isspace(): #doitext 是空的
            self.show_msg('DOI格式不正确')
        else:
            dic = bib2dic(doitext)
            url = delbracket(dic['url'])
            self.show_msg("Open :" + url)
            openurl(url)

    #在页面2打开DOI链接
    def btnpress_openDOI_2(self):
        doitext = self.text_JC_Browser_2.toPlainText()  # 类型是str
        if doitext.isspace():  #doitext 是空的
            self.show_msg('DOI格式不正确')
        else:
            dic = bib2dic(doitext)
            url = delbracket(dic['url'])
            self.show_msg("Open :" + url)
            openurl(url)

    def btnpress_openURL_1(self):
        url = self.URL_link_1.toPlainText()
        if url.isspace():
            self.show_msg('PDF 链接不正确')
        else:
            self.show_msg("Open :" + url)
            openurl(url)

    def btnpress_openURL_2(self):
        url = self.URL_link_2.toPlainText()
        if url.isspace():
            self.show_msg('PDF 链接不正确')
        else:
            self.show_msg("Open :" + url)
            openurl(url)

    #复制文件并重命名 然后 打开坚果云位置
    def btnpress_openPDF_1(self):
        '''
        复制并重命名PDF到坚果云文件夹
        然后打开坚果云文件夹
        '''
        # self.rawPDF = False 说明有PDF
        if not os.path.isfile(self.rawPDF):  # 如果没有选择了PDF文件
            self.show_msg('请选择PDF文件')
            return 'PDF not Found'
        else:
            url = self.nutstore_Weekly
            if url.isspace():
                self.show_msg('PDF 链接不正确')
            else:
                self.show_msg("Open :" + url)
                openurl(url)

            date = self.QtDate2str(self.calendarWidget_1.selectedDate())  # [2021,07,23]的list
            srcpath = self.rawPDF  # 类似 原PDF位置G:/Data/WenLab/JC_Update/SD.pdf
            self.show_msg(srcpath)

            self.show_msg('选择的JC日期' + date2str(date, '_', 3))
            paper = self.title
            pdfname = renamePDF(date, paper)

            # 如果是空的
            self.show_msg(copyfile.copy_rename_2(srcpath, config.get('nutstore_Weekly'), pdfname, ".pdf"))
            self.show_msg('Copy and rename success')
            # 然后打开坚果云文件夹

    def btnpress_openPDF_2(self):
        '''
                复制并重命名PDF到坚果云文件夹
                然后打开坚果云文件夹
        '''
        # self.rawPDF = False 说明有PDF
        if not os.path.isfile(self.rawPDF):  # 如果没有选择了PDF文件
            self.show_msg('请选择PDF文件')
            return 'PDF not Found'
        else:
            url = self.nutstore_Theory
            if url.isspace():
                self.show_msg('PDF 链接不正确')
            else:
                self.show_msg("Open :" + url)
                openurl(url)

            date = self.QtDate2str(self.calendarWidget_2.selectedDate())  # [2021,07,23]的list
            srcpath = self.rawPDF  # 类似 原PDF位置G:/Data/WenLab/JC_Update/SD.pdf
            self.show_msg(srcpath)

            self.show_msg('选择的JC日期' + date2str(date, '_', 3))
            paper = self.title
            pdfname = renamePDF(date, paper)

            # 如果是空的
            self.show_msg(copyfile.copy_rename_2(srcpath, config.get('nutstore_Theory'), pdfname, ".pdf"))
            self.show_msg('Copy and rename success')
            # 然后打开坚果云文件夹


    #清空消息日志
    def btnpress_clear_log_1(self):
        self.text_paper_Browser_1.setPlainText('')

    def btnpress_clear_log_2(self):
        self.text_paper_Browser_2.setPlainText('')

    def btnpress_clear_log_3(self):
        self.text_paper_Browser_2.setPlainText('')
    # def update_JC(self):

    def clearAllInfo(self):
        #清除窗口
        self.DOI_1.setPlainText('')
        self.title_1.setPlainText('')
        self.Presenter_1.setPlainText('')
        self.URL_link_1.setPlainText('')
        self.PDF_link_1.setPlainText('')
        self.text_JC_Browser_1.setPlainText('')
        self.text_paper_Browser_1.setPlainText('')

        self.DOI_2.setPlainText('')
        self.title_2.setPlainText('')
        self.Presenter_2.setPlainText('')
        self.URL_link_2.setPlainText('')
        self.PDF_link_2.setPlainText('')
        self.text_JC_Browser_2.setPlainText('')
        self.text_paper_Browser_2.setPlainText('')

        self.Presenter_3.setPlainText('')
        self.text_paper_Browser_3.setPlainText('')
        #清除变量
        self.Presenter = ''
        self.title = ''
        self.authors = ''
        self.URLLink = ''
        self.rawPDF = ''
        self.PDFLink = ''
        self.date = ''
        self.time = ''
        self.datetime = ''
        self.location = ''
        self.doidic = []  # Bibtex
        self.ymlall = []
        self.ymlnew = {}




