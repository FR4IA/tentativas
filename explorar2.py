from scapy.all import *

def explorar_porta_tcp(ip_alvo, porta_alvo):
    # Criação do pacote TCP
    pacote_tcp = IP(dst=ip_alvo)/TCP(dport=porta_alvo, flags="S")
    # Envio do pacote e recebimento da resposta
    resposta = sr1(pacote_tcp, timeout=2, verbose=False)
    # Verificação se houve resposta
    if resposta:
        print(f"A porta {porta_alvo} está aberta.")
    else:
        print(f"A porta {porta_alvo} está fechada.")

# Exemplo de uso
if __name__ == "__main__":
    # Defina o IP do alvo e a porta alvo
    ip_alvo = "99.99.99.254"
    porta_alvo = 3389
    # Chamando a função para explorar a porta TCP
    explorar_porta_tcp(ip_alvo, porta_alvo)
