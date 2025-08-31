from dao.db import get_connection

class UserModel:
    @staticmethod
    def get_user_by_email(email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        return user
