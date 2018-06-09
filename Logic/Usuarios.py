from Data import Data

class Usuarios:


    def add(object):
        try:
            return Data.add('Usuarios', object)
        except:
            return False

