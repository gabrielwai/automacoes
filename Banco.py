from sqlite3.dbapi2 import connect


class Banco():

    #def __conectar(self):
        #pass    

    def query(self, query):
        conn = connect('./sqlite/jfmartins-adp.db')
        curs = conn.cursor()

        #curs.execute("insert into contas values ('usuario_3', 'senha_3', 'BRASILSEG');")
        #conn.commit()

        curs.execute(query)
        response = curs.fetchall()
        #for usuario, senha, empresa in curs.fetchall():
        #    print(usuario, senha, empresa)
        conn.close()
        print(response)
        return response


    def insert(self, comando):
        conn = connect('./sqlite/jfmartins-adp.db')
        curs = conn.cursor()

        curs.execute(str(comando))
        conn.commit()
        conn.close()
