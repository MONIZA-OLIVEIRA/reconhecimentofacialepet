# <p align="center"> VISION - Reconhecimento de emoções e raças de cães.



## ⚙️ Versão<a name="versao"></a>

Atualmente está disponível a **Versão 1.0** do presente projeto, disponibilizada em Outubro/2024.

## 📝 Descrição do Projeto:

Este projeto visa receber imagens dos usuários e a partir dela analisar as emoções detectadas. Também verificará se há animais de estimação na imagem e, caso afirmativo, identificará a raça, retornando dicas sobre o animal.

## 🎯 Especificações do Projeto:

O projeto é dividido em duas etapas principais:

##### Parte 1 - Detecção de emoções:

- O projeto começa com a criação de uma API usando o framework Serverless que permite ao usuário enviar uma imagem.
- Essa imagem é verificada pelo rekoginition que analisa os rotulos encontrados.
- Após verificação do rekoginition é retornado a emoção encontrada na imagem com maior confiabilidade.
- Caso tenha mais de uma face ele analisa e retorna os resultados separadamente.

##### Parte 2 - Emoções + Pet:

- A segunda parte envolve a análise da imagem e detectar as emoções e se existe um pet na imagem utilizando rekoginition.
- Caso exista um pet verifica a raça do pet.
- Se identificar a raça gerar um texto via bedrock com dicas relacionadas aquela raça.
- As seguintes informações são obrigatórias: Nível de energia e necessidades de exercícios, Temperamento e Comportamento, Cuidados e Necessidades, Problemas de Saúde Comuns.
- Após verificação do rekoginition é retornado a emoção encontrada na imagem com maior confiabilidade.
- Caso tenha mais de uma face ele analisa e retorna os resultados separadamente.
- Ao final é retornado as faces e as dicas para o pet.

## ⚙️ Tecnologias Utilizadas:
<p align="center">
  <a href="https://go-skill-icons.vercel.app/">
    <img src="https://go-skill-icons.vercel.app/api/icons?i=vscode,python,aws,git,github,postman" />
  </a>
</p>



 - **VSCode**:IDE escolhida para escrever, editar e depurar o código do projeto.
 - **Python**: Linguagem de programação utilizada.
 - **Serverless/Lambda**: O projeto foi desenvolvido com o framework Serverless. O Lambda permite rodar o código sem a necessidade de gerenciar servidores.
 - **AWS Cloud**: A AWS fornece os serviços de computação, armazenamento, processamento de imagem, integrando-os em uma solução completa que facilita a implementação, com escalabilidade e sem a necessidade de gerenciar infraestrutura física.
 - **AWS Rekoginition**: Para analisar as imagens e detectar rostos e pets encontrados nas imagens enviadas.
 - **AWS Bedrock**: Para implementação de IA e geração de texto relacionado a raça do pet.
 - **Amazon S3**: Utilizado para armazenar as imagens que serão analisadas pela aplicação.
 - **AWS IAM (Identity and Access Management)**: Gerencia as credenciais e permissões de acesso aos serviços AWS utilizados, garantindo que os componentes da aplicação possam interagir de forma segura.
 - **Git e Github**: Para versionamento da aplicação.
 - **Postman**: Para testar as rotas e funcionamento da aplicação.

## 🛠 Como Abrir e Executar Esse Projeto:

**1. Clone o repositório**:

```
git clone --branch grupo-1 https://github.com/Compass-pb-aws-2024-JUNHO/sprint-8-pb-aws-junho.git
```
**2. Abra o repositório clonado em uma IDE de sua escolha, neste projeto a IDE utilizada foi o Visual Studio Code (VSCode)**:

**3. Recomendamos o uso de um ambiente virtual para que não aja conflito de versões**:
```
python -m venv venv

.\venv\Scripts\activate

```
**4. Para saber se o acesso ao ambiente virtual foi bem sucedido, o prefixo venv deverá estar presente no caminho do projeto do seu terminal, exemplo**:
```
(venv) PS C:\Users\usuário\sprint-8-pb-aws-junho>
```
**5. No terminal, instale o framework Serverless através do comando**:
```
npm install -g serverless
```
**6. Após a instalação do framework do projeto, configure suas credenciais AWS**:

##### Opção 1 - Via AWS CLI (Opção que recomendamos):

Instale a AWS CLI e configure suas credenciais com:

```
aws configure
```
Você será solicitado a fornecer:

- AWS Access Key ID: Sua chave de acesso.<br>
- AWS Secret Access Key: Sua chave secreta.<br>
- Default region name: Por exemplo, us-east-1 (Escolha a região que você está utilizando).<br>
- Default output format: Pode ser json.

**7. Instale as dependências**:
```
npm install
pip install -r requirements.txt:
```

**8. Adicione as Variáveis de Ambiente**:

Crie um arquivo `.env` no diretório raiz com o ID do modelo do Amazon Bedrock, dessa maneira:
- `MODEL_ID`

**9. Faça o deploy da aplicação no Serverless Framework**:

Agora que tudo está configurado, faça o deploy da aplicação para a AWS:

```
task deploy
```

##### Esse comando irá:

- Configurar o API Gateway.<br>
- Configurar outras integrações AWS necessárias.


**10. Verifique os endpoints gerados. Esses endpoints são URLs para as funções Lambda. Use-os para fazer requisições à API, seja via navegador, Postman, ou outra ferramenta**:

endpoints:
```
  Deploying vision to stage dev (us-east-1)

Service deployed to stack vision-dev (85s)

endpoints:
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v1
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v2
  POST - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v1/vision
  POST - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v2/vision
functions:
  health: vision-dev-health (25 MB)
  v1Description: vision-dev-v1Description (25 MB)
  v2Description: vision-dev-v2Description (25 MB)
  detectEmotion: vision-dev-detectEmotion (25 MB)
  detectPetAndEmotion: vision-dev-detectPetAndEmotion (25 MB)
```

**11. Teste a API localmente**:

```
serverless invoke local --function v1Description
```
Usando serverless-offline:
```
task run
```
Usando serverless-offline e nodemon com reload automático:
```
npx nodemon 
```
##  Testando o VISION :

1. **Faça o upload da imagem para a bucket**:

    Selecione a imagem e faça seu envio para a bucket configurada.<br>

2. **Execute o deploy da aplicação**:

    Execute o deploy da aplicação, após validar o deploy acesse via POSTMAN.<br>

3. **Digite as informações da imagem**:

    Digite as informações da bucket e o nome da imagem salva.<br>

Exemplo:
```json
{
  "bucket": "myphotosmo",
  "imageName": "pugs.jpg"
}
```
4. **Possíveis retornos após a análise da imagem**:

Nulo:
```json
{
    "url_to_image": "https://myphotosmo.s3.amazonaws.com/2dogs.jpg",
    "created_image": "14-10-2024 09:36:19",
    "faces": [
        {
            "position": {
                "Height": null,
                "Left": null,
                "Top": null,
                "Width": null
            },
            "classified_emotion": null,
            "classified_emotion_confidence": null
        }
    ]
}
```
Emoção:
```json
{
    "url_to_image": "https://myphotosmo.s3.amazonaws.com/triste.jpg",
    "created_image": "14-10-2024 08:54:35",
    "faces": [
        {
            "position": {
                "Height": 0.4149770438671112,
                "Left": 0.4800688624382019,
                "Top": 0.24941901862621307,
                "Width": 0.1959000676870346
            },
            "classified_emotion": "SAD",
            "classified_emotion_confidence": 93.24629974365234
        }
    ]
}
```
Pet:
```json
{
    "url_to_image": "https://myphotosmo.s3.amazonaws.com/cachorro.jpg",
    "created_image": "14-10-2024 09:36:20",
    "pets": [
        {
            "labels": [
                {
                    "Confidence": 99.0054931640625,
                    "Name": "Animal"
                },
                {
                    "Confidence": 99.0054931640625,
                    "Name": "Dog"
                },
                {
                    "Confidence": 99.0054931640625,
                    "Name": "Pet"
                },
                {
                    "Confidence": 92.6964111328125,
                    "Name": "Hound"
                }
            ],
            "Dicas": "1. Nível de energia: A raça é ativa e gosta de atividades físicas, como passeios, corridas e jogos. Também gosta de atividades mentais, como treinamentos e atividades cognitivas. 2. Necessidades diárias de exercício físico: Recomenda-se pelo menos duas caminhadas diárias de 30 minutos cada, além de jogos e brincadeiras.
            3. Temperamento: É uma raça amigável com crianças e outros animais, mas pode ser possessiva com alimentos. Recomenda-se socialização desde cedo.
            4. Necessidades especiais de cuidados: Recomenda-se banho regular, escovação dos dentes e cuidados com as unhas. Também é necessário fornecer comida de qualidade e suplementos para a pele e o pelo.
            5. Problemas de saúde comuns: São raças propensas a problemas de saúde como obesidade, problemas oculares e problemas de coluna. Recomenda-se avaliações regulares com o veterinário."
        }
    ]
}
```
Emoção + pet:
```json

{
    "url_to_image": "https://myphotosmo.s3.amazonaws.com/pessoa-pet2.jpg",
    "created_image": "14-10-2024 09:45:22",
    "faces": [
        {
            "position": {
                "Height": 0.23378419876098633,
                "Left": 0.3006735146045685,
                "Top": 0.15228010714054108,
                "Width": 0.1119609847664833
            },
            "classified_emotion": "HAPPY",
            "classified_emotion_confidence": 100.0
        }
    ],
    "pets": [
        {
            "labels": [
                {
                    "Confidence": 98.90979766845703,
                    "Name": "Animal"
                },
                {
                    "Confidence": 98.90979766845703,
                    "Name": "Dog"
                },
                {
                    "Confidence": 98.90979766845703,
                    "Name": "Pet"
                },
                {
                    "Confidence": 96.54975891113281,
                    "Name": "Golden Retriever"
                }
            ],
            "Dicas": "1. Nível de energia: A raça é ativa e gosta de atividades físicas, como passeios, corridas e jogos. Também gosta de atividades mentais, como treinamentos e atividades cognitivas. 2. Necessidades diárias de exercício físico: Recomenda-se pelo menos duas caminhadas diárias de 30 minutos cada, além de jogos e brincadeiras.
            3. Temperamento: É uma raça amigável com crianças e outros animais, mas pode ser possessiva com alimentos. Recomenda-se socialização desde cedo.
            4. Necessidades especiais de cuidados: Recomenda-se banho regular, escovação dos dentes e cuidados com as unhas. Também é necessário fornecer comida de qualidade e suplementos para a pele e o pelo.
            5. Problemas de saúde comuns: São raças propensas a problemas de saúde como obesidade, problemas oculares e problemas de coluna. Recomenda-se avaliações regulares com o veterinário."
        }
    ]
}
```

## 📂  Estrutura do Projeto:

### Estrutura de Diretórios:

A estrutura do projeto é organizada da seguinte maneira:
```
sprints-8-pb-aws-junho/                             # Diretório principal do projeto Sprint 8 PB AWS - Junho
│
├── assets/                                         # Contém arquivos de mídia e recursos visuais do projeto
│   ├── arquitetura-base.jpeg                       # Imagem da arquitetura base do sistema
│
├── development/                                    # Diretório de desenvolvimento com collectoins e scripts
│   ├── collections/                                # Contém collectoins postman
│         └── sprint-8-pb-aws-junho.json            # Coleção Postman específica da sprint
│   ├── taskpy/                                     # Scripts automatizados para tarefas relacionadas ao desenvolvimento
│
├── visao-computacional/                            # Módulo de visão computacional do projeto
│     ├── api/                                      # Contém todas as versões da API
│         ├── v1/                                   # API versão 1
│             ├── handlers/                         # Handlers para lidar com requisições da API v1
│         ├── v2/                                   # API versão 2
│             ├── handlers/                         # Handlers para lidar com requisições da API v2
│
│     ├── aplication/                               # Lógica de aplicação para o módulo de visão computacional
│         ├── contrib/                              # Contém código reaproveitado no projeto inteiro e exceções customizadas
|         ├── core/                                 # Configurações do projeto e variáveis de ambiente
│
│     ├── infrastructure/                           # Arquivos relacionados à infraestrutura do sistema
│         ├── aws/                                  # Código dos serviços da AWS utilizados
│         ├── schemas/                              # Schemas dos dados de entrada dos endpoints
│
├── .gitignore                                      # Arquivo para ignorar arquivos e diretórios no controle de versão
├── .pre-commit-config.yaml                         # Configurações do pre-commit para validações automáticas antes dos commits
├── pyproject.toml                                  # Arquivo de configuração de dependências e ferramentas para o projeto Python
├── nodemon.json                                    # Configurações do Nodemon para monitoramento e reinício automático do servidor
├── package.json                                    # Dependências do projeto e scripts do Node.js
├── requirements.txt                                # Dependências Python necessárias para o projeto
└── README.md                                       # Arquivo de instruções e documentação do projeto
```
## 😵‍💫 Dificuldades Encontradas:

- **Labels do rekoginition**: Dificuldades em entender e ajustar as labels de raças para retornar a resposta pedida de forma correta.

## Licença:
Este projeto está licenciado sob a [MIT License](LICENSE).



## 🌐 Equipe:
🧑 💻 Este projeto foi desenvolvido por:</br>
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/97261564?v=4" width=115><br><sub>Gustavo Felipe</sub>](https://github.com/gusttavofelipe) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/167718668?v=4" width=115><br><sub>Jean Carlos</sub>](https://github.com/JeanPTBR) |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/25685390?v=4" width=115><br><sub>John Sousa</sub>](https://github.com/johnSousa23)  |  [<img loading="lazy" src="https://avatars.githubusercontent.com/u/173844663?v=4" width=115><br><sub>Moniza Oliveira</sub>](https://github.com/MONIZA-OLIVEIRA) |
| :---: | :---: | :---: | :---: |
