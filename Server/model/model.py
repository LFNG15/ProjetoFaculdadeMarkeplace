class Seller:
    def __init__(self, name, id, cnpj):
        self.name = name
        self.id = id
        self.cnpj = cnpj

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'cnpj': self.cnpj
        }