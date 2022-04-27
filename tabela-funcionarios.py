# Edit-table
print("--------editor da tabela------")
import sqlite3
banco=sqlite3.connect("segundobanco.db")
cursor=banco.cursor()
#cursor.execute("CREATE TABLE pessoas(nome text,idade integer,email text,cpf integer)")
menu=int(input("o que gostaria de realizar:1-[registro] 2-[exclusão],3-[ATUALIZAR/alterar DADOS]"))
if menu==1:
    print("informe seu dados para ser registrado.")
    nome=str(input("digite seu nome: "))
    idade=str(input("digite sua idade: "))
    email=str(input("seu email: "))
    CPF=str("digite o seu cpf(somente numeros")
    cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"','"+CPF+"')")
    cursor.execute("SELECT*FROM Pessoas")
    banco.commit()
    print(cursor.fetchall())
elif menu==2:
    print("informe seu dados para ser deletado.")
    CPF=int(input("digite o cpf para exclusão: "))
    cursor.execute("DELETE from pessoas WHERE nome='+nome+'")
    cursor.execute("SELECT*FROM pessoas")
    banco.commit()
    print(cursor.fetchall())
    print("CPF CANCELADO")
elif menu == 3:
    att=int(input("qual dados deseja alterar:1[nome],2-[idade],3-email,4-cpf :"))
    if att==1:
        nomealt=str(input("informe qual nome que vc deseja inserir na alteracao: "))
        naltrd=str(input("quem vc deseja alterar: "))
        cursor.execute("UPDATE pessoas SET nome= '"+nomealt+"' WHERE nome= '"+naltrd+"' ")
        cursor.execute("SELECT*FROM pessoas")
        banco.commit()
        print(cursor.fetchall())
        print("dados atualizados")
    elif att==2:
            nomealt=str(input("informe qual idade que vc deseja inserir na alteracao: "))
            naltrd=str(input("digite o cpf de quem vc deseja alterar idade: "))
            cursor.execute("UPDATE pessoas SET idade= '"+nomealt+"' WHERE cpf= '"+naltrd+"' ")
            cursor.execute("SELECT*FROM pessoas")
            banco.commit()
            print(cursor.fetchall())
            print("dados atualizados")
            
    elif att==3:
            nomealt=str(input("informe qual email que vc deseja inserir na alteracao: "))
            naltrd=str(input("digite o cpf de quem vc deseja alterar  email: "))
            cursor.execute("UPDATE pessoas SET idade= '"+nomealt+"' WHERE cpf= '"+naltrd+"' ")
            cursor.execute("SELECT*FROM pessoas")
            banco.commit()
            print(cursor.fetchall())
            print("dados atualizados")
            
    elif att==4:
        nomealt=str(input("informe qual nome que vc deseja inserir na alteracao: "))
        naltrd=str(input("quem vc deseja alterar: "))
        cursor.execute("UPDATE pessoas SET nome= '"+nomealt+"' WHERE nome= '"+naltrd+"' ")
        cursor.execute("SELECT*FROM pessoas")
        banco.commit()
        print(cursor.fetchall())
        print("dados atualizados")

