import socket
from emoji import demojize
import re


server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'datatestdummy' #username goes here
token = 'oauth:400o7hwm2fen32pwjigjpfi0cmixue' #oauth token goes here (include the oauth:)
channel = '#ninja'
# chat = 'playhearthstone_chat.log'

def init_socket():
    sock = socket.socket()

    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    resp = sock.recv(2048).decode('utf-8')
    resp = sock.recv(2048).decode('utf-8')
def get_chat():
    
    pass

if __name__ == '__main__':
    while True:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        
        elif len(resp) > 0:
    #         logging.info(demojize(resp))
            msg = demojize(resp)
            msg = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', msg)
            if(msg):
                _, _, message = msg.groups()
                print(message)