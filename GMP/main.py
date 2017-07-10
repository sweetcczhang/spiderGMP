# _*_ coding: utf-8 _*_

import paraserHtml
from GMP import downloadHtml

import saveToData
#import saveToDB
from bs4 import BeautifulSoup
import time
class gmpSpider(object):
    def __init__(self):
        self.download_html = downloadHtml.DownloadHtml()
        self.paraser_html = paraserHtml.HtmlParaser()
        self.save_data = saveToData.SaveData()
        #self.saveDb = saveToDB.ConnMysql()

    def getGMPinfo(self, base):
        page_i = 5000
        gmp_infos = list()
        while True:
            gmp_url = base+str(page_i)
            #print 'base url:', gmp_url
            page_html = self.download_html.download(gmp_url)
            #print 'page_html:',page_html
            if page_html == None:
                page_i += 1
                time.sleep(2)
                continue
            soup = BeautifulSoup(page_html, 'lxml')
            gmp_info = self.paraser_html.get_gmp_info(soup)
            if gmp_info == None:
                page_i += 1
                time.sleep(2)
                continue
            gmp_infos.append(gmp_info)

            data = gmp_info['province'] + '\t' + gmp_info['certificateNumber'] + '\t' + gmp_info[
                'enterpriseName'] + '\t' + gmp_info['address'] + '\t' + \
                   gmp_info['certificationScope'] + '\t' + gmp_info['dateOfIssue'] + '\t' + gmp_info['expireDate'] + '\t' + \
                   gmp_info['continueDate'] + '\t' + gmp_info['validTill'] + '\t' + gmp_info['continueScope'] + '\t' + gmp_info['gmpVersion']
            print data
            page_i += 1
            time.sleep(2)
            if len(gmp_infos) > 50:
                self.save_data.savefile2(gmp_infos)
                gmp_infos=list()




