from dao.db import get_connection

class UserModel:
    @staticmethod
    def get_user_by_email(email: str):
        """
        Retorna dados do usuário vinculado ao funcionário com o e-mail informado
        """
        conn = get_connection()
        cur = conn.cursor()

        sql = """
        SELECT u.id_usuario, u.senha_hash, u.ativo, f.id_funcionario, f.nome_completo, f.email
        FROM usuarios u
        JOIN funcionarios f ON f.id_funcionario = u.id_funcionario
        WHERE f.email = ? AND u.ativo = 1
        """
        cur.execute(sql, (email,))

        row = cur.fetchone()
        conn.close()
        return dict(row) if row else None
