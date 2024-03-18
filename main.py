import paramiko
import telebot

# Defina as informações do seu bot
TOKEN = 'SEU_TOKEN_AQUI'
bot = telebot.TeleBot(TOKEN)

# O chat id é importante para garantir que apenas você possa executar os comandos.
CHAT_ID = 0000000000  # Defina o seu ID de chat

HOST = 'IP_DO_SEU_SERVIDOR'  # Defina as informações do servidor Linode
PORT = 22
USERNAME = 'USERNAME_DO_SEU_SERVIDOR'
PRIVATE_KEY = '/caminho/para/sua/chave_privada' # Exemplo ppk: /root/manager/id_rsa.ppk
PASSWORD = 'SENHA_DA_CHAVE_PRIVADA' # Deixe em branco se você não definiu uma senha para a chave privada

# Função para lidar com o comando SSH e reiniciar o servidor
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id == CHAT_ID:
        bot.reply_to(
            message, "O que você deseja fazer? \n\n /restart_server para reiniciar o servidor Linode\n /restart_check para reiniciar o serviço GRD Check.")
    else:
        bot.reply_to(
            message, "Acesso negado. Você não tem permissão para executar este comando.")

# Função para lidar com o comando SSH e reiniciar o servidor
@bot.message_handler(commands=['restart_server'])
def restart_server(message):
    try:
        # Verifica se a mensagem foi enviada por você
        if message.chat.id == CHAT_ID:
            # Conecte-se ao servidor Linode com a chave privada e senha
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(HOST, PORT, USERNAME,
                        key_filename=PRIVATE_KEY, password=PASSWORD)

            # Execute o comando SSH para reiniciar o serviço
            command = 'sudo systemctl reboot'
            stdin, stdout, stderr = ssh.exec_command(command)           
            output = stdout.read().decode()  # Obtenha a saída do comando
            ssh.close() # Fecha a conexão SSH

            # Verifica se a saída está vazia
            if not output.strip():
                bot.reply_to(
                    message, "O comando foi executado com sucesso. O servidor foi reiniciado.")
            else:
                bot.reply_to(message, output)
        else:
            bot.reply_to(
                message, "Você não tem permissão para executar este comando.")
    except Exception as e:
        bot.reply_to(
            message, f"Ocorreu um erro ao executar o comando SSH: {str(e)}")

# Função para lidar com o comando SSH e reiniciar o serviço
@bot.message_handler(commands=['restart_check'])
def restart_check(message):
    try:
        # Verifica se a mensagem foi enviada por você
        if message.chat.id == CHAT_ID:
            # Conecta ao servidor Linode com a chave privada e senha
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(HOST, PORT, USERNAME,
                        key_filename=PRIVATE_KEY, password=PASSWORD)

            # Executa o comando SSH para reiniciar o serviço
            command = 'sudo systemctl restart grdcheck.service'
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode() # Obtenha a saída do comando
            ssh.close() # Feche a conexão SSH

            # Verifica se a saída está vazia
            if not output.strip():
                bot.reply_to(
                    message, "O comando foi executado com sucesso.")
            else:
                bot.reply_to(message, output)
        else:
            bot.reply_to(
                message, "Você não tem permissão para executar este comando.")
    except Exception as e:
        bot.reply_to(
            message, f"Ocorreu um erro ao executar o comando SSH: {str(e)}")
        
bot.polling()
