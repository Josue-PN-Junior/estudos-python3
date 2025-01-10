"""
    Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""
from time import sleep
import requests

print("~ Site está acessível?", '-'*27)
print("\tVerificando se o site http.cat está acessível...")
sleep(1)
print("~ Resultado", '-'*38)
try:
    requests.get("https://http.cat/")
except:
    print("\033[31m\t# Não foi possível acessar o site!\033[m")
else :
    print("\033[32m\t* Foi possível acessar o site!\033[m")