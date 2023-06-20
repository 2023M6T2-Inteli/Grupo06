#include "dht.h" //INCLUSÃO DE BIBLIOTECA

const int PinA0 = A0;//PINO UTILIZADO PELO SENSOR DE GÁS MQ-2
const int pinoDHT11 = A2; //PINO ANALÓGICO UTILIZADO PELO DHT11

dht DHT; //VARIÁVEL DO TIPO DHT

int leitura_sensor = 300;//DEFININDO UM VALOR LIMITE (NÍVEL DE GÁS NORMAL)

void setup(){
pinMode(PinA0, INPUT); //DEFINE O PINO COMO ENTRADA
// pinMode(Pinbuzzer, OUTPUT); //DEFINE O PINO COMO SAÍDA
Serial.begin(9600);//INICIALIZA A SERIAL
delay(1000); //INTERVALO DE 1 SEGUNDO ANTES DE INICIAR
}
void loop(){
  DHT.read11(pinoDHT11); //LÊ AS INFORMAÇÕES DO SENSOR
  int valor_analogico = analogRead(PinA0); //VARIÁVEL RECEBE O VALOR LIDO NO PINO ANALÓGICO
  Serial.print("Leitura de gás do sensor: "); //EXIBE O TEXTO NO MONITOR SERIAL
  Serial.println(valor_analogico);// MOSTRA NO MONITOR SERIAL O VALOR LIDO DO PINO ANALÓGICO
  Serial.print("Umidade: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.humidity); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO
  Serial.print("%"); //ESCREVE O TEXTO EM SEGUIDA
  Serial.print(" / Temperatura: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(DHT.temperature, 0); //IMPRIME NA SERIAL O VALOR DE UMIDADE MEDIDO E REMOVE A PARTE DECIMAL
  Serial.println("*C"); //IMPRIME O TEXTO NA SERIAL
  delay(1000); //INTERVALO DE 1 SEGUNDOS * NÃO DIMINUIR ESSE VALOR
}