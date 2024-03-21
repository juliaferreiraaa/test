# test
Código Teste Gupy

"""
* Teste Estágio Gupy  *
( Linguagem Python )

1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);

 
Resposta :

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

----------------------------

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem python, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;



Resposta:

def fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))
if fibonacci(numero):
    print("O número pertence à sequência de Fibonacci.")
else:
    print("O número não pertence à sequência de Fibonacci.")

--------------------------------------------------
3) Descubra a lógica e complete o próximo elemento:


a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____

Resposta:

a) 1, 3, 5, 7, 9

b) 2, 4, 8, 16, 32, 64, 128

c) 0, 1, 4, 9, 16, 25, 36, 49

d) 4, 16, 36, 64, 100

e) 1, 1, 2, 3, 5, 8, 13

f) 2, 10, 12, 16, 17, 18, 19, 20

---------------------------------------
4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

Resposta:

Na primeira visita à sala das lâmpadas:

Ligue o primeiro interruptor e deixe-o ligado por um tempo.
Em seguida, desligue o primeiro interruptor e ligue o segundo interruptor.
Entre na sala.
Na segunda visita à sala das lâmpadas:

Observe o estado das lâmpadas:
Se uma lâmpada estiver acesa, isso significa que o segundo interruptor está conectado a ela.
Se uma lâmpada estiver desligada e quente, isso significa que o primeiro interruptor está conectado a ela.
Se uma lâmpada estiver desligada e fria, isso significa que o terceiro interruptor está conectado a ela.
Com este método, podemos determinar qual interruptor controla cada lâmpada com apenas duas visitas à sala das lâmpad

--------------------------------------------------------------------------------

5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

Resposta:

def inverter_string(string):
    string_invertida = ""
    for caractere in string:
        string_invertida = caractere + string_invertida
    return string_invertida

# Exemplo de uso
string = input("Digite uma string: ")
string_invertida = inverter_string(string)
print("String invertida:", string_invertida) """
