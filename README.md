# Chatbot Sushiba

## Descrição
Este projeto fictício foi inspirado no evento Imersão IA da Alura. A ideia inicial era criar um chatbot para pedidos e informações sobre o restaurante. Mas percebi que seria útil também apresentar o catálogo aos clientes. Vamos combinar, se você tem um catálogo impresso, seria demorado digitar item por item, né?
Então, adaptei o modelo Gemini para ser um chat que interpreta imagens e responde às perguntas dos clientes. Assim, juntei o útil ao agradável.

## Funcionalidades
- **Interpretação de Imagens:** Análise e extração de informações de imagens de catálogos físicos. ( A imagem precisa ter uma boa qualidade e textos legiveis! Quanto melhor a organização dos itens pelo catalogo, melhor para a IA interpretar.)
- **Adaptação Digital:** Conversão das informações extraídas para um formato digital.
- **Resposta a Dúvidas:** Respostas automáticas a perguntas com base nas informações do catálogo e informações dadas ao bot através do treinamento dele.
- **Pedidos:** Funcionalidade de agendamento de pedidos diretamente pelo chatbot, o chat pergunta se deseja retirar o pedido ou receber em casa.
- **Informações sobre Rodízio:** Fornecimento de detalhes sobre o sistema de rodízio.

## Tecnologias Utilizadas
- **Google Generative AI:** Utilização do SDK `google-generativeai` para processamento de linguagem natural. (Gemini)
- **PIL (Python Imaging Library):** Manipulação e análise de imagens.
- **Google Colab:** Ambiente para desenvolvimento e execução do código.

## Configuração e Uso

### Pré-requisitos
- Python 3.x
- Conta no Google Cloud com a API key configurada

### Passos para Configuração
1. **Clone o Repositório:**
    ```bash
    git clone https://github.com/seu-usuario/Chatbot_Sushiba.git
    ```
2. **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Execute o Notebook no Google Colab:**
    Abra o arquivo `Chatbot_Sushiba.ipynb` no Google Colab:
    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seu-usuario/Chatbot_Sushiba/blob/main/Chatbot_Sushiba.ipynb)

4. **Configure a API Key:**
    Salve sua chave de API no Google Colab:
    ```python
    GOOGLE_API_KEY = 'sua-api-key-aqui'
    ```
### Exemplos de utilização do Chatbot

<details>
<summary>Chat escolhendo a opção de rodizio:</summary>
  
  Digite uma Mensagem: Ola  
  
  Resposta: Olá, bem-vind@ ao Sushiba, eu sou o Sushito e vou realizar seu atendimento hoje! Para começar o atendimento, poderia me informar seu nome? 😊  
  
  Digite uma Mensagem: Leo  
  
  Resposta: Certo, Léo! Por favor, selecione uma opção abaixo:
  
  1. Rodízio
  2. Pedido via chat
  3. Falar com atendente. 
   
  
  Digite uma Mensagem: 1
  
  Resposta: Léo,  ótima escolha! 😋  
  
  O Rodízio do Sushiba funciona da seguinte forma:
  
  **Almoço:** 
  - De Segunda a Quinta > R$89,90 
  - De Sexta a domingo > R$ 109,90 
  
  **Janta:**
  - De Segunda a Quinta > R$109,90
  - De Sexta a domingo > R$ 129,90
  
  Você gostaria de:
  
  1. Ver o cardápio do Rodízio? 
  2. Voltar ao menu principal? 
   
  
  Digite uma Mensagem: 1
  
  Resposta: Léo, aqui está o cardápio do nosso delicioso Rodízio:
  
  **Uramaki**
  - Filadélfia: Salmão, Cream cheese, Cebolinha e Pepino
  - Skin: Salmão skin, Cream cheese e Cebolinha
  - Kani-Phila: Kani, Cream cheese, Cebolinha e Pepino
  - Cazadeira: Salmão, Cream cheese, Cebolinha e Abacate
  
  **Niguiri**
  - Salmão: Arroz com Salmão
  - Skin: Arroz com Salmão grelhado
  - Kani: Arroz com Kani
  - Acelga Maki: Arroz envolto na acelga, Cream cheese e Cebolinha
  
  **Sashimi**
  - Tilápia: Tilápia
  - Kani: Kani
  - Salmão: Salmão
  
  **Temaki**
  - Filadélfia: Salmão, Cream cheese, Cebolinha e Pepino
  - Skin-Filadélfia: Salmão skin, Cream cheese, Cebolinha e Pepino
  - Salmão: Salmão
  - Califórnia: Kani, Manga e Pepino
  
  Para o Rodízio, basta comparecer nos dias de funcionamento. 😊
  
  Ficou alguma dúvida sobre o Rodízio, Léo? 
  
  Se não tiver mais dúvidas, poderia me dar um feedback sobre o atendimento?  (Ruim/Bom/Ótimo) 
   
  
  Digite uma Mensagem: Otimo
  
  Resposta: Que ótimo saber que você está satisfeito com o atendimento, Léo! 😄  
  
  Aproveite o Rodízio do Sushiba e volte sempre!  🍣  
  
  Até a próxima! 
   
  Digite uma Mensagem: sair
</details>

<details>
<summary>Chat escolhendo a opção de pedido online:</summary>
Digite uma Mensagem: Ola
  
Resposta: Olá, bem-vind@ ao Sushiba, eu sou o Sushito e vou realizar seu atendimento hoje! Para começar o atendimento, poderia me informar seu nome? 😊 
 

Digite uma Mensagem: Heitor

Resposta: Certo, Heitor! Por favor, selecione uma opção abaixo:

1. Rodízio
2. Pedido via chat
3. Falar com atendente. 
 

Digite uma Mensagem: 2

Resposta: Ok, Heitor!  Aqui está o nosso menu de itens:

1. Uramaki
2. Niguiri
3. Temaki
4. Sashimi

Qual opção você gostaria de ver? 😊 
 

Digite uma Mensagem: 1

Resposta: Ótimo! Aqui estão as opções de Uramaki:

* Califórnia: R$ 2,00
* Skin: R$ 2,00
* Kani-Fila: R$ 3,00
* Cazadeira: R$ 4,00

Qual você gostaria de pedir? 😊 
 

Digite uma Mensagem: quero 4 california

Resposta: Ok, Heitor!  4 Califórnia, anotado!  Você gostaria de pedir mais alguma coisa? 😊 
 

Digite uma Mensagem: sim

Resposta: Ótimo!  O que mais você gostaria de pedir? 😊 
 

Digite uma Mensagem: me mostra o menu novamente

Resposta: Claro, Heitor! Aqui está o nosso menu de itens novamente:

1. Uramaki
2. Niguiri
3. Temaki
4. Sashimi

Qual opção você gostaria de ver? 😊 
 

Digite uma Mensagem: 3

Resposta: Ok, Heitor! Aqui estão as opções de Temaki:

* Filadélfia: R$ 20,00
* Skin-Filadélfia: R$ 23,00
* Salmão: R$ 25,00
* Califórnia: R$ 22,00

Qual você gostaria de pedir? 😊 
 

Digite uma Mensagem: vou querer 1 de Salmão e 1 de California

Resposta: Perfeito, Heitor!  Então são 4 Califórnia, 1 Salmão e 1 Califórnia de Temaki, certo? 😊 

Seu pedido total ficou em R$ 16,00 (4 Califórnia x R$ 2,00) + R$ 25,00 (1 Salmão) + R$ 22,00 (1 Califórnia) = R$ 63,00. 

Gostaria de confirmar seu pedido? 😊 
 

Digite uma Mensagem: sim

Resposta: Ótimo, Heitor! Seu pedido está confirmado:

* 4 Uramaki Califórnia
* 1 Temaki Salmão
* 1 Temaki Califórnia

Total: R$ 63,00

Agora, qual a forma de pagamento que você prefere? Cartão, Pix ou dinheiro?  E você prefere retirar no local (Rua do Sushi, 123) ou deseja entrega? 😊 
 

Digite uma Mensagem: Eu vou pagar via Cartão e vou retirar no local

Resposta: Perfeito, Heitor!  Seu pedido está confirmado para retirada no local, na Rua do Sushi, 123, com pagamento via cartão. 😊

Seu pedido estará pronto em breve!  Aproveite seu jantar e  avalie nosso atendimento, por favor!  Ruim/Bom/Ótimo? 😊 
 

Digite uma Mensagem: Otimo

Resposta: Que ótimo saber que você está satisfeito, Heitor! 😄  Agradecemos a preferência e esperamos te ver novamente em breve!  😊 
 
Digite uma Mensagem: sair
</details>

<details>
<summary>Chat escolhendo a opção de falar com atendente:</summary>
Digite uma Mensagem: Ola
  
Resposta: Olá, bem-vind@ ao Sushiba, eu sou o Sushito e vou realizar seu atendimento hoje! Para começar o atendimento, poderia me informar seu nome? 😊 
 

Digite uma Mensagem: Yanca

Resposta: Certo Yanca! Por favor, selecione uma opção abaixo:

1. Rodizio
2. Pedido via chat
3. Falar com atendente. 
 

Digite uma Mensagem: 3

Resposta: Em breve um atendente irá continuar o seu atendimento. 
 

Digite uma Mensagem: sair
</details>


## Contato
- **Email:** leoldsgn@gmail.com
- **LinkedIn:** https://linkedin.com/in/leoldsgn

---
Obrigado por conferir este projeto! Se você gostou, não se esqueça de dar uma estrela no repositório.
