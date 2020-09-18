#python3 Steven 09/17/20
'''AL/CV/DL/CNN... Readme.md create'''
import os
from personDict import Scientist
from scientists import scientists
from paperDict import Paper
from papers import papers
from AILab import AILab,AILabs

gFile = r'../README.md'

def getMarkDownUrl(str,url):
    return '[{str}]({url})'.format(str=str,url=url)

def writePerson(file,i):
    strPerson = '|'
    for k in Scientist.Keys:
        #print(k,i.getAttr(k))
        if k == Scientist.Keys[3]: #papers
            papers = i.getAttr(k).getDict()
            #print('papers=',papers)
            for p in papers:
                url = getMarkDownUrl(p,papers[p])
                strPerson += url
                strPerson += ', '
            strPerson += '|'
                
        elif k == Scientist.Keys[4] or k == Scientist.Keys[5] \
             or k == Scientist.Keys[6] : #GoogleScholar or wiki, website
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
    
def getMarkdownTableH(columns):
    strHeader = '|'
    strHeaderFmt = '|'
    for k in columns:
        strHeader += (k+'|')
        strHeaderFmt += ('---'+'|')
    strHeader += '\n'
    strHeaderFmt += '\n'
    return strHeader,strHeaderFmt

def writeScientists(file,scientists):
    content = ''
    content += '# AI/DeepLearning Star Scientists\n\n'
    
    strHeader,strHeaderFmt = getMarkdownTableH(Scientist.Keys)
    
    content += strHeader
    content += strHeaderFmt
    
    writeToFile(file,content)
    for i in scientists:
        writePerson(file,i)
        
def writePapers(file,papers):
    content = '\n\n'
    content += '# AI/DeepLearning/CV famous Papers\n\n'
    
    strHeader,strHeaderFmt = getMarkdownTableH(Paper.Keys)
    
    content += strHeader
    content += strHeaderFmt
    
    writeToFile(file,content)
    for i in papers:
        strPaper = '|'
        for k in Paper.Keys:
            #print(k,i.getAttr(k))
            if k == Paper.Keys[3]: #url                
                url = i.getAttr(k)
                strPaper += (getMarkDownUrl('paper',url) + '|')
            else:
                strPaper += (i.getAttr(k) + '|')
        strPaper += '\n'
        writeToFile(file,strPaper)
    
def writeLabs(file,AILabs):
    content = '\n\n'
    content += '# AI Labs\n\n'
    
    strHeader,strHeaderFmt = getMarkdownTableH(AILab.Keys)
    content += strHeader
    content += strHeaderFmt
    writeToFile(file,content)
    
    for i in AILabs:
        strLib = '|'
        for k in AILab.Keys:
            strLib += (i.getAttr(k) + '|')
        strLib += '\n'
        writeToFile(file,strLib)
        
def createReadme(file):
    removeFile(file)
    writeScientists(file,scientists)
    writePapers(file,papers)
    writeLabs(file,AILabs)
    
def writeToFile(fileName,content):
        with open(fileName,'a',newline='\n',encoding='utf-8') as dstF:
            dstF.write(content)
            
def removeFile(fileName=gFile):
        """remove svg file if already exist"""
        if os.path.exists(fileName):
            os.remove(fileName)  
                      
if __name__=='__main__':
    createReadme(gFile)