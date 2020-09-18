#python3 Steven 09/18/20
'''dictObject class'''

class dictObject():
    def __init__(self):
        self.dict = {}
        
    def getDict(self):
        return self.dict
    
    def getAttr(self,attr):
        return self.dict[attr] if attr in self.dict else None
    
    def addAttr(self,name,value):
        self.dict[name] = value
         
    def printAll(self):
        for i in self.dict:
            print(i,': ',self.dict[i])