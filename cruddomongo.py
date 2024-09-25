import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['contatos_db'] 
contatos_collection = db['contatos']  

def criar_contato(nome, telefone, email=None):
    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    contatos_collection.insert_one(contato)
    return f"Contato '{nome}' criado com sucesso!"

def listar_contatos():
    contatos = contatos_collection.find()
    contatos_list = []
    
    for contato in contatos:
        detalhes = f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato.get('email', 'N/A')}"
        contatos_list.append(detalhes)
    
    return contatos_list if contatos_list else ["Nenhum contato encontrado."]

def atualizar_contato(nome, novo_telefone=None, novo_email=None):
    contato = contatos_collection.find_one({"nome": nome})
    
    if contato:
        update_fields = {}
        
        if novo_telefone:
            update_fields['telefone'] = novo_telefone
        if novo_email:
            update_fields['email'] = novo_email
        
        if update_fields:
            contatos_collection.update_one({"nome": nome}, {"$set": update_fields})
            return f"Contato '{nome}' atualizado com sucesso!"
        else:
            return "Nenhuma atualização foi feita."
    else:
        return f"Contato com nome '{nome}' não encontrado."

def deletar_contato(nome):
    result = contatos_collection.delete_one({"nome": nome})
    
    if result.deleted_count > 0:
        return f"Contato '{nome}' deletado com sucesso!"
    else:
        return f"Contato com nome '{nome}' não encontrado."