import os, ollama, time

os.system("clear")

user = input("Qual seria o seu nome: ")
print(f"\n e um prazer conhece-lo {user}\n")
time.sleep(1.0)
ianam = input("Qual nome vc quer dar a sua IA?: ")

time.sleep(2.0)
os.system("clear")


while True:
    #caixa de pergunta ou area das variaveis
    quest = input(f"{user}|>>> ")
    
    #codigo do funcionamento da ia
    resposta_completa = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': quest}])

    texto_da_ia = resposta_completa['message']['content']

    #mensagem ou impressões
    print(f"\n" + str(ianam) + "]--> " +texto_da_ia + "\n")