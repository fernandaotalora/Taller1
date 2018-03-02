class Documentos:
    def __init__(self,idDoc,documento):
        self.iddoc = idDoc
        self.documento = documento

    def toDBCollection (self):
        return {
            "_id":self.iddoc,
            "documento":self.documento
        }