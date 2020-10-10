import requests
import time
import json
import os


class TelegramBot:
    def __init__(self):
        token = '' # coloca seu token ai
        self.url_base = f'https://api.telegram.org/bot{token}/'

    def Iniciar(self):
        update_id = None
        while True:
            atualizacao = self.obter_novas_mensagens(update_id)
            dados = atualizacao["result"]
            if dados:
                for dado in dados:
                    update_id = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    eh_primeira_mensagem = int(
                        dado["message"]["message_id"]) == 1
                    resposta = self.criar_resposta(mensagem,
                                                   eh_primeira_mensagem)
                    self.responder(resposta, chat_id)

    # Perguntas
    def obter_novas_mensagens(self, update_id):
        link_requisicao = f'{self.url_base}getUpdates?timeout=100'
        if update_id:
            link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)

    # Resposta
    def criar_resposta(self, mensagem, eh_primeira_mensagem):
        if eh_primeira_mensagem == True or mensagem in ('foda', 'foda'):
            return f'''Olá amigo me diga Qual você prefere:{os.linesep}1 - Moobloom{os.linesep}2 - Glow Squid {os.linesep}3 - Iceologer'''
        if mensagem == '1':
            return f'''Parabens amigo, seu QI e ALTO{os.linesep}escolher decisão?(s/n)
            '''
        elif mensagem == '2':
            return f'''Parabens amigo, seu Q1 e bem BAIXO{os.linesep}escolher decisão?(s/n)
            '''
        elif mensagem == '3':
            return f'''Parabens amigo, seu QI e BAIXO{os.linesep}escolher decisão?(s/n)'''

        elif mensagem.lower() in ('s', 'sim'):
            return ''' QI confirmado! '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' QI não confirmado! '''
        else:
            return 'Olá vamos testar seu QI digite "foda"'

    # Responder
    def responder(self, resposta, chat_id):
        link_requisicao = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(link_requisicao)


bot = TelegramBot()
bot.Iniciar()
