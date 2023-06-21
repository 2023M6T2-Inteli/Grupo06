import serial
import requests
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Configurações da porta serial
porta = '/dev/ttyACM0'  # Substitua pela porta correta
baud_rate = 9600

backend_url = 'http://127.0.0.1:3000/gas'

# Inicializa a comunicação serial
conexao = serial.Serial(porta, baud_rate)

# Lista para armazenar os valores analógicos
valores_analogicos = []

# Lista para armazenar as médias móveis
medias_moveis = []

# Número de amostras para calcular a média móvel
janela = 3

# Lista para armazenar as médias móveis por porcentagem
media_mov_porc = []

# Configura o gráfico
fig, ax = plt.subplots()

# variável para controlar o loop
continuar = True

try:
    # Lê os valores analógicos continuamente
    while continuar:
        # Lê uma linha da porta serial
        linha = conexao.readline().decode().strip()

        # Verifica se a linha contém um valor analógico válido
        if linha.startswith('Leitura'):
            valor_analogico = int(linha.split(':')[1])
            print('Valor analógico:', valor_analogico)

            # Calcula a média móvel usando a função np.mean()
            media_movel = np.mean(valores_analogicos[-janela:])

            # faz a média móvel em porcentagem
            porcentagem = (media_movel * 100) / 1023

            print('Média móvel:', media_movel)
            print(f'(Média móvel em porcentagem: {porcentagem:.2f}%)')
            # Armazena o valor analógico na lista
            valores_analogicos.append(valor_analogico)

            # Verifica se há valores suficientes para calcular a média móvel
            if len(valores_analogicos) >= janela:

                # Armazena a média móvel na lista
                medias_moveis.append(media_movel)
                media_mov_porc.append(porcentagem)

                # Realiza o envio do valor analógico para o backend
                payload = {'valor_analogico': valor_analogico, 'timestamp': str(datetime.now())}
                response = requests.post(f"{backend_url}", json=payload)
                if response.status_code != 201:
                    print('Falha ao enviar valor analógico para o backend:', response.text)


            if len(valores_analogicos) >= 3 :
                continuar = False

            # Atualiza o gráfico com os valores atuais e as médias móveis
            ax.clear()
            #ax.plot(valores_analogicos, label='Valores Analógicos')
            #ax.plot(medias_moveis, label='Médias Móveis')
            ax.plot(media_mov_porc, label='Médias Móveis em Porcentagem')
            ax.legend()

            # Define os rótulos e título do gráfico
            ax.set_xlabel('Amostras')
            ax.set_ylabel('Valor')
            ax.set_title('Valores Analógicos e Médias Móveis')

            # Exibe o gráfico
            plt.pause(0.01)

except KeyboardInterrupt:
    pass

finally:
    # Fecha a conexão serial
    conexao.close()

plt.show()