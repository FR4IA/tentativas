from scapy.all import *

def explorar_vulnerabilidade(ip_alvo, porta_alvo, exploit):
    # Criação do pacote com o exploit específico
    pacote = IP(dst=ip_alvo)/TCP(dport=porta_alvo)/exploit
    # Envio do pacote e captura da resposta
    resposta = sr1(pacote, timeout=5, verbose=0)
    # Verifica se houve resposta
    if resposta:
        print("Vulnerabilidade explorada com sucesso!")
        # Aqui você pode adicionar ações adicionais após a exploração bem-sucedida
    else:
        print("Não foi possível explorar a vulnerabilidade.")

# Exemplo de uso
if __name__ == "__main__":
    # Defina o IP alvo, porta alvo e o exploit a ser usado
    ip_alvo = "99.99.99.254"
    porta_alvo = 3306
    # Aqui você deve substituir "exploit" pelo exploit específico que deseja usar
    exploit = "MS08-067"
    # Chamando a função para explorar a vulnerabilidade
    explorar_vulnerabilidade(ip_alvo, porta_alvo, exploit)
