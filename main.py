from writeAJson import writeAJson
from database import Database

from ProductAnalyzer import *

result = Total_de_vendas_em_um_dia("2022-03-14")
writeAJson(result, "Total_de_vendas_em_um_dia")

result1 = Produto_mais_vendido()
writeAJson(result1, "Produto_mais_vendido")

result2 = Cliente_que_mais_gastou_em_uma_unica_compra()
writeAJson(result2, "Cliente_que_mais_gastou_em_uma_unica_compra")

result3 = Lista_de_produtos_que_tiveram_uma_quantidade_vendida_acima_de_1_unidades()
writeAJson(
    result3, "Lista_de_produtos_que_tiveram_uma_quantidade_vendida_acima_de_1_unidades")
