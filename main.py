#python3 Steven 09/17/20
'''AL/CV/DL/CNN... scientist Readme.md create'''
import os
from personDict import scientist
from scientists import scientists

gFile = r'./README.md'

def getMarkDownUrl(str,url):
    return '[{str}]({url})'.format(str=str,url=url)

def writePerson(file,i):
    strPerson = '|'
    for k in scientist.Keys:
        print(k,i.getAttr(k))
        if k == scientist.Keys[3]: #papers
            papers = i.getAttr(k)
            print('papers=',papers)
            for p in papers:
                url = getMarkDownUrl(p,papers[p])
                strPerson += url
                strPerson += ', '
            strPerson += '|'
                
        elif k == scientist.Keys[4] or k == scientist.Keys[5] \
             or k == scientist.Keys[6] : #GoogleScholar or wiki, website
            url=i.getAttr(k)
            if url:
                scholar = getMarkDownUrl(k,url)
                strPerson += (scholar + '|')
            else:
                strPerson += '|'
    
        else:
            strPerson += (i.getAttr(k) + '|')
    strPerson += '\n'
    writeToFile(file,strPerson)
    
def createReadme(file,scientists):
    removeFile(file)
    content = ''
    content += '# AI/CV/DL/CNN Star Scientist List\n\n'
    
    strHeader = '|'
    strHeaderFmt = '|'
    for k in scientist.Keys:
        strHeader += (k+'|')
        strHeaderFmt += ('---'+'|')
    strHeader += '\n'
    strHeaderFmt += '\n'
    
    content += strHeader
    content += strHeaderFmt
    
    writeToFile(file,content)
    for i in scientists:
        writePerson(file,i)
    
def writeToFile(fileName,content):
        with open(fileName,'a',newline='\n',encoding='utf-8') as dstF:
            dstF.write(content)
            
def removeFile(fileName=gFile):
        """remove svg file if already exist"""
        if os.path.exists(fileName):
            os.remove(fileName)  
                      
if __name__=='__main__':
    createReadme(gFile, scientists)