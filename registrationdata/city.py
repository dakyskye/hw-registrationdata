from enum import Enum


class City(Enum):
    TBILISI = "Tbilisi"
    KUTAISI = "Kutaisi"
    BATUMI = "Batumi"
    OTHER = "Other"

    @classmethod
    def by_id(cls, user_id):
        ids_and_cities = {'0101': cls.TBILISI, '0102': cls.TBILISI, '0103': cls.TBILISI}
        return ids_and_cities.get(user_id, cls.OTHER)
