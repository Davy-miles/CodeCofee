import os, time, platform, sys, json #adicionar uma forma de baixar todas as depedencias automaticamente e uma interface CLI bem feita e adicionar uma interface grafica sem ser CLI
from openai import OpenAI
from os import getenv

def reset():
    os.execv(sys.executable, [sys.executable] + sys.argv)


def limpar():
    if platform.system() == "Windows":
        os.system("clr")
    
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        print("Infelizmente seu dispositivo não e compativel na nossa lista de dispositivos compativeis...")
        time.sleep(2.0)
        os.system("exit")

limpar()

try:
  if getenv("OPENROUTER_API_KEY") == None:
    Api_key = open("Config.txt")
    recept = Api_key.read()
    Api_key.close()
    os.environ["OPENROUTER_API_KEY"] = recept
except:
    print("infelizmente recebemos algum erro no nosso codigo tente rodar novamente...")
    limpar()

    print("Talvez você possa editar isso nas configurações de api em configurações -> configurações de api -> api personalizada.")#tenho plano de criar um painel de configurações que vai salvar tudo em um arquivo no caso o Config.txt, onde vai fcar os chats e as configurações e tals ate pra mudar o modelo da ia
    reset()

try:
    time.sleep(0.2)
    user = input("Qual seria o seu nome: ")#na versão final vai mudar pois pretendo adicionar um login unico com verificação via e-mail 
    print(f"\n e um prazer conhece-lo {user}\n")
    time.sleep(1.0)
    ianam = input("Qual apelido vc quer dar ao seu chat?: ")
except:
    print("Tivemos um erro no nosso servidor, por favor reinicie")


time.sleep(2.0)
limpar()

client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=getenv("OPENROUTER_API_KEY"),
    )

historico=[{"role": "system", "content": f"Falar apenas Portugues brasil; Seu nome é {ianam}; meu nome é {user}", }]

while True:

# gets API Key from environment variable OPENAI_API_KEY

    quest = input(f"[{user}]>>> ")
    historico.append({"role": "user", "content": quest, })

    completion = client.chat.completions.create(
      model="openrouter/free",
      messages=historico,
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
    )


    historico.append({"role": "assistant", "content": completion.choices[0].message.content,}),
    
    convertxt = json.dumps(historico)
    arquivo = open("historico.json", "w")
    arquivo.write(convertxt)
    arquivo.close()

    print( str(f"\n{ianam}") + "~≳ " + completion.choices[0].message.content + str("\n"))

    

