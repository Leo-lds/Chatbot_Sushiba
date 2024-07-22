# Importanto as Bibliotecas e utilizando a API KEY do Gemini (Você consegue pegar a API nesse site: https://aistudio.google.com/app/apikey)

import google.generativeai as genai
import PIL.Image
import urllib.request
import os
from dotenv import load_dotenv
from sys_instruction import sys_instruction

#Coloque sua key.
load_dotenv()
key = os.getenv("api_key")
genai.configure(api_key=key)

#Dentro do Gemini podemos indicar a influencia das variaveis entre texto, uma das opções é a variação de temperatura (proximo ao 0 é menos criativa e mais proxima ao 1 é mais criativa)
generation_config = {
  "candidate_count": 1,
  "temperature": 0.2
}

#Já aqui, definimos as os parametros de segurança.
safety_settings={
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
    }

#Codigo responsavel por salvar o catalogo da url (obs a imagem referente é ilustrativa e foi retirada do google, porem você pode substituir com qualquer catalogo que tenha. obs:basta substituir o link do imgur.)
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(
  'https://i.imgur.com/FII56mD.png',"Assets/catalogo.jpeg")
image = PIL.Image.open("Assets/catalogo.jpeg")

#Esse codigo abaixo ira ler o catalogo do restaurante e informar os itens e ingredientes de cada um e ira guardar o texto gerado em uma variavel para utilizar depois.
model_2 = genai.GenerativeModel("gemini-1.5-pro")
response2 = model_2.generate_content(
    ["Descrição: Cite 4 Uramaki, 3 Niguiri (salmão, skin, Kani), Sashimi(tilapia, kani e salmao) e Temaki(Filadélfia, skin-Filadélfia, salmão, California), apresente os ingredientes de todos os itens (Não incluir Yakisoba e Peixe Branco e todos os itens da aba Sobremesa) ", image], stream=True)
response2.resolve()
catalogo = response2.text

model = genai.GenerativeModel(model_name='gemini-1.5-flash',
                                  system_instruction=sys_instruction(catalogo),
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)

#Com o chatbot configurado, vamos iniciar o chat
chat = model.start_chat(history=[])
prompt = input('\n\033[33mDigite uma Mensagem: \033[m').lower()
while prompt != "sair":
  response = chat.send_message(prompt)
  print("\nResposta:", response.text)
  prompt = input('\033[33mDigite uma Mensagem: \033[m').lower()