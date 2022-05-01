from .geral_exceptions import IncorrectField, InvalidInput, MissingField


class InvalidName(InvalidInput):...
class InvalidProfessionCode(InvalidInput):...
class InvalidCPF(InvalidInput):...
class InvalidCPFFormat(IncorrectField):...
class InvalidPhone(InvalidInput):...
class InvalidPhoneFormat(IncorrectField):...
class InvalidEmail(InvalidInput):...
class InvalidProfession(InvalidInput):...
class PasswordHashError(MissingField):...