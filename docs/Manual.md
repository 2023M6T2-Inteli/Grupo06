# Manual do Usuário | Donatello AGV


## Especificações do sistema


### Introdução do sistema
O Donatello é um AGV (Autonomous Ground Vehicle) desenvolvido para a inspeção de espaços confinados, especialmente tubulações da Gerdau. Ele foi construído utilizando a plataforma TurtleBot3, ROS2 (Robot Operating System 2), Nav2 (Navigation2), Raspberry Pi, sensores de qualidade do ar, uma câmera e um modelo de detecção de rachaduras treinado com Yolov8 utilizando OpenCV. O robô pode ser controlado manualmente por meio de uma interface gráfica ou seguir uma rota previamente determinada em um mapa. Os sensores enviam dados continuamente para o front-end, fornecendo informações sobre as condições atmosféricas para garantir a segurança dos operadores. O sistema de IA detecta rachaduras, e a câmera permite que o técnico visualize o ambiente remotamente.


### Componentes e especificações

- TurtleBot3
- Raspberry Pi
- Sensores de qualidade do ar
- Câmera Dobot
- Modelo de detecção de rachaduras treinado com Yolov8 e OpenCV
- Software ROS2 (Robot Operating System 2) e Nav2 (Navigation2)


## Manual Operacional

### Guia de Montagem e Inicialização do Sistema


**Para o robô**
=======
#### Robô
1. Abertura do Robô:


Antes de iniciar a instalação, abra o robô Donatello com cuidado, removendo a tampa ou qualquer outra proteção que possa estar no local. Certifique-se de tomar as precauções necessárias para evitar danos ao equipamento durante esse processo.


2. Verificação do Cartão SD:


O robô Donatello já vem com um cartão SD contendo o sistema operacional Ubuntu 22.04 devidamente instalado, juntamente com o ROS2, o LiDAR e o Nav2. Antes de prosseguir com a instalação, verifique se o cartão SD está corretamente inserido no Raspberry Pi do robô.


3. Conectando-se ao Raspberry Pi:
Existem duas alternativas para se conectar ao Raspberry Pi do Donatello:


a) Conexão utilizando mouse, teclado e monitor:
- Conecte um mouse, um teclado e um monitor ao Raspberry Pi do robô Donatello.
- Ligue o robô e aguarde até que o sistema operacional seja inicializado.
- Utilize o mouse e o teclado para interagir com o sistema operacional.


b) Conexão utilizando SSH para uma solução headless:


- Abra um terminal em seu computador.
- Para se conectar ao Raspberry Pi por SSH, utilize o endereço IP local ou o hostname do Raspberry Pi.
- No terminal, execute o seguinte comando:


```
ssh <usuário>@<hostname-pi>
```


Substitua <usuário> pelo nome de usuário configurado no Raspberry Pi e <hostname-pi> pelo nome do hostname configurado. Caso esteja executando o comando em um sistema Linux, verifique se o avahi-daemon está instalado e em execução. Para sistemas WSL (Windows Subsystem for Linux), utilize uma versão modificada do comando acima:


```
ssh <usuário>@<hostname-pi>.local
```


Se tudo ocorrer corretamente, você receberá uma mensagem perguntando se deseja adicionar o hostname à lista de hosts conhecidos.
Insira a senha correspondente ao usuário configurado no Raspberry Pi e você terá acesso ao terminal do Raspberry Pi.
Observação: Neste manual, daremos enfoque à solução headless utilizando SSH para a conexão com o Raspberry Pi.


## Interface gráfica

Para instalar um frontend utilizando a estrutura do Next.js, siga as seguintes etapas:

1. Certifique-se de ter o Node.js instalado em seu sistema. 
2. Navegue para a pasta src/frontend. Então, rode:

    ```
    npm install
    npm run dev
    ```
3. Então, acesse o site em [localhost:3000.com](localhost:3000.com)

# Execução do Servidor Backend

## Requisitos de Sistema

Antes de prosseguir com a instalação, certifique-se de ter os seguintes requisitos instalados:

- [uvicorn](https://www.uvicorn.org/)

## Instalação

Siga as etapas abaixo para instalar o servidor backend:

1. Abra o terminal do seu sistema operacional.

2. Certifique-se de que o `uvicorn` esteja instalado executando o seguinte comando:

   ```
   uvicorn --version
   ```

   Se o comando não for reconhecido, instale o pacote através do comando abaixo

   ```
   pip install "fastapi[standard]"
   ```

## Executando o Servidor Backend

Para executar o servidor backend da aplicação, siga estas etapas:

1. Navegue até a pasta 'src/backend' do projeto.

   ```
   cd src/backend
   ```

2. No terminal, execute o seguinte comando:

   ```
   uvicorn main:app --port 3000
   ```
   Certifique-se de que a porta `3000` esteja disponível para uso.

3. Aguarde até que o servidor backend seja inicializado. Você verá mensagens no terminal indicando o status do servidor.

   ```
   INFO: Uvicorn running on http://127.0.0.1:3000 (Press CTRL+C to quit)
   ```

4. Uma vez que o servidor esteja em execução, a interface da aplicação já acessa as rotas e endpoints disponiveis.

   Observação: Consulte a documentação completa da aplicação para obter mais detalhes sobre as rotas e endpoints disponíveis.

5. Caso deseje encerrar a execução do servidor, pressione `CTRL+C` no terminal.

Parabéns! Agora você pode executar o servidor backend da aplicação web e interagir com as informações do veículo.


**Para o modelo de AI**
=======

1. Certifique-se de ter o Python3.9 e pip instalados em seu sistema. 
2. Navegue para a pasta raiz do backend e rode:

```
pip install -r /path/to/requirements.txt
```
Então, acesse o site em localhost:3000

#### Simulação

Para instalar o ROS, precisamos adicionar novos repositórios ao apt, pois o ROS não se encontra nos repositórios padrão do Ubuntu. Para isso começaremos garantindo que o repositório universe está habilitado. Rode:

```
sudo apt-add-repository universe
```

A seguir, precisamos baixar uma chave GPG e adicioná-la ao keyring do sistema para poder validar o repositório que vamos adicionar. Rode:

```
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Agora precisamos adicionar o repositório à lista de repositórios. Use:

```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

Como fizemos alterações nos repositórios do apt, precisamos atualizar seu banco de dados novamente. Rode:

```
sudo apt update
```

Pronto! Agora estamos finalmente prontos para instalar a nossa distribuição de ROS. Rode:

```
sudo apt install ros-humble-desktop
```

```
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

A seguir, complete o guia de instalação e configuração do ROS 2 em https://docs.ros.org/en/humble/Installation.html.

Então, instale todos os pacotes relacionados ao turtlebot 3 utilizando o seguinte comando:

```
sudo apt install ros-humble-turtlebot3*
```

```
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc
```

Após rodar esse comando, é necessário dar source novamente na configuração do bash. Rode:

```
source ~/.bashrc
```

### Troubleshooting

**Erro de importação de mapa no Rviz**
Então, rode o seguinte:


```
sudo apt update
sudo apt install ros-humble-rmw-cyclonedds-cpp
gedit ~/.bashrc
```


Adicione a seguinte linha:


```
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```


Depois, vá para o seguinte caminho:


```
cd /opt/ros/humble/share/turtlebot3_navigation2/param
```


Altere o arquivo "waffle.yaml" pelo sudo gedit ou vim. Substitua a linha robot_model_type por:


```
robot_model_type: "nav2_amcl::DifferentialMotionModel"
```


Não se esqueça de dar source no ~/.bashrc antes de continuar!

### Instruções operacionais

**Movimentação manual do robô**
=======

Antes de comandar o TurtleBot3, é necessário configurar a variável de ambiente que define o modelo do robô. Execute o seguinte comando no terminal:


```
echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc && source ~/.bashrc
```


Isso define o modelo do TurtleBot3 como "burger" para a sessão atual e futuras sessões.


Em um terminal, execute o seguinte comando para iniciar o pacote do TurtleBot3:


```
ros2 launch turtlebot3_bringup robot.launch.py
```


Isso iniciará a operação do TurtleBot3 e permitirá que ele comece a receber comandos.


Em outro terminal, execute o pacote teleop para controlar o TurtleBot3 manualmente usando o teclado:


```
ros2 run turtlebot3_teleop teleop_keyboard
```


Agora você pode usar as teclas do teclado para controlar o movimento do robô.



# **Mapeamento de ambiente**


Em três terminais paralelos:


```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```


(abre o Turtlebot World no Gazebo)


```
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```


(abre o modo de mapeamento do RViz)


```
ros2 run turtlebot3_teleop teleop_keyboard
```


(abre o tópico de controle de movimentação do robô pelo teclado)


Então, movimente o robô por todo o mundo até que o mapa esteja bem delimitado no RViz (branco nas áreas livres e escuro nos obstáculos, sem manchas cinza no meio)


Para salvar o mapa, digite o seguinte comando na raiz do sistema operacional (~):


```
mkdir maps
cd maps
```


Rode o seguinte comando para salvar o mapa:


```
ros2 run nav2_map_server map_saver_cli -f <nome-do-mapa>
```


Se tudo deu certo, é para ter um arquivo ".pmg" e ".yaml" na pasta "maps".


**Abrir o mapa em si**
Em terminais paralelos, abra o Gazebo com o Turtlebot World e carregue o mapa gerado no RViz:


```
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```


Na pasta raiz (~):


```
ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=maps/<nome-do-mapa>.yaml
```


Feito isso, é só setar o ponto inicial e movimentar o robô normalmente pela interface gráfica ou API em Python.


### Considerações de segurança


**Riscos operacionais**


Ao operar o Donatello AGV, é importante estar ciente dos possíveis riscos operacionais. Aqui estão alguns exemplos de riscos que devem ser considerados:


- Colisões: O robô pode colidir com obstáculos presentes no ambiente, o que pode causar danos ao robô ou a objetos próximos. Isso pode ocorrer durante a operação manual ou em casos em que a navegação autônoma não detecta corretamente os obstáculos.


- Quedas: Se o Donatello AGV operar em superfícies elevadas ou inclinadas, existe o risco de queda. Isso pode resultar em danos ao robô e possivelmente a objetos ou pessoas próximas.


- Interferência eletromagnética: Em ambientes com interferência eletromagnética intensa, como em áreas próximas a equipamentos elétricos potentes, pode ocorrer interferência na comunicação e no funcionamento adequado do robô.


- Condições atmosféricas adversas: O Donatello AGV pode ser afetado por condições climáticas adversas, como chuva intensa, ventos fortes ou altas temperaturas. Essas condições podem impactar a capacidade do robô de se movimentar adequadamente e podem representar riscos adicionais de segurança.


- Erros de operação: O manuseio inadequado do Donatello AGV, como a inserção de comandos incorretos ou a seleção de configurações inadequadas, pode levar a ações indesejadas do robô, aumentando o risco de colisões ou quedas.


- Problemas de comunicação: Falhas na comunicação entre o operador e o Donatello AGV podem ocorrer, o que pode levar a atrasos nas respostas do robô ou ações imprevistas.


- Falhas do sistema: Embora seja uma prova de conceito, o Donatello AGV ainda pode apresentar falhas de hardware ou software que afetem seu desempenho e segurança operacional.


É fundamental estar ciente desses riscos e tomar as devidas precauções ao operar o Donatello AGV. Certifique-se de seguir todas as instruções fornecidas neste manual do usuário e adotar práticas de segurança adequadas para minimizar os riscos associados à operação do robô.


**Adequação do local**


Antes de operar o Donatello AGV, certifique-se de que o local de operação esteja adequado para evitar riscos desnecessários. Considere a presença de obstáculos, condições atmosféricas adversas ou outros fatores que possam afetar a segurança do robô e dos operadores.


**Guia de prevenção**
- Siga sempre as instruções operacionais fornecidas neste manual.
- Mantenha distância segura do Donatello AGV durante a operação.
- Nunca force os movimentos do robô além de suas capacidades.
- Em caso de emergência, pressione o botão de parada de emergência para interromper imediatamente as operações do Donatello AGV.


Lembre-se de que este manual é para uma prova de conceito, e o Donatello AGV não está plenamente integrado à simulação. Portanto, as instruções incluídas neste manual são para movimentar o robô manualmente e iniciar rotas pré-programadas na simulação. Certifique-se de seguir todas as regulamentações de segurança e requisitos específicos do local ao utilizar o robô para inspeção de espaços confinados.



