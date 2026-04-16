import os, time, platform
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
    user = input("Qual seria o seu nome: ")
    print(f"\n e um prazer conhece-lo {user}\n")
    time.sleep(1.0)
    ianam = input("Qual nome vc quer dar a sua IA?: ")
except:
    print("Tivemos um erro no nosso servidor, por favor reinicie")


time.sleep(2.0)
limpar()

#memoria da IA
historico=[{"role": "system", "content": "Falar apenas Portugues brasil"}]

while True:

# gets API Key from environment variable OPENAI_API_KEY

    quest = input(f"[{user}]>>> ")
    historico.append({"role": "user", "content": quest})

    client = OpenAI(
      base_url="https://openrouter.ai/api/v1",
      api_key=getenv("OPENROUTER_API_KEY"),
      messages=historico,
    )
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
    messages=[
       {
         "role": "user",
         "content": quest,
       },
      ],
    ) 
    print(str(ianam) + "~≳ " + completion.choices[0].message.content)

