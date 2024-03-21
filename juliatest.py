juliatest

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

 """


INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

"""----------------------------

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem python, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;



Resposta: """

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




"""
--------------------------------------------------------------------------------

5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

Resposta:"""

def inverter_string(string):
    string_invertida = ""
    for caractere in string:
        string_invertida = caractere + string_invertida
    return string_invertida

# Exemplo de uso
string = input("Digite uma string: ")
string_invertida = inverter_string(string)
print("String invertida:", string_invertida) 