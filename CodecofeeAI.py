import os, time, platform #adicionar uma forma de baixar todas as depedencias automaticamente e uma interface CLI bem feita
from openai import OpenAI
from os import getenv

def limpar():
    if platform.system() == "Windows":
        os.system("clr")
    
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        print("Infelizmente seu dispositivo não e compativel na nossa lista de dispositivos compativeis...")
        time.sleep(4.0)
        os.system("exit")

limpar()

try:
  if getenv("OPENROUTER_API_KEY") == None:
    Api_key = input("Nos informe a sua key, pode ser achada no openrouter: ")
    os.environ["OPENROUTER_API_KEY"] = Api_key
except:
    print("infelizmente recebemos algum erro no nosso codigo tente rodar novamente...")

try:
    time.sleep(0.2)
    user = input("Qual seria o seu nome: ")#falta adicionar o sistema de pular o nomeamento, o quê na versão final vai mudar pois pretendo adicionar um login unico com verificação via e-mail
    print(f"\n e um prazer conhece-lo {user}\n")
    time.sleep(1.0)
    ianam = input("Qual nome vc quer dar a sua IA?: ")
except:
    print("Tivemos um erro no nosso servidor, por favor reinicie")


time.sleep(2.0)
limpar()

client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=getenv("OPENROUTER_API_KEY"),#adicionar uma forma de baixar a key sozinha ou executar
    )

#memoria da IA
historico=[{"role": "system", "content": "Falar apenas Portugues brasil", }]#melhorar esse sistem ainda esta muinto basico

while True:

# gets API Key from environment variable OPENAI_API_KEY

    quest = input(f"[{user}]>>> ")
    historico.append({"role": "user", "content": quest})
     
    completion = client.chat.completions.create(
      model="nvidia/nemotron-3-super-120b-a12b:free",
      extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    # pass extra_body to access OpenRouter-only arguments.
    # extra_body={
      # "models": [
      #   "${Model.GPT_4_Omni}",
      #   "${Model.Mixtral_8x_22B_Instruct}"
      # ]
     # },
     
    messages=historico,

    ) 
   

    print(str(ianam) + "~≳ " + completion.choices[0].message.content)

