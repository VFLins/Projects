import sqlalchemy as alch
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from time import sleep
from platform import system
from os import mkdir, chdir
from os.path import isdir, expanduser

DB_DECBASE = declarative_base()
SYS_NAME = system()

try:
   if SYS_NAME == "Windows":
      WORK_DIR = expanduser("~") + "\\Appdata\\Roaming\\Cashd"
      if not isdir(WORK_DIR): mkdir(WORK_DIR)
   elif SYS_NAME == "Darwin":
      WORK_DIR = expanduser("~") + "\\Library\\\Preferences\\Cashd"
      if not isdir(WORK_DIR): mkdir(WORK_DIR)
   elif SYS_NAME =="Linux":
      WORK_DIR = expanduser("~") + "\\.local\\Share\\Cashd"
      if not isdir(WORK_DIR): mkdir(WORK_DIR)
   chdir(WORK_DIR)
except Exception as manage_dir_error:
   sleep_time = 30
   print("ERRO FATAL:\n", manage_dir_error, "\nFechando em 30 segundos...", sep="")
   sleep(30)
   quit()

if SYS_NAME == "Windows":
   DB_ENGINE = alch.create_engine("sqlite:///DB.sqlite")
else:
   DB_ENGINE = alch.create_engine("sqlite:////DB.sqlite")

#DB_METADATA = alch.MetaData(bind = DB_ENGINE)

DB_SESSION = sessionmaker(bind = DB_ENGINE)
DB_MSESSION = DB_SESSION()

class tb_entry(DB_DECBASE):
   __tablename__ = "entry"
   Id = alch.Column(alch.Integer, primary_key = True)
   Data = alch.Column(alch.Date)
   Hora = alch.Column(alch.Time)
   Valor = alch.Column(alch.Float)

   def __repr__(self):
      return "<entry(Data={}, Hora={}, Valor={})>".format(
         self.Data, self.Hora, self.Valor
      )

DB_DECBASE.metadata.create_all(DB_ENGINE)
