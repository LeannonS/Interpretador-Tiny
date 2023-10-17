# Interpretador para Tiny

Esse projeto contém a implementação de um interpretador para a linguagem Tiny.
Essa é uma linguagem simples, utilizada para exercitar os conceitos necessários
para a disciplina de linguagens de programação do CEFET-MG.
<a href="https://github.com/rimsa" target="_blank">Andrei Rimsa</a> (CEFET/MG) e <a href="https://github.com/DiegoAscanio" target="_blank">Diego Ascanio</a> (CEFET/MG), o interpretador da linguagem tiny foi feito na linguagem de programação python.

## Características da linguagem

Tiny é uma linguagem interpretada de brinquedo com uma sintaxe e semântica
simples.
* A linguagem possui quatro tipos de comandos: comando condicional (**if**),
comando de repetição (**while**), comando de atribuição (**id = expr**) e
comando de saída (**output expr**).
* Esses comandos podem ser combinados para formar blocos de comandos.
Um programa em Tiny começa com a palavra-reservada **program** seguida de um
bloco de comandos.
* Identificadores (variáveis) começam com uma letra ou underscore (_) e podem
ser seguidos de letras, dígitos e underscore (_).
Esses armazenam apenas números inteiros.
* A linguagem permite avaliação de expressões lógicas simples em comandos
condicionais e de repetição.
* As expressões lógicas suportadas são: igual (**==**), diferente (**!=**),
menor (**<**), maior (**>**), menor igual (**<=**), maior igual (**>=**).
Não existe forma de conectar multiplas expressões lógicas com E/OU.
* A linguagem suporta constantes númericas inteiras e leitura de um valor
númerico inteiro do teclado (**read**).
* Expressões artiméticas são suportadas sobre números inteiros: adição (**+**),
subtração (**-**), multiplicação (**&ast;**), divisão (**/**) e
resto da divisão (**%**). Expressões artiméticas compostas devem usar,
necessariamente, identificadores auxiliares.
* A linguagem possui comentários de uma linha a partir do símbolo tralha (#).

## Exemplo de Execução

Um exemplo de linguagem é dado a seguir (*somatorio.tiny*).

```
# calcula o somatório de números obtidos pela entrada
program
    sum = 0;
    i = read;
    while i > 0 do
        sum = sum + i;
        i = read;
    done;
    output sum;
```

Esse programa produz o somatório de números inteiros enquanto o usuário
entrar com valores maiores que zero.
Ao final, é exibido o valor do somatório.
Por exemplo, para os números 4, 8, 15, 16, 23, 42, o interpretador produz o
somatório 108.

    $ Interpretador_Tiny/tinyi.py examples/somatorio.tiny
    4
    8
    15
    16
    23
    42
    0
    108

## Referências

[1] RIMSA, ANDREI - Repositório GitHub, @rimsa: tiny - Disponível em: https://github.com/rimsa/tiny.

[2] ASCANIO, DIEGO - Repositório GitHub, @DiegoAscanio: interpretador tiny incompleto - Disponível em: https://github.com/DiegoAscanio/interpretador-tiny-incompleto.

[3] ASCANIO, DIEGO - Repositório GitHub, @DiegoAscanio: analizador lexico exemplo - Disponível em: https://github.com/DiegoAscanio/analisador-lexico-exemplo.
