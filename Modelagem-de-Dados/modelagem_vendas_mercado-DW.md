# Projeto de Modelagem: Data Warehouse de Vendas e Estoque

Este projeto apresenta a modelagem de um Data Warehouse (DW) utilizando a arquitetura **Star Schema**, desenvolvida como parte dos estudos da pós-graduação.

## 🎯 Objetivos
* Implementar uma camada de **Staging** para recepção de dados brutos.
* Garantir a integridade histórica utilizando **Surrogate Keys (SK)**.
* Estruturar tabelas de Fato e Dimensões para otimização de consultas analíticas.

## 🛠️ Ferramentas Utilizadas
* **dbdiagram.io** para modelagem lógica.
* **SQL Server** (SSMS) como motor de banco de dados pretendido.

## 📐 Diagrama do Modelo
![Diagrama de Vendas](./diagrama_vendas.png)

## 🧠 Conceitos Aplicados
1. **Star Schema:** Centralização das tabelas de fato (`ft_vendas`, `ft_estoque`) conectadas a dimensões padronizadas.
2. **Área de Staging:** Uso de tabelas temporárias (`tmp_`) para o processo de ETL, separando o dado transacional do dado analítico.
3. **Tipagem de Chaves:** Uso de SKs para evitar dependência direta dos IDs dos sistemas de origem.
