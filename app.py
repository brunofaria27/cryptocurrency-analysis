# IMPORTS
import requests
import json
import time
import colorama
from colorama import Fore, Back, Style
from pyfiglet import figlet_format

# Função criada para pesquisar determinada moeda no mercado
# param -> recebe o nome da moeda que deseja pesquisar
# return -> retorna o valor unitário em BRL da última negociação
def requestMB(crypto):
    request = requests.get(f"https://www.mercadobitcoin.net/api/{crypto}/ticker")
    payload = json.loads(request.content)
    crypto = payload['ticker']['last']
    return float(crypto)

# Função usada para mostrar a logo da aplicação
def logo():
    print(Fore.CYAN + "=============================================================================" + Style.RESET_ALL)
    print(figlet_format('Crypto Analysis', font="standard"))
    print(Fore.CYAN + "=============================================================================" + Style.RESET_ALL)

def menu():
    print(Fore.CYAN + "=============================================================================" + Style.RESET_ALL)
    print("Criptomoedas disponíveis: ")
    print("1 - BTC")
    print("2 - ADA")
    print("3 - ETH")
    print("4 - LTC")

# Funçõo utilizada para interagir com o usuário e pegar a criptomoeda desejada
def select_coin():
    menu()
    opcao = input("Selecione a sua opção: ")
    
    # Retorno de acordo com a seleção do usuário
    if int(opcao) == 1:
        return "BTC"
    elif int(opcao) == 2:
        return "ADA"
    elif int(opcao) == 3:
        return "ETH"
    elif int(opcao) == 4:
        return "LTC"

# Logo
logo()

# Variaveis
list_coin = []
looping = 0

# Pegar a moeda desejada
try:
    crypto_search = select_coin()
except:
    print("Seleção errada!")

while (True):
    # Requisição
    try:
        value = requestMB(crypto_search)

        # Armazenando em listas para fazer uma comparação
        list_coin.append(value)

        # Mostrar resultado para o usuário
        if list_coin[looping] > list_coin[looping - 1]:
            print(f'{crypto_search}: O valor atual é R${value:.2f} -> ' + Fore.GREEN + 'Estável!' + Style.RESET_ALL)
        elif list_coin[looping] == list_coin[looping - 1]:
            print(f'{crypto_search}: O valor atual é R${value:.2f} -> ' + Fore.YELLOW + 'Estável!' + Style.RESET_ALL)
        else:
            print(f'{crypto_search}: O valor atual é R${value:.2f} -> ' + Fore.RED + 'Caindo!' + Style.RESET_ALL)
        print(Fore.CYAN + "=============================================================================" + Style.RESET_ALL)
        looping += 1 # Atualização do looping while para que possa acessar os indices na lista
        time.sleep(1) # Esperar 30 segundos para fazer a requisição novamente
    except:
        print("Nenhuma requisição foi recebida, reinicie o programa!")
        break

