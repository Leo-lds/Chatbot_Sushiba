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

#### Rodizio
![Chatbot_Sushiba-Rodizio](https://github.com/Leo-lds/Chatbot_Sushiba/assets/169949808/4d91a51a-2ae7-4f9b-a4d0-ae0a200b1e77)    

#### Pedidos

![Chatbot_Sushiba-Atendente](https://github.com/Leo-lds/Chatbot_Sushiba/blob/main/Assets/Chatbot_Sushiba-Pedido.gif)

#### Atendimento
![Chatbot_Sushiba-Atendente](https://github.com/Leo-lds/Chatbot_Sushiba/assets/169949808/0aea9645-855d-4f4f-9a9e-00405a21f4cf)

## Contato
- **Email:** leoldsgn@gmail.com
- **LinkedIn:** https://linkedin.com/in/leoldsgn

---
Obrigado por conferir este projeto! Se você gostou, não se esqueça de dar uma estrela no repositório.
