import sqlite3

class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                telefone TEXT,
                email TEXT,
                usuario TEXT,
                senha TEXT
            )
        """)
        self.conexao.commit()
        c.close()

    def closeConnection(self):
        if self.conexao:
            self.conexao.close()

    def commit(self):
        if self.conexao:
            self.conexao.commit()
