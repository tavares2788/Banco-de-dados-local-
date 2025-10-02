import sqlite3 

conn = sqlite3.connect("banco.db")  
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas(
    cpf CHAR(12) PRIMARY KEY ,
    nome VARCHAR(40),
    idade INTEGER 
)               
''')

cpf = input("Digite seu CPF :")
nome = input("Entre com sua nome :")
idade = input("Entre com sua idade : ")


cursor.execute('''
INSERT INTO pessoas (cpf , nome , idade)
VALUES(?,?,?)''' , (cpf,nome,idade))
conn.commit()

print(f"Seus dados foram salvos com sucesso , {nome}")

cursor.execute("SELECT * FROM pessoas")
for curso in cursor:
    print(f" CPF : {cpf}  , nome : {nome} , idade :  {idade}")