[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/7EVNAYx2)
# ClientServerBasics (2.0)
Starter code for the basic client-server assignment


Este template corresponde ao exemplo da Fig. 2.3 do livro. O exercício consiste em acrescentar funcionalidade ao servidor para torná-lo mais útil. Essa funcionalidade deve ser acessível aos clientes. Por exemplo, o servidor pode ser uma espécie de calculadora remota. O cliente passa dois valores numéricos, juntamente com o nome de uma operação (ex.: add, subtract, multiply, divide) e o servidor executa a operação respectiva e retorna seu resultado para o cliente. Você pode implementar um servidor com outras funcionalidades (diferente da calculadora). O imporante é que ele ofereça pelo menos três operações diferentes que os clientes podem utilizar remotamente, passando dados para serem processados e recebendo o resultado desse processamento como resposta.

Tarefa individual.

Incluir um Readme descritivo do sistema implementado.

---

## Funcionamento

O sistema segue o modelo cliente-servidor:

* O servidor permanece em execução aguardando conexões.
* O cliente se conecta ao servidor e envia requisições.
* O servidor processa os dados recebidos e retorna uma resposta.

A comunicação ocorre via sockets TCP.

---

## Funcionalidades

O servidor implementa as seguintes operações:

| Comando | Descrição               | Exemplo  |
| ------- | ----------------------- | -------- |
| ADD     | Soma dois números       | ADD 2 3  |
| SUB     | Subtrai dois números    | SUB 5 2  |
| MUL     | Multiplica dois números | MUL 3 4  |
| DIV     | Divide dois números     | DIV 10 2 |
| POW     | Potência                | POW 2 3  |
| SQRT    | Raiz quadrada           | SQRT 16  |

O cliente pode enviar qualquer um desses comandos ao servidor, que executa a operação correspondente e retorna o resultado.

---

## Protocolo de Comunicação

A comunicação entre cliente e servidor segue um protocolo baseado em texto:

Formato da requisição:

```
OPERACAO valor1 valor2
```

Exemplo:

```
ADD 10 5
```

Para operações com um único operando:

```
SQRT 16
```

O servidor responde com:

```
resultado | tempo servidor: X.XXXXXXs
```

---

## Medição de Tempo

O sistema mede o tempo de processamento no servidor e o tempo total no cliente (incluindo rede)

---

## Tratamento de Erros

O servidor trata situações como:

* Comandos inválidos
* Número incorreto de argumentos
* Divisão por zero
* Raiz de número negativo
