from enum import Enum

class CatType(Enum):

    PHONE = 'phone'
    SHIRT = 'shirt'
    PANT = 'pant'
    TECH = 'tech'
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]