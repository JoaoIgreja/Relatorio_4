from database import Database
db = Database(database="mercado", collection="compras")
db.resetDatabase()
dataset = db.collection.find()


def Total_de_vendas_em_um_dia(data):
    return db.collection.aggregate([
        # Filtra documentos para a data desejada
        {"$match": {"data_compra": data}},
        {"$unwind": "$produtos"},
        {"$group": {"_id": None, "total_vendas": {
            "$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    ])


def Produto_mais_vendido():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "total_vendido": {
            "$sum": "$produtos.quantidade"}}},
        {"$sort": {"total_vendido": -1}},  # Classificar em ordem decrescente
        {"$limit": 1}
    ])


def Cliente_que_mais_gastou_em_uma_unica_compra():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": {"cliente": "$cliente_id", "compra": "$_id"},
                    "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        {"$sort": {"total": -1}},
        {"$group": {"_id": "$_id.compra", "cliente": {
            "$first": "$_id.cliente"}, "total": {"$first": "$total"}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}
    ])


def Lista_de_produtos_que_tiveram_uma_quantidade_vendida_acima_de_1_unidades():
    return db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "total_vendas": {"$sum": 1}}},
        {"$match": {"total_vendas": {"$gte": 1}}}
    ])
