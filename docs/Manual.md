# Manual do Usuário | Donatello AGV

## Especificações do sistema

### Introdução do sistema
O Donatello é um AGV (Autonomous Ground Vehicle) desenvolvido para a inspeção de espaços confinados, especialmente tubulações da Gerdau. Ele foi construído utilizando a plataforma TurtleBot3, ROS2 (Robot Operating System 2), Nav2 (Navigation2), Raspberry Pi, sensores de qualidade do ar, uma câmera e um modelo de detecção de rachaduras treinado com Yolov8 utilizando OpenCV. O robô pode ser controlado manualmente por meio de uma interface gráfica ou seguir uma rota previamente determinada em um mapa. Os sensores enviam dados continuamente para o front-end, fornecendo informações sobre as condições atmosféricas para garantir a segurança dos operadores. O sistema de IA detecta rachaduras, e a câmera permite que o técnico visualize o ambiente remotamente.

### Lista de componentes do sistema

#### Robô TurtleBot3
- Raspberry Pi
- Sensores de qualidade do ar
- Câmera Dobot
- Modelo de detecção de rachaduras treinado com Yolov8 e OpenCV
- Software ROS2 (Robot Operating System 2) e Nav2 (Navigation2)

### Especificações técnicas do Sistema

Peso total: [Inserir peso total do sistema]

Dimensões: [Inserir dimensões do sistema]

Velocidade máxima: [Inserir velocidade máxima do sistema]

Autonomia da bateria: [Inserir autonomia da bateria]

Compatibilidade com sistemas operacionais: [Inserir sistemas operacionais compatíveis]

## Manual Operacional
## Frontend 
- Para a inicialização do sistema em local host é necessário entrar na pasta \src e depois entrar em \frontend e rodar o seguinte comando: npm install, para intalar todas as dependencias necessárias para rodar o front. Por fim, para testar o frontend basta rodar na mesma pasta o comando: npm run dev. Ele irá geral a url do site que poderá ser aberto no navegador.
## Backend
- Para a inicialização do sistema é necessário instalar a pasta requirements para todas as rotas e arquivos em python funcinarem.



### Guia de Montagem e Inicialização do Sistema

**Para o robô**

**Para a simulação**

**Para o modelo de AI**

### Instruções operacionais

**Movimentação manual do robô**

**Mapeamento de ambiente**

**Movimentação em mapa**

**Checagem de outputs do AI**

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
