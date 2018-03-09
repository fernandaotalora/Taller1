class Diccionario:
    def __init__(self,idWord,word):
        self.idWord = idWord
        self.word   = word
        
    def toDBCollection(self):
        return{
            "_id":self.idWord,
            "word":self.word
        }   