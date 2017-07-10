# _*_ coding: utf-8 _*_

from GMP import main

base = 'http://qy1.sfda.gov.cn/datasearch/face3/content.jsp?tableId=23&tableName=TABLE23&tableView=GMP认证&Id='
spider = main.gmpSpider()
spider.getGMPinfo(base)