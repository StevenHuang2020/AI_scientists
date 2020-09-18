#python3 Steven 09/17/20
'''AL/CV/DL/CNN... Scientist class'''

from dictObject import dictObject

class Scientist(dictObject):
    Keys = ['Name','Description','Fields','Papers','GoogleScholar','Wiki','Website']
    def __init__(self, name, desc='', googleScholar='',fields='',wiki='',website=''):
        super().__init__()
        
        index=0    
        self.addAttr(Scientist.Keys[index],name)
        index+=1
        self.addAttr(Scientist.Keys[index],desc)
        index+=1
        self.addAttr(Scientist.Keys[index],fields)
        index+=1
        self.addAttr(Scientist.Keys[index],dictObject())
        index+=1
        self.addAttr(Scientist.Keys[index],googleScholar)
        index+=1
        self.addAttr(Scientist.Keys[index],wiki)
        index+=1
        self.addAttr(Scientist.Keys[index],website)
       
    def addPapers(self,paperName,url):
        self.dict[Scientist.Keys[3]].addAttr(paperName,url)
         
    
if __name__=='__main__':
    print(__doc__)
    a = Scientist('Geoffrey Hinton','University of Toronto & Engineering Fellow, Google','https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en&oi=ao','DL',wiki='https://en.wikipedia.org/wiki/Geoffrey_Hinton')
    #a = Scientist('Kunihiko Fukushima','https://en.wikipedia.org/wiki/Kunihiko_Fukushima','gg')
    a.addPapers('Imagenet classification with deep convolutional neural networks','http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf')
    a.printAll()
    print(a.getAttr('Name'))