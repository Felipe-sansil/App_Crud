from Banco import Banco

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("""
                INSERT INTO usuarios (nome, telefone, email, usuario, senha)
                VALUES (?, ?, ?, ?, ?)
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha))

            banco.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            print(str(e))
            return "Ocorreu um erro ao cadastrar o usuário"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("""
                UPDATE usuarios
                SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?
                WHERE idusuario = ?
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))

            banco.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except Exception as e:
            print(str(e))
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("DELETE FROM usuarios WHERE idusuario = ?", (self.idusuario,))

            banco.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except Exception as e:
            print(str(e))
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, search_param):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            # Verifica se o parâmetro de busca é um número (idusuario) ou uma string (nome)
            if search_param.isdigit():
                c.execute("SELECT * FROM usuarios WHERE idusuario = ?", (search_param,))
            else:
                c.execute("SELECT * FROM usuarios WHERE nome LIKE ?", ('%' + search_param + '%',))

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            c.close()

            return "Busca feita com sucesso!"
        except Exception as e:
            print(str(e))
            return "Ocorreu um erro na busca"
        
    # Adicione este método à sua classe Usuarios
    def selectAllUsers(self):
        banco = Banco()
        lista_usuarios = []

        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios")

            for linha in c.fetchall():
                usuario_info = f"ID: {linha[0]}, Nome: {linha[1]}, Telefone: {linha[2]}, Email: {linha[3]}, Usuário: {linha[4]}, Senha: {linha[5]}"
                lista_usuarios.append(usuario_info)

            c.close()
        except Exception as e:
            print(str(e))

        return lista_usuarios


            
