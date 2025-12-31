# 🔐 Criptografia e Descriptografia de Arquivos

Este projeto foi desenvolvido com o objetivo de **estudar e demonstrar o funcionamento da criptografia e descriptografia de dados**. O cenário simula **mecanismo criptográfico**, o impacto da **indisponibilidade dos dados** e na **recuperação segura da informação** usados em ataques do tipo ransomware**.

---

## 🎯 Objetivo do Projeto

- Compreender como funciona a **criptografia simétrica**
- Aplicar criptografia em arquivos reais (`.txt`)
- Demonstrar a indisponibilidade de dados sem a chave correta
- Simular a recuperação dos dados via descriptografia
- Estudar conceitos aplicados à Segurança da Informação

---

## 🚀 Funcionalidades Principais

* Geração segura de chave criptográfica
* Verificação para evitar sobrescrita da chave
* Criptografia de arquivos `.txt`
* Remoção do arquivo original após criptografia
* Descriptografia e recuperação do conteúdo
* Manipulação correta de arquivos binários
* Estrutura simples e modular para estudo

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem & Core:**
    * ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    * ![Segurança da Informação](https://img.shields.io/badge/Segurança%20da%20Informação-2C3E50?style=for-the-badge)

* **Bibliotecas & Conceitos:**
    * ![Cryptography](https://img.shields.io/badge/cryptography-Fernet-8E44AD?style=for-the-badge)
    * ![Pathlib](https://img.shields.io/badge/pathlib-Manipulação%20de%20Arquivos-2980B9?style=for-the-badge)

* **Ferramentas:**
    * ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
    * ![GitHub](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)

---

## 🛠️ Como usar

### 1. Criptografar o arquivo
Execute o comando:

python encrypter.py

O processo irá:
- Criar o arquivo `secret.key` caso ainda não exista
- Criptografar o conteúdo de `teste.txt`
- Gerar `teste.txt.ransomwaretroll.bin`
- Remover o arquivo original `teste.txt`, simulando indisponibilidade dos dados

### 2. Descriptografar o arquivo
Execute o comando:

python decrypt.py

O processo irá:
- Ler o arquivo `teste.txt.ransomwaretroll.bin`
- Utilizar a chave `secret.key`
- Restaurar o arquivo `.txt` com o conteúdo original
- Remover o arquivo `teste.txt.ransomwaretroll.bin`

---

## 📮 Contato

Se quiser acompanhar mais estudos, projetos e evolução na área de Python e back-end:  

**[Carlos Marques]**

* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carlos-marques-a41721162/)
* [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/carlosMarques2810)
* ✉️ carlosmarques.2810@gmail.com