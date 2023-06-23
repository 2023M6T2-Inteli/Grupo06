<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="20%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

# Sistema de Inspeção de Espaços Confinados para a Gerdau

Este repositório contém uma solução de inspeção de espaços confinados para a Gerdau, que utiliza um AGV (Autonomous Ground Vehicle) conectado a um dashboard para visualização dos dados coletados em tempo real e historicamente. O objetivo principal dessa solução é garantir a segurança do ambiente durante a inspeção, aumentar a acurácia na medição de gases e evitar gargalos operacionais.

## Documentação

A documentação completa desse sistema pode ser encontrada [aqui](https://github.com/2023M6T2-Inteli/lincore/blob/main/docs/index.md#miss%C3%A3o-do-projeto).

## Manual do Usuário

Para obter informações detalhadas sobre como utilizar o sistema, consulte o [Manual do Usuário](https://github.com/2023M6T2-Inteli/lincore/blob/main/docs/Manual.md).

## Features

O sistema possui as seguintes features:

- **Leitura de Nível de Gás Ambiente em Tempo Real:** Permite monitorar o nível de gases presentes no ambiente de forma contínua e em tempo real.
- **Dashboard de Visualização de Dados da Inspeção Atual:** Apresenta os dados coletados pelo AGV durante a inspeção atual em um formato visualmente intuitivo.
- **Histórico de Dashboards:** Permite acessar dashboards históricos de inspeções anteriores, facilitando a comparação e análise dos dados coletados ao longo do tempo.
- **Visão Computacional para Análise de Rachaduras nas Paredes do Ambiente:** Utiliza a tecnologia YoloV8 para detectar e analisar rachaduras nas paredes do espaço confinado, fornecendo informações importantes para manutenção preventiva.

## Tecnologias Utilizadas

O sistema faz uso das seguintes tecnologias:

- **FastAPI:** Framework web utilizado para desenvolver a API que alimenta o dashboard e fornece os dados coletados pelo AGV.
- **YoloV8:** Um modelo de rede neural utilizado para detecção e análise de objetos, nesse caso, rachaduras nas paredes do ambiente.
- **ROS2:** Middleware de comunicação utilizado para integrar o AGV e os sensores ao sistema.
- **NAV2:** Pacote de navegação para o ROS2, responsável pelo planejamento de rotas e movimentação do AGV no espaço confinado.
- **Next.js:** Framework de desenvolvimento web utilizado para criar o frontend do dashboard, proporcionando uma experiência de usuário moderna e responsiva.
- **SQL:** Linguagem de consulta estruturada utilizada para manipulação de dados no banco de dados.
- **Supabase:** Serviço de armazenamento online de imagens utilizado para armazenar imagens capturadas pelo AGV durante a inspeção.
- **AWS:** Amazon Web Services, utilizado para armazenar o banco de dados em um serviço de RDS (Relational Database Service).
- **Robô: Turtlebot3 Burguer:** Robô utilizado como AGV para realizar a inspeção dos espaços confinados, equipado com sensores de gás e câmera para captura de imagens.

## Instalação e Configuração

Para instalar e configurar o sistema, siga as instruções detalhadas no [Guia de Instalação](https://github.com/2023M6T2-Inteli/lincore/blob/main/docs/index.md#miss%C3%A3o-do-projeto).

## Contribuição

Contribuições para o aprimoramento deste sistema são bem-vindas. Sinta-se à vontade para enviar pull requests e relatar problemas.


