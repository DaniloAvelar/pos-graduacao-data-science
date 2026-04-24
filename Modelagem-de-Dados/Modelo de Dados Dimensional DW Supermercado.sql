CREATE TABLE [dim_categoria] (
  [sk_categoria] INTEGER PRIMARY KEY,
  [cd_categoria] INTEGER NOT NULL,
  [ds_categoria] VARCHAR(45) NOT NULL
)
GO

CREATE TABLE [dim_cliente] (
  [sk_cliente] INTEGER PRIMARY KEY,
  [cd_cliente] INTEGER NOT NULL,
  [nm_cliente] VARCHAR(100) NOT NULL
)
GO

CREATE TABLE [dim_produto] (
  [sk_produto] INTEGER PRIMARY KEY,
  [cd_produto] INTEGER NOT NULL,
  [ds_produto] VARCHAR(45) NOT NULL,
  [nm_fabricante] VARCHAR(100) NOT NULL
)
GO

CREATE TABLE [dim_data] (
  [sk_data] CHAR(8) PRIMARY KEY,
  [dt_data] DATE NOT NULL,
  [num_mes] INTEGER NOT NULL,
  [num_ano] INTEGER NOT NULL
)
GO

CREATE TABLE [ft_vendas] (
  [sk_produto_vendas] INTEGER NOT NULL,
  [sk_cliente_vendas] INTEGER NOT NULL,
  [sk_data_vendas] CHAR(8) NOT NULL,
  [sk_categoria_vendas] INTEGER NOT NULL,
  [num_pedido] INTEGER PRIMARY KEY,
  [qt_produto_vendido] INTEGER,
  [vl_produto_vendido] DECIMAL(10,2)
)
GO

CREATE TABLE [ft_estoque] (
  [sk_produto_estoq] INTEGER NOT NULL,
  [sk_categoria_estoq] INTEGER NOT NULL,
  [sk_data_estoq] CHAR(8) NOT NULL,
  [qt_produto] INTEGER,
  [vl_custo] DECIMAL(10,2)
)
GO

CREATE TABLE [tmp_categoria] (
  [id_categ_tmp] INTEGER PRIMARY KEY,
  [sk_categoria_tmp] INTEGER,
  [ds_categoria_tmp] VARCHAR(45)
)
GO

CREATE TABLE [tmp_cliente] (
  [id_cliente_tmp] INTEGER PRIMARY KEY,
  [sk_cliente_tmp] INTEGER,
  [cd_cliente_tmp] INTEGER,
  [nm_cliente_tmp] VARCHAR(100)
)
GO

CREATE TABLE [tmp_produto] (
  [id_produto_tmp] INTEGER PRIMARY KEY,
  [sk_produto_tmp] INTEGER,
  [ds_produto_tmp] VARCHAR(45),
  [ds_fabricante_tmp] VARCHAR(100)
)
GO

CREATE TABLE [tmp_ft_vendas] (
  [id_ft_venda_tmp] INTEGER PRIMARY KEY,
  [sk_produto_ft_venda_tmp] INTEGER,
  [cd_produto_vendas_tmp] INTEGER,
  [sk_cliente_ft_venda_tmp] INTEGER,
  [cd_cliente_vendas_tmp] INTEGER,
  [sk_data_ft_venda_tmp] CHAR(8),
  [dt_data_venda_tmp] DATE,
  [sk_categoria_vendas_tmp] INTEGER,
  [cd_categoria_vendas_tmp] INTEGER,
  [num_pedido_vendas_tmp] INTEGER,
  [qt_produto_vendido] INTEGER,
  [vl_produto_vendido] DECIMAL(10,2)
)
GO

CREATE TABLE [tmp_ft_estoque] (
  [id_ft_estoque_tmp] INTEGER PRIMARY KEY,
  [sk_data_ft_estoque_tmp] CHAR(8),
  [data_compra_ft_estoque_tmp] INTEGER,
  [sk_produto] INTEGER,
  [cd_produto_ft_estoque_tmp] INTEGER,
  [sk_categoria_ft_estoque_tmp] INTEGER,
  [cd_categoria_ft_estoque_tmp] INTEGER,
  [qt_produto_ft_estoque_tmp] INTEGER,
  [vl_custo_ft_estoque_tmp] DECIMAL(10,2)
)
GO

ALTER TABLE [ft_vendas] ADD FOREIGN KEY ([sk_produto_vendas]) REFERENCES [dim_produto] ([sk_produto])
GO

ALTER TABLE [ft_vendas] ADD FOREIGN KEY ([sk_cliente_vendas]) REFERENCES [dim_cliente] ([sk_cliente])
GO

ALTER TABLE [ft_vendas] ADD FOREIGN KEY ([sk_data_vendas]) REFERENCES [dim_data] ([sk_data])
GO

ALTER TABLE [ft_vendas] ADD FOREIGN KEY ([sk_categoria_vendas]) REFERENCES [dim_categoria] ([sk_categoria])
GO

ALTER TABLE [ft_estoque] ADD FOREIGN KEY ([sk_produto_estoq]) REFERENCES [dim_produto] ([sk_produto])
GO

ALTER TABLE [ft_estoque] ADD FOREIGN KEY ([sk_categoria_estoq]) REFERENCES [dim_categoria] ([sk_categoria])
GO

ALTER TABLE [ft_estoque] ADD FOREIGN KEY ([sk_data_estoq]) REFERENCES [dim_data] ([sk_data])
GO
