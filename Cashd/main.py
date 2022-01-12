# import PySimpleGUI as sgui
import os
import time
import platform as pf
import datetime as dt

def shortcut_handle(shortcut):
   if shortcut.upper() == "HOJE":
      return dt.date.today()
   elif shortcut.upper() == "AGORA":
      return dt.datetime.now().strftime("%H:%M:%S")

def inp_date_handle():
   try:
      str_input = input("Insira a data (ddmmaaaa):\n")
      tru_date = str(dt.date(
         year = int( str_input[4:] ), 
         month = int( str_input[2:4] ), 
         day = int( str_input[0:2] )
      ))
      return tru_date
   except:
      str_input = input("Insira a data (ddmmaaaa):\n")
      tru_date = shortcut_handle( str_input )
      if bool(dt.datetime.strptime(tru_date, "%Y-%m-%d")):
         return tru_date
      else:
         print("Data inválida!\n\n")
         prompter()

def inp_time_handle():
   try:
      str_input = input("Insira o horário (hhmmss):\n")
      tru_time = dt.time(
         second = int( str_input[4:] ),
         minute = int( str_input[2:4] ),
         hour = int( str_input[0:2] )
      )
      return tru_time
   except ValueError:
      str_input = input("Insira o horário (hhmmss):\n")
      tru_time = shortcut_handle( str_input )
      if bool(dt.datetime.strptime(tru_time, "%H:%M:%S")):
         return tru_time
      else:
         raise Exception("Valor icorreto para este campo!")
   except:
      print("Horário inválido!\n\n")
      prompter()

def inp_numeric_handle():
   try:
      str_input = input("Insira o valor (0000.00):\n")
      return float( str_input )
   except:
      print("Valor inválido!\n\n")
      prompter()

def manage_dir():
   global work_dir
   try:
      if pf.system() == "Windows":
         work_dir = os.path.expanduser("~") + "\\Appdata\\Roaming\\Cashd"
         if not os.path.isdir(work_dir):
            os.mkdir(work_dir)
      elif pf.system() == "Darwin":
         work_dir = os.path.expanduser("~") + "\\Library\\\Preferences\\Cashd"
         if not os.path.isdir(work_dir):
            os.mkdir(work_dir)
      elif pf.system() =="Linux":
         work_dir = os.path.expanduser("~") + "\\Cashd"
         if not os.path.isdir(work_dir):
            os.mkdir(work_dir)
      os.chdir(work_dir)
   except Exception as manage_dir_error:
      print(manage_dir_error)
      countdown_message("Não foi possível definir pasta de trabalho, fechando em")

def data_storage(array):
   """Save the array of inputs in a text file"""
   manage_dir()
   regfile = open("input_reg.csv", "a")
   for item in array:
      regfile.write(item)
   regfile.close()

def countdown_message(message, seconds = 5):
   while seconds > 0:
      print(message, seconds, end = "\r")
      time.sleep(1)
      seconds -= 1

def prompter():
   inp_date = inp_date_handle()
   inp_time = inp_time_handle()
   inp_value = inp_numeric_handle()
   try:
      data_storage(
         [str(inp_date)+",", str(inp_time)+",", str(inp_value), "\n"]
      )
      print("Dados armazenados!\n")
   except Exception as prompter_error:
      print(prompter_error)
      countdown_message("Falha no aramazenamento dos dados, fechando em")
   finally:
      prompter()

manage_dir()
print(
    "Bem vindo ao Cashd, seus dados serão salvos em: ",
    work_dir + "\\input_reg.csv\n",
    "Você pode sempre inserir 'P' para entrar com a data ou horário atual.",
    sep = ""
)
prompter()