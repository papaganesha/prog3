#encoding: utf-8
from connect_db import *
from consultar import *
from inserirProduto import *
from update import *

#CREATE TABLE PRODUTO( id int NOT null PRIMARY key AUTO_INCREMENT, nome varchar(100) not null, preco double not null, quantidade int not null)


#inserirProduto()

Consultar_Produtos()
Consultar_Produtos_IDfilter(2)

updateProduto()

Consultar_Produtos()