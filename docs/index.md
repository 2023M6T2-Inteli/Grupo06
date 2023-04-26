<table>
<tr>
<td>
<a href= "https://www2.gerdau.com.br/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Gerdau_logo_%282011%29.svg/1200px-Gerdau_logo_%282011%29.svg.png" alt="Gerdau" border="0" width="70%"></a>
</td>
<td><a href= "https://www.inteli.edu.br/"><img src="https://www.inteli.edu.br/wp-content/uploads/2021/08/20172028/marca_1-2.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0" width="30%"></a>
</td>
</tr>
</table>

<font size="+12"><center>

</center></font>

# Entendimento de negócios
## Matriz de oceano azul
## Matriz de risco
## Canvas de proposta de valor
## Análise financeira

# Entendimento de metadesign
## Fatores mercadológicos
### Orientação ao mercado e precificação
Os AGVs são veículos automatizados que seguem uma trajetória previamente definida. Eles são capazes de transportar grandes cargas de forma repetitiva, com sensores e câmeras para evitar colisões, e podem ser usados em ambientes confinados onde há riscos à segurança dos trabalhadores. 

Pensando nisso, o projeto do robô Donatello trata-se de um AGV para monitoramento e inspeção de espaços confinados. Visa diminuir a exposição dos funcionários da Gerdau a perigos como níveis de oxigênio prejudiciais e gases tóxicos. Nesse sentido, o Donatello utiliza visão computacional, sensores e gravações do ambiente para identificar a situação atual desses espaços sem a presença física de um técnico. 

Além disso, o Donatello se orienta ao mercado no atendimento de demandas por segurança e eficiência. Sua aplicação está diretamente relacionada ao conceito de Indústria 4.0, pois, com ele, pode-se otimizar processos produtivos através da captura de dados em tempo real para auxiliar na tomada de decisão. A tendência mercadológica é comprovada pela Confederação Nacional da Indústria, que aponta que 48% da indústria brasileira pretende investir na Indústria 4.0 nos próximos anos (“Crescimento do investimento na Indústria 4.0”, [s.d.]). 

No que tange à precificação, em geral, AGVs tendem a variar entre US$40.000 e US$200.000 (“How much does an AGV cost?”, [s.d.]), dependendo do tipo de navegação, bateria, carregamento, peso suportado, altura atingida, etc. Ainda, considera-se também o investimento para a implementação do robô nos processos da empresa, o que inclui treinamento de pessoal, instalação de referências para o movimento (trilhos, fitas, QR codes, etc), integração com os sistemas vigentes, entre outros.

No caso do Donatello, a precificação incluirá os custos do TurtleBot3, dos sensores utilizados, dos utensílios de hardware empregados para sua fabricação e hospedagem online do dashboard. Igualmente, deve-se também considerar o investimento para implementação da solução na Gerdau.

### Cenário do mercado
O projeto abrange o cenário do mercado de automação e robótica industrial, com foco em aplicações para ambientes de espaço confinado e inspeção estrutural.

Nesse sentido, aponta-se que o mercado global de robótica industrial está em constante expansão, com um crescimento estimado de US$ 25 bilhões em 2021 a US$ 260 bilhões em 2030, segundo um relatório da BCG (Boston Consulting Group) (ARTES, 2022). No Brasil, a tendência mercadológica é explicitada ao utilizarem-se cada vez mais robôs como o da companhia Vale, por exemplo, que adquiriu um cão-robô para fiscalizar zonas de mineração e seus espaços confinados, como tubulações, galerias e drenos (“Vale investe em robôs para retirar empregados de situação de risco e aumentar a segurança de suas operações”, [s.d.]). Desse modo, a crescente demanda por eficiência e segurança nas operações industriais têm impulsionado a adoção de robôs em diversos setores, como o petroquímico, de energia, construção civil e mineração.

Em ambientes confinados, onde o acesso humano é limitado ou arriscado, a utilização de robôs tem se mostrado uma solução promissora para aumentar a segurança e a eficiência. De fato, apenas na América Latina, espera-se que o mercado de AGVs, para esse e outros fins, chegue a US$ 963,8 milhões até 2026. 

Nesse contexto, o projeto é especialmente relevante para a Gerdau, a qual tem como valores fundamentais a inovação constante em processos produtivos para maximizar a segurança de seus funcionários (“Sobre nós”, [s.d.]). Com a introdução de inspeções automatizadas antes e depois de sessões de manutenção, será possível atingir níveis ainda maiores de qualidade de ambiente de trabalho e satisfação de seus operários, além de aumentar a eficiência e produtividade da companhia.

### Visão do projeto proposto

## Sistema produto-design
## Sustentabilidade ambiental

# Arquitetura do sistema
## Requisitos funcionais e não funcionais
### Funcionais
1. Detecção de condições atmosféricas, incluindo quantidade de oxigênio, presença de gases tóxicos e temperatura, em diferentes pontos no espaço confinado;
2. Verificação de condições de segurança da NR33;
3. Inspeção antes e após a manutenção;
4. Certificação de que equipamentos de manutenção não foram esquecidos no espaço confinado após o término da operação;
5. Sensor na base do robô para detectar colisões;
6. Rotina de retorno ao ponto inicial em caso de erros e/ou colisões;
7. Movimentação determinada por trilha em fitas;
8. Movimentação opcional por controle remoto;
9. Dashboard com apresentação dos dados coletados em tempo real;
10. Dashboard com vídeo em tempo real;
11. Geração de relatórios em PDF;
12. Alerta sonoro na interface gráfica em caso de erros e/ou colisões.

### Não funcionais
1. Performance otimizada para garantir a eficiência do processo de inspeção: o sistema deve ser capaz de executar as inspeções de forma eficiente, com uma taxa de sucesso de pelo menos 95%.
2. Confiabilidade na detecção de condições atmosféricas: o sistema deve ser capaz de detectar com precisão a quantidade de oxigênio e a presença de gases tóxicos com uma margem de erro de no máximo 5%.
3. Funcionamento confiável em ambientes com falta de regularidade (tubulações):poderá haver o sistema deve ser capaz de navegar em tubulações com uma margem de erro de no máximo 10%.
4. Rápido tempo de resposta em detecção de obstáculos: o sistema deve ser capaz de detectar obstáculos em no máximo 1 segundo.
5. Confiança na precisão da detecção de obstáculos: o sistema deve ser capaz de detectar obstáculos com pelo menos 95% de precisão.
6. Interação com usuário intuitiva: a interface deve ser fácil de usar e compreender para o usuário final (executante da manutenção) e gestor (dash/relatórios).

## Viabilidade técnica
Para que haja uma implementação, então, do AGV Donatello, é necessário considerar alguns aspectos técnicos, como a escolha dos sensores, do hardware e do software e suas limitações. O hardware principal utilizado, como já citado, será o Donatello, que é um módulo robótico TurtleBot3, e apesar de ser um sistema com baixo custo de implementação e versátil ele pode ter velocidade e autonomia um pouco limitados por conta do seu processador de baixa potência. No caso dos sensores, serão utilizados sensores capazes de medir condições atmosféricas e detectar obstáculos, e como as tubulações serão consideradas superfícies planas por conta da prototipação do sistema para a locomoção do robô, poderá haver algumas limitações na detecção de alguns obstáculos nesse espaço, como pequenos detritos e declives à sua frente e abaixo, por exemplo. Considerando-se ainda a aquisição de dados físicos do espaço, para a medição de condições atmosféricas, serão utilizados sensores de temperatura, de oxigênio e de gases tóxicos, e tais sensores podem ter uma limitação quanto à resolução e precisão da aquisição dessas medições físicas.  Em relação à detecção de obstáculos, será utilizado o sensor "LiDAR"(Light Detection and Ranging) que está embutido no módulo robótico TurtleBot3, um sensor capaz de detectar obstáculos por meio da emissão de laser na banda do infravermelho próximo, e com isso, modela a superfície do terreno tridimensionalmente, mas pode ser que as tubulações dificultem a aquisição de dados do ambiente e um grande volume de dados pode interferir no processamento desse sensor também. Além disso, como um monitoramento com a identificação das condições ambientais em tempo real agrega valor ao projeto, será utilizada uma câmera para a captação das imagens e transmissão das condições em tempo real para os operadores, contudo, dependendo da iluminação do ambiente, o envio das imagens pode ser prejudicado. Por fim, o software utilizado para simular o roteamento da movimentação robótica no ambiente será feita pelo ROS (Robot Operating System), que é um meta sistema operacional que fornece uma estrutura de desenvolvimento, gerenciamento e execução de aplicações robóticas, no entanto, por ser uma tecnologia mais recente e está em constante evolução, a implementação deste software traz uma complexidade maior para a simulação e, além disso, pode apresentar também vulnerabilidades de segurança ao usar um ambiente de rede compartilhada. 

## Proposta geral
O objeto da proposta geral do sistema é o desenvolvimento de um AGV (Automated Guided Vehicle) para inspeção pré-manutenção e pós-manutenção de espaços confinados, com foco em tubulações. O sistema será capaz de examinar as condições atmosféricas em diferentes pontos, detectar a presença de gases e a quantidade de oxigênio, além de alertar o operador sobre possíveis obstáculos para sua locomoção na tubulação. A interface com dados e vídeo em tempo real permitirá a geração de relatórios em PDF e vídeos da inspeção. O sistema será projetado para melhorar as condições de segurança do operador e a eficiência do processo de inspeção, reduzindo o tempo necessário para realizar a inspeção e evitando a possibilidade de esquecimento de ferramentas ou equipamentos no interior dos tubos. O usuário final do sistema será o executante da manutenção, enquanto o usuário indireto será o gestor responsável por visualizar os dados e relatórios gerados pelo sistema.

## Arquitetura da solução
A arquitetura da solução para o projeto de AGV de inspeção de espaços confinados será composta por três principais elementos: hardware, software e comunicação. O hardware incluirá o próprio AGV, equipado com sensores de colisão, sensores de gás, câmeras de vídeo, sensores de temperatura e um sistema de monitoramento das condições atmosféricas do ambiente. O software será responsável por controlar o movimento do AGV, detectar obstáculos e alterar a rota do AGV quando necessário. Também será responsável pela interface com o usuário, permitindo o controle remoto do AGV e a visualização dos dados e relatórios gerados durante a inspeção. Por fim, a comunicação será realizada via rede sem fio, permitindo a transmissão dos dados e relatórios gerados em tempo real para o gestor responsável pelo monitoramento do sistema. Com essa arquitetura, o sistema será capaz de realizar a inspeção de forma autônoma, segura e eficiente, proporcionando ao usuário final a tranquilidade e agilidade necessárias para a realização de uma manutenção confiável.

![image]("https://github.com/2023M6T2-Inteli/lincore/blob/main/media/arquitetura/arquitetura_sprint_1.jpg?raw=true")

# Referências
How much does an AGV cost? Disponível em: <https://www.flexqube.com/news/how-much-does-an-agv-cost/#:~:text=Based%20on%20the%20main%20product>.

Crescimento do investimento na Indústria 4.0. Disponível em: <https://www.redutoresibr.com.br/noticia/crescimento-do-investimento-na-industria-4-0>. Acesso em: 24 abr. 2023.

Sobre nós. Disponível em: <https://www2.gerdau.com.br/sobre-nos/>.

Vale investe em robôs para retirar empregados de situação de risco e aumentar a segurança de suas operações. Disponível em: <https://ibram.org.br/noticia/vale-investe-em-robos-para-retirar-empregados-de-situacao-de-risco-e-aumentar-a-seguranca-de-suas-operacoes/>. Acesso em: 24 abr. 2023.

ARTES, L. Aumento no mercado de robótica e automação em 2022 > VDI Brasil. Disponível em: <https://www.vdibrasil.com/aumento-no-mercado-de-robotica-e-automacao-em-2022/#:~:text=No%20n%C3%ADvel%20global%2C%20as%20proje%C3%A7%C3%B5es>. Acesso em: 24 abr. 2023.
