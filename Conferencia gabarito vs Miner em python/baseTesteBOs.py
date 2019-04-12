# Cria uma conexão com SQLite
from datetime import date
import sqlite3
conn = sqlite3.connect('baseTestDipol.db')
c = conn.cursor()
class BaseTesteBOsDAO:
  
#select na base dos BOs
    def baseBOs(self):
# Criando um cursor SQLite

        c.execute ("SELECT * FROM baseTesteBOs")
        retornoSql = c.fetchall()
        c.close
        return retornoSql


# Função para criar uma tabela
    def gravaBOs(self,conteudo):
        data_atual = date.today()
        novaData = data_atual.strftime('%d/%m/%Y')

        c.execute('CREATE TABLE IF NOT EXISTS "resultTesteBOsNova" (data_exec	TIMESTAMP,delegacia INTEGER not null,ano INTEGER not null,numero INTEGER not null,\
            nAutor VARCHAR(5) not null default "NP", nAutorAcaoFugir VARCHAR(5) not null default "NP",nAutorAcaoAbordagem VARCHAR(5) not null default "NP",\
            nQtdeAutor VARCHAR(5) not null default "NP", nAutorArma VARCHAR(5) not null default "NP", nAutorSubtrair VARCHAR(5) not null default "NP",\
            nAutorAcaoAgressao VARCHAR(5) not null default "NP", nAutorAcaoCoacao VARCHAR(5) not null default "NP", nArmaBranca VARCHAR(5) not null default "NP",\
            similares INTEGER not null)')

# Função para inserir uma linha
        listaDb = []
        for i in conteudo:
            a = []
            bro = []
            bro.append(novaData)
            a += (bro+i)
            listaDb.append(a)
        c.executemany("""
        INSERT INTO resultTesteBOsNova (data_exec, delegacia, ano, numero, nAutor,nAutorAcaoFugir, nAutorAcaoAbordagem, nQtdeAutor, nAutorArma, nAutorSubtrair,\
                    nAutorAcaoAgressao, nAutorAcaoCoacao, nArmaBranca, similares)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, listaDb)
        # gravando no bd
        conn.commit()
        print("Dados inseridos da lista com sucesso: %s registros." %len(conteudo))
        c.close()
    
    def atualizaSimilares(self,lista):
        try:
            c.execute('ALTER TABLE resultTesteBOs ADD COLUMN similares INTEGER;')
        except:
            pass # handle the error

        conn.commit()

        print('Novo campo adicionado com sucesso.')
#inserir o numero de similares
        for i in lista:
            c.execute("""
            UPDATE resultTesteBOs1 SET similares = ? WHERE delegacia = ? and ano = ? and numero = ?
            """, i[3],i[0],i[1],i[2])