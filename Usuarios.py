import Data


def add(object):
    try:
        return Data.add('Usuarios', object)
    except:
        return False


def get():
    try:
        return Data.getall('Usuarios')
    except:
        return None
