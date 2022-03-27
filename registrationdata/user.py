from dataclasses import dataclass

from registrationdata.city import City


class InvalidUserInfoError(Exception):
    pass


def _get_name():
    name = input("input your name and surname: ")
    name = name.split(' ')
    if len(name) != 2:
        raise InvalidUserInfoError("name and surname must be separated by a space")
    return tuple(name)


def _get_id():
    user_id = input("input your id: ")
    if len(user_id) != 11 or not user_id.isdigit():
        raise InvalidUserInfoError("user id must consist of eleven digits")
    return user_id


def _get_age():
    try:
        user_age = int(input("input your age: "))
        if user_age < 12:
            raise InvalidUserInfoError("user age must be greater than or equal to twelve")
    except ValueError:
        raise InvalidUserInfoError("user age must be a valid integer")
    return user_age


@dataclass
class User:
    uid: str
    first_name: str
    last_name: str
    age: int
    city: City

    @property
    def user_name(self):
        return f"{self.first_name} {self.last_name}"


def new_user() -> User:
    name = _get_name()
    uid = _get_id()
    age = _get_age()
    city = City.by_id(uid[:4])

    return User(uid, name[0], name[1], age, city)
