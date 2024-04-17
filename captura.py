from scapy.all import *

def capturar_pacotes_icmp():
    # Define um filtro para capturar apenas os pacotes ICMP echo-request do alvo
    filtro_alvo = "icmp and src host 99.99.99.254 and icmp[icmptype] == 8"
    # Define um filtro para capturar apenas os pacotes ICMP echo-reply do Kali
    filtro_kali = "icmp and src host 99.99.99.50 and icmp[icmptype] == 0"
    
    try:
        # Captura os pacotes ICMP do alvo
        pacotes_alvo = sniff(filter=filtro_alvo, timeout=10)
        print("Pacotes ICMP echo-request capturados do alvo:")
        print(pacotes_alvo.summary())
        
        # Captura os pacotes ICMP do Kali
        pacotes_kali = sniff(filter=filtro_kali, timeout=10)
        print("\nPacotes ICMP echo-reply capturados do Kali:")
        print(pacotes_kali.summary())
        
    except KeyboardInterrupt:
        print("\nCaptura interrompida pelo usuário.")

# Exemplo de uso
if __name__ == "__main__":
    capturar_pacotes_icmp()
