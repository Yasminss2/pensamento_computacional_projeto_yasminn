# 🍧 Sistema de Vendas - Açaíteria

Este projeto consiste em um sistema de gerenciamento e vendas baseado em terminal para uma Açaíteria, desenvolvido inteiramente em Python. O software visa organizar o catálogo de produtos, controlar estoque, aplicar regras de promoções diárias, processar pagamentos e registrar o histórico de vendas de forma simples e eficiente.
<!-- Esse projeto é meu -->
---

## 📌 Panoramas Gerais (Histórias de Usuário)

O desenvolvimento deste sistema foi guiado por diferentes perspectivas e necessidades de negócio:

* **👑 Product Owner (PO):** Necessita de um sistema de vendas centralizado para organizar os produtos da açaíteria, controlar o fluxo de saída de mercadorias e oferecer um atendimento rápido e ágil aos clientes.
* **👥 Quality Assurance / Cliente (QA):** Deseja um sistema transparente onde seja possível visualizar o menu de produtos, escolher o açaí ideal com seus respectivos adicionais, consultar informações da loja e realizar compras sem complicações.
* **💻 Tech / Programador:** Focado em criar um software estruturado, limpo, modular e de fácil manutenção utilizando os conceitos fundamentais da lógica de programação em Python.
* **🛠️ Developer (Dev):** Responsável por implementar regras de cadastro de produtos, listagem dinâmica, controle rigoroso de estoque, aplicação de cupons/descontos, e armazenamento do histórico de vendas.
* **🎨 UX Designer:** Preocupado em garantir uma interface de terminal simples, com menus numéricos de fácil navegação e retornos visuais amigáveis (emojis e resumos de pedidos) para o usuário.
* **📊 Analista de Dados (IA):** Busca coletar registros precisos sobre o volume de vendas, faturamento e as preferências de sabores/tamanhos mais pedidos para futuras tomadas de decisão na empresa.

---

## 🚀 Funcionalidades Principais

O sistema opera em um loop interativo (`while True`) com um menu composto por 10 opções:

1.  **Gerenciamento de Produtos:** Permite cadastrar dinamicamente até 3 produtos simultâneos no sistema (vagas limitadas no código atual), definindo nome, estoque inicial, preço, validade e descrição.
2.  **Listagem de Catálogo:** Exibe de forma organizada os detalhes de todos os produtos ativos e disponíveis no sistema.
3.  **Realização de Vendas:** Abate a quantidade desejada do estoque atual do produto, calcula o valor parcial e armazena os dados temporariamente.
4.  **Cardápio Interativo:** Menu interativo focado na experiência do cliente, permitindo selecionar o tamanho do açaí (*Tradicional, Premium ou Especial*) e os *toppings* adicionais (*Frutas, Granola, Paçoca ou Nutella*).
5.  **Módulo de Promoções:** Regras de negócio automatizadas por dia da semana:
    * *Terça do Tradicional:* 15% de desconto para compras acima de 2 unidades do açaí tradicional.
    * *Quinta Premium:* R$ 10,00 de desconto fixo no total.
    * *Combo Fim de Semana (Sex a Dom):* 10% de desconto em compras com valor total acima de R$ 90,00.
6.  **Formas de Pagamento:** Processamento de pagamentos com tratativas específicas:
    * **Pix:** Concede 5% de desconto automaticamente.
    * **Cartão (Crédito/Débito):** Valor integral da compra.
    * **Dinheiro:** Cálculo automático de troco. *(Inclui estorno automatizado de estoque caso a venda seja cancelada ou o valor pago seja insuficiente).*
7.  **Histórico de Vendas:** Exibe um relatório completo de todas as transações finalizadas com sucesso durante a execução do programa.
8.  **Modos de Entrega, Contato e Suporte:** Estruturas preparadas para exibição de informações da loja física e canais de atendimento.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando recursos nativos da linguagem **Python 3**, sem a necessidade de instalação de bibliotecas externas:

* **Estruturas de Repetição e Condicionais:** `while`, `if`, `elif`, `else` para controle do fluxo do menu e validações.
* **Coleções de Dados:** * `Tuplas` para dados imutáveis (Tamanhos e Toppings).
    * `Listas` para dados dinâmicos (Dias da semana e Histórico de vendas).
    * `Dicionários` para mapeamento de dados estruturados (Preços promocionais e objetos de venda).
* **Funções (`def`):** Utilizadas para encapsular e modularizar a lógica do cálculo de descontos e promoções.
* **Formatação de Strings:** Uso de f-strings e formatadores numéricos (`:.2f`) para exibição monetária limpa.

---

## 🎮 Como Executar o Projeto

1. Certifique-se de ter o **Python 3.x** instalado em sua máquina.
2. Faça o clone deste repositório ou baixe o arquivo do código.
3. Abra o terminal na pasta do arquivo e execute o comando:
   ```bash
   python nome_do_seu_arquivo.py
