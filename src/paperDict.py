#python3 Steven 09/18/20
'''AL/CV/DL/CNN... Paper class'''

from dictObject import dictObject

class Paper(dictObject):
    Keys = ['Author','Year','Name','Url','Description']
    def __init__(self, author, year='', name='',url='',desc=''):
        super().__init__()

        index=0    
        self.addAttr(Paper.Keys[index],author)
        index+=1
        self.addAttr(Paper.Keys[index],year)
        index+=1
        self.addAttr(Paper.Keys[index],name)
        index+=1
        self.addAttr(Paper.Keys[index],url)
        index+=1
        self.addAttr(Paper.Keys[index],desc)
        index+=1
    
    
if __name__=='__main__':
    print(__doc__)
    a = Paper('Geoffrey Hinton','2020','University','https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en&oi=ao','DL')
    print(a.getAttr('Name'))
    a.printAll()