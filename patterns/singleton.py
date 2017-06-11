#!usr/bin/python

class DBConexion(object):
    __instance = None
    def __new__(self, val):
        if DBConexion.__instance is None:
            DBConexion.__instance = object.__new__(self)
        DBConexion.__instance.val = val
        return DBConexion.__instance

def main():
	b = DBConexion("valor")
	c = DBConexion("valor")
	if (id(b) == id(c)):
		print "Llamado a la base de datos"
	else:
		print "Ha fallado el llamado a la base de datos"
