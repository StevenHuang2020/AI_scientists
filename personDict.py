#python3 Steven 09/17/20
'''AL/CV/DL/CNN... scientist class'''

class scientist():
    Keys = ['Name','Description','Fields','Papers','GoogleScholar','Wiki','Website']
    def __init__(self, name, desc='', googleScholar='',fields='',wiki='',website=''):
        self.dict={}
        index=0
        self.dict[scientist.Keys[index]] = name
        index+=1
        self.dict[scientist.Keys[index]] = desc
        index+=1
        self.dict[scientist.Keys[index]] = fields
        index+=1
        self.dict[scientist.Keys[index]] = {}
        index+=1
        self.dict[scientist.Keys[index]] = googleScholar
        index+=1
        self.dict[scientist.Keys[index]] = wiki
        index+=1
        self.dict[scientist.Keys[index]] = website
        
    def getAttr(self,attr):
        return self.dict[attr] if attr in self.dict else None
    
    def addPapers(self,paperName,url):
        self.dict[scientist.Keys[3]][paperName] = url
         
    def printAll(self):
        for i in self.dict:
            print(i,': ',self.dict[i])
    
    
if __name__=='__main__':
    print(__doc__)
    a = scientist('Geoffrey Hinton','University of Toronto & Engineering Fellow, Google','https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en&oi=ao','DL',wiki='https://en.wikipedia.org/wiki/Geoffrey_Hinton')
    #a = scientist('Kunihiko Fukushima','https://en.wikipedia.org/wiki/Kunihiko_Fukushima','gg')
    a.addPapers('Imagenet classification with deep convolutional neural networks','http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf')
    a.printAll()
    print(a.getAttr('Name'))