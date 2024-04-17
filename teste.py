from scapy.all import *

def verificar_portas_abertas(ip_alvo, portas_alvo):
    portas_abertas = []
    for porta in portas_alvo:
        # Criação do pacote TCP
        pacote_tcp = IP(dst=ip_alvo)/TCP(dport=porta, flags="S")
        # Envio do pacote e recebimento da resposta
        resposta = sr1(pacote_tcp, timeout=2, verbose=False)
        # Verificação se houve resposta
        if resposta:
            print(f"A porta {porta} está aberta.")
            portas_abertas.append(porta)
    return portas_abertas

def explorar_portas_abertas(ip_alvo, portas_abertas, comando):
    for porta in portas_abertas:
        # Explorar a porta apenas se estiver aberta
        print(f"Explorando a porta {porta}...")
        # Aqui você pode adicionar o código para explorar a porta, como injetar comandos
        # Vou manter apenas a impressão como exemplo
        print(f"Comando injetado na porta {porta}: {comando}")

# Exemplo de uso
if __name__ == "__main__":
    # Defina o IP do alvo, as portas alvo e o comando a ser injetado
    ip_alvo = "99.99.99.254"
    portas_alvo = [3306, 3389, 21, 22, 80]  # Portas a serem verificadas
    comando = "ping 99.99.99.254"  # Comando a ser injetado nas portas abertas
    # Verificar quais portas estão abertas
    portas_abertas = verificar_portas_abertas(ip_alvo, portas_alvo)
    # Explorar apenas as portas abertas
    explorar_portas_abertas(ip_alvo, portas_abertas, comando)
