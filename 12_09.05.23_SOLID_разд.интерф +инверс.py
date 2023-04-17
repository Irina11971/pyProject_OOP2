from abc import ABC, abstractmethod
from copy import copy

# Задание 1.
# Рассмотрим принцип разделения интерфейсов.
# Допустим у нас имеется абстрактный класс Payments и в нем есть три метода:
# оплата WebMoney, оплата банковской карточкой и оплата по номеру телефона.
# class Payments(ABC):
# @abstarctmethod
# def payWebMoney(self): pass
# @abstarctmethod
# def payCreditCard(self): pass
# @abstarctmethod
# def payPhoneNumber(self): pass
# Выполните разделение интерфейса таким образом, чтобы можно было реализовать
# два класса-сервиса, которые будут у себя реализовывать различные виды проведения
# оплат (класс def payPhoneNumber(self): pass и TerminalPaymentService). При этом
# TerminalPaymentService не должен поддерживать проведение оплат по номеру телефона.

class WebMoney(ABC):
    @abstractmethod
    def payWebMoney(self):
        pass
class CreditCard(ABC):
    @abstractmethod
    def payCreditCard(self):
        pass
class PhoneNumber(ABC):
    @abstractmethod
    def payPhoneNumber(self):
        pass

class PayPhoneNumber(PhoneNumber, WebMoney):
    def payPhoneNumber(self):
        # TODO: реализовать логику оплаты по номеру телефона
        pass
    def payWebMoney(self):
        # TODO: реализовать логику оплаты веб-деньгами
        pass

class TerminalPaymentService(CreditCard, WebMoney):
    def payCreditCard(self):
        # TODO: реализовать логику оплаты по кредитной карте
        pass
    def payWebMoney(self):
        # TODO: реализовать логику оплаты веб-деньгами
        pass

# Задание 2.
# Рассмотрим принцип инверсии зависимостей. Исправьте следующий код таким
# образом, чтобы классы и верхних, и нижних уровней зависели от одних и тех же
# абстракций, а не от конкретных реализаций.
# class AnonymousAuthentication:
# def doAauthentication(self): pass
# class GithubAuthentication:
# def doAuthentication(self): pass
# class FacebookAuthentication:
# def doAuthentication(self): pass
# class Permissions:
# def __init__(self, auth: AnonymousAuthentication)
# self.auth = auth
# def getPermissions(self):
# self.auth.doAuthentication()


class AnonymousAuthentication(ABC):
    def doAuthentication(self, login: str, password: str):
        pass

class GithubAuthentication(AnonymousAuthentication):
    def doAuthentication(self, login: str, password: str):
        # TODO: реализовать логику регистрации в Github
        pass

class FacebookAuthentication(AnonymousAuthentication):
    def doAuthentication(self, login: str, password: str):
        # TODO: реализовать логику регистрации в фейсбуке
        pass

class Permissions:
    def __init__(self, auth: AnonymousAuthentication):
        self.__auth = copy(auth)
    def getPermissions(self, login: str, password: str):
        self.__auth.doAuthentication(login, password)

