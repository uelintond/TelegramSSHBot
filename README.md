# Bot de Comandos SSH para Servidores Remotos

Este é um bot Telegram desenvolvido em Python que permite executar comandos SSH em servidores remotos acessíveis via SSH. O bot utiliza a biblioteca paramiko para estabelecer conexões SSH seguras e confiáveis.

Recursos Principais:
Execução de Comandos SSH: Com este bot, é possível executar comandos SSH em servidores remotos de forma remota e segura.

## Como Utilizar:

- Configuração:
  Clone este repositório para o seu ambiente local:

```
git clone https://github.com/seuusuario/seurepositorio.git
```

Instale as dependências necessárias usando pip:

```
pip install -r requirements.txt
```

Edite o arquivo main.py para adicionar as informações do seu bot Telegram e do servidor remoto:

# Defina as informações do seu bot Telegram:

## Defina as informações do seu bot

```
TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)
```

## Defina o seu ID de chat

CHAT_ID = 0000000000

Bot para conseguir o seu chat id https://t.me/get_id_bot
Defina as informações do servidor remoto (substitua HOST, PORT, USERNAME, PRIVATE_KEY ou PASSWORD pelos detalhes do seu servidor):

## Defina as informações do servidor remoto

```
HOST = 'IP_DO_SEU_SERVIDOR'
PORT = 22
USERNAME = 'USERNAME_DO_SEU_SERVIDOR'
PRIVATE_KEY = '/caminho/para/sua/chave_privada'  # ou deixe em branco se estiver usando senha
PASSWORD = 'SENHA_DA_CHAVE_PRIVADA'  # Deixe em branco se você não definiu uma senha para a chave privada
```

## Adicionando Novos Comandos:

- Você pode adicionar novos comandos ou ajustar os existentes no arquivo main.py. Cada comando é tratado em uma função separada no código Python.

Para adicionar um novo comando, crie uma nova função de manipulador de mensagem, semelhante às existentes, e registre-a usando @bot.message_handler(commands=['seu_comando']).

### Notas Importantes:

- Certifique-se de ter permissões adequadas para executar os comandos SSH no servidor remoto.
- Mantenha suas informações de autenticação (chave privada ou senha) em segurança.
- Não compartilhe-as publicamente.

Este bot é apenas uma ferramenta para facilitar operações remotas em servidores SSH e deve ser usado com responsabilidade.

### Contribuições e Melhorias:

Se você tiver sugestões, correções ou melhorias para este bot, sinta-se à vontade para contribuir! Basta enviar um pull request com suas alterações.
