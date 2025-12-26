import pyfirmata2  # <--- O '2' é fundamental aqui
import time

# Tente detectar a porta automaticamente ou force a 'COM3'
# Para Windows, geralmente é 'COM3', 'COM4' etc.
porta = "COM5" 

print(f"Tentando conectar na {porta}...")

try:
    # Iniciando a placa com a versão 2
    placa = pyfirmata2.Arduino(porta)
    print("Conexão estabelecida!")

    # Configura o pino 13 (LED interno do Arduino)
    led = placa.get_pin('d:13:o') 

    while True:
        led.write(1)
        print("Ligado")
        time.sleep(0.5)
        led.write(0)
        print("Desligado")
        time.sleep(0.5)

except Exception as e:
    print(f"Erro: {e}")
finally:
    if 'placa' in locals():
        placa.exit()