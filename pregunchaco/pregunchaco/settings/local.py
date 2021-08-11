from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'JUEGO',
        'Trusted_Connection':'yes',
        'HOST':'localhost\\SQLEXPRESS01',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    }
}

#Prueba gitignore