# _*_ coding:utf-8 _*_

class SaveData(object):
    def __init__(self):
        self.savefile = open('gmp_info.txt', 'wb')

    def savefile2(self,gmp_infos):

       for gmp_info in gmp_infos:
           data = gmp_info['province'] + '\t' + gmp_info['certificateNumber'] + '\t' + gmp_info['enterpriseName'] + '\t' + gmp_info['address'] + '\t' +\
           gmp_info['certificationScope'] + '\t' + gmp_info['dateOfIssue'] + '\t' + gmp_info['expireDate'] + '\t' + gmp_info['continueDate'] +'\t' + \
           gmp_info['validTill'] + '\t' + gmp_info['continueScope'] + '\t' + gmp_info['gmpVersion']

           print data
           self.savefile.write(data)
           self.savefile.flush()


    def close(self):
        self.savefile.close()

