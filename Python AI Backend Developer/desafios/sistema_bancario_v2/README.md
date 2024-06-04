# Sistema Bancário em Python V2

## Descrição do Projeto

Este projeto consiste no desenvolvimento de um Sistema Bancário em Python, com o objetivo de implementar três operações essenciais: depósito, saque e extrato. O sistema é projetado para um banco que busca monetizar suas operações e oferece uma oportunidade prática para aplicar conhecimentos de programação Python na criação de um sistema funcional que simule operações bancárias. Nesta versão 02 do sistema também foram inclusas as operações de cadastro de usuário e conta, além das funções que visualizam todos os dados de cadastro de ambas operações.

## Funcionalidades

### Depósito
- É permitido depósitos de no mínimo R$ 10,00.
- Não permite valores negativos.
- Todos os depósitos são armazenados e exibidos no extrato.

### Saque
- Permite até 3 saques diários.
- Cada saque pode ser de no máximo R$ 500,00.


### Criação de usuário
- Adiciona à lista um novo usuário, desde que o CPF ainda não tenha sido usado.

### Criação de conta
- Adiciona à lista uma nova conta. 
- Um CPF pode criar várias contas, mas para criar uma conta, sempre é necessário um usuário. 
- Ao criar uma conta, caso o CPF ainda não tenha sido cadastrado, há a opção de criar apenas um usuário ou criar um novo usuário e a partir disso, usar o mesmo cadastro para criar a conta.

### Ver extrato, usuários e contas 
- É possível visualizar todas as operações realizadas (depósitos e saques) com seus respectivos valores, mostrando também o saldo inicial e o atual da conta.
- É possível visualizar todos os usuários cadastrados no sistema.
- É possível visualizar todas as contas cadastradas no sistema.
