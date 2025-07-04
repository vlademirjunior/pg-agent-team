# AI Agent Test Questions & Expected Answers

This document provides a structured set of questions to test the capabilities of the Autonomous Database Analyst Agent. The questions are based on the provided database schema and are categorized by difficulty. Each question includes the expected answer for validation.

---

## Simple Questions (Single Table Queries)

### 1. Total de Clientes

* **PT-BR:** Quantos clientes estão registrados no total?
* **EN:** How many customers are registered in total?
* **Expected Answer:** Existem 5 clientes registrados. / There are 5 registered customers.

### 2. Item Mais Caro

* **PT-BR:** Qual é o item mais caro disponível e qual o seu preço?
* **EN:** What is the most expensive item available and what is its price?
* **Expected Answer:** O item mais caro é o 'Laptop', custando 1200.00. / The most expensive item is the 'Laptop', costing 1200.00.

### 3. Total de Pedidos

* **PT-BR:** Quantos pedidos foram feitos no total?
* **EN:** How many orders were made in total?
* **Expected Answer:** Foram feitos 6 pedidos no total. / There were 6 orders made in total.

---

## Medium Questions (Simple Joins & Filtering)

### 4. Pedidos de um Cliente Específico

* **PT-BR:** Liste as datas de todos os pedidos feitos pela cliente 'Ana Silva'.
* **EN:** List the dates of all orders made by the customer 'Ana Silva'.
* **Expected Answer:** Ana Silva fez pedidos nas datas 2023-10-01 e 2023-10-20. / Ana Silva placed orders on 2023-10-01 and 2023-10-20.

### 5. Itens em um Pedido Específico

* **PT-BR:** Quais itens, e em que quantidade, estavam no pedido de ID 3?
* **EN:** What items, and in what quantity, were in order ID 3?
* **Expected Answer:** O pedido continha 2 'Laptop', 1 'Gaming Mouse' e 1 'Mechanical Keyboard'. / The order contained 2 'Laptop', 1 'Gaming Mouse', and 1 'Mechanical Keyboard'.

### 6. Preço Médio por Categoria

* **PT-BR:** Qual é o preço médio de um item na categoria 'Electronics' (com base no preço de lista na tabela items)?
* **EN:** What is the average price of an item in the 'Electronics' category (based on the list price in the items table)?
* **Expected Answer:** O preço médio de um item na categoria 'Electronics' é 535.10. / The average price of an item in the 'Electronics' category is 535.10.

---

## Hard Questions (Complex Joins, Aggregations & Subqueries)

### 7. Cliente com Maior Gasto Total

* **PT-BR:** Mostre-me o cliente com o maior valor total de compras.
* **EN:** Show me the customer with the highest total purchase amount.
* **Expected Answer:** A cliente que mais gastou foi Carla Mendes, com um total de 2625.50. / The customer who spent the most was Carla Mendes, with a total of 2625.50.

### 8. Categoria de Item Mais Rentável

* **PT-BR:** Qual é a categoria de item mais vendida em termos de receita total?
* **EN:** What is the best-selling item category by total revenue?
* **Expected Answer:** A categoria mais rentável é 'Electronics'. / The most profitable category is 'Electronics'.

### 9. Clientes com Maior Variedade de Itens

* **PT-BR:** Quais são os dois clientes, por nome e sobrenome, que compraram a maior variedade de itens distintos? Mostre também a contagem dessa variedade para cada um.
* **EN:** Which two customers, by first and last name, purchased the largest variety of distinct items? Also show the count of that variety for each.
* **Expected Answer:** Ana Silva e Carla Mendes, que compraram 3 itens distintos cada. / Ana Silva and Carla Mendes, who both bought 3 distinct items.

### 10. Itens Mais Vendidos por Quantidade

* **PT-BR:** Quais são os 3 itens mais vendidos por quantidade total?
* **EN:** What are the top 3 best-selling items by total quantity?
* **Expected Answer:** Os itens mais vendidos são 'Laptop' e 'Gaming Mouse' (3 unidades cada), seguidos por '4K Monitor' e 'Smartphone' (2 unidades cada). / The best-selling items are 'Laptop' and 'Gaming Mouse' (3 units each), followed by '4K Monitor' and 'Smartphone' (2 units each).

### 11. Receita Total por Mês

* **PT-BR:** Qual foi a receita total gerada no mês de Outubro de 2023?
* **EN:**
* **Expected Answer:** A receita total em Outubro de 2023 foi de 6816.99. / The total revenue in October 2023 was 6816.99.

### 12. Clientes Sem Pedidos

* **PT-BR:** Liste todos os clientes que nunca fizeram um pedido.
* **EN:** List all customers who have never placed an order.
* **Expected Answer:** (O agente deve indicar que não há clientes sem pedidos com base nos dados fornecidos ou retornar um resultado vazio). / (The agent should indicate that there are no customers without orders based on the provided data or return an empty result).
