#!/usr/bin/python
# _*_ coding: utf-8 _*_

from bs4 import BeautifulSoup
import re


class HtmlParaser(object):

     def get_gmp_info(self, soup):

         try:
             gmp_msg = soup.find(name='div', attrs={'class':'listmain'})
             print "error -2"
             tag_table = gmp_msg.find_all(name='table')
             print  'error -1'
             tag_tr = tag_table[0].find_all(name='tr')
             print 'error 0'
             gmp_info = dict()
             flags = 0
             gmp_info['province'] = tag_tr[1].find_all(name='td')[1].getText().strip()
             print "error province 1"
             gmp_info['certificateNumber'] = tag_tr[2].find_all(name='td')[1].getText().strip()
             print 'error certificateNumber 2'
             gmp_info['enterpriseName'] = tag_tr[3].find_all(name='td')[1].find(name='a').getText().strip()
             print 'error enterpriseName 3'
             gmp_info['address'] = tag_tr[4].find_all(name='td')[1].getText().strip()
             print 'error address 4'
             gmp_info['certificationScope'] = tag_tr[5].find_all(name='td')[1].getText().strip()
             print 'error certificationScope 5'
             gmp_info['dateOfIssue'] = tag_tr[6].find_all(name='td')[1].getText().strip()
             print 'error dateOfIssue 6'
             gmp_info['expireDate'] = tag_tr[7].find_all(name='td')[1].getText().strip()
             print 'error dateOfIssue 7'
             gmp_info['continueDate'] = tag_tr[8].find_all(name='td')[1].getText().strip()
             print 'error continueDate 8'
             gmp_info['validTill'] = tag_tr[9].find_all(name='td')[1].getText().strip()
             print 'error validTill 9'
             gmp_info['continueScope'] = tag_tr[10].find_all(name='td')[1].getText().strip()
             print 'error continueScope 10'
             gmp_info['gmpVersion'] = tag_tr[11].find_all(name='td')[1].getText().strip()
             print 'error gmpVersion 11'
             return gmp_info
         except :
             print 'exception:',None
             return None


