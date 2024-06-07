from enum import Enum

class UserRoles(Enum):
    ADMIN = 'admin'
    SHOP = 'shop'
    BUYER = 'buyer'

    @classmethod
    def choices(cls):
        return [(rol.value , rol.name) for rol in cls]