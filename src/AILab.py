#python3 Steven 09/18/20
'''AILab class'''

from dictObject import dictObject

class AILab(dictObject):
    Keys = ['Name','Url','Description']
    def __init__(self, name='',url='',desc=''):
        super().__init__()

        index=0    
        self.addAttr(AILab.Keys[index],name)
        index+=1
        self.addAttr(AILab.Keys[index],url)
        index+=1
        self.addAttr(AILab.Keys[index],desc)
 
 
AILabs = [] #AILab list

AILabs.append( AILab(name = 'Stanford AI Lab', \
        url= 'https://ai.stanford.edu/', \
        desc = 'Stanford AI Lab') )

AILabs.append( AILab(name = 'MIT CSAIL', \
        url= 'https://www.csail.mit.edu/', \
        desc = 'MIT AI Lab') )

AILabs.append( AILab(name = 'GOOGLE AI', \
        url= 'https://ai.google/', \
        desc = 'GOOGLE AI') )

AILabs.append( AILab(name = 'CMU CS', \
        url= 'https://www.cs.cmu.edu/', \
        desc = 'CMU CS') )
