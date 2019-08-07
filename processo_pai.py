import os


programa = "google-chrome"
args = ['www.google.com']

print("Iniciando processo pai...")
input("Digite ENTER")

os.execvp(programa, (programa,) + tuple(args))

print("Finalizando processo pai...")
