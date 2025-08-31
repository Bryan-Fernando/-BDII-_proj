import os

class Config:
    #SECRET_KEY = os.environ.get("SECRET_KEY", "chave-secreta-dev")
    DATABASE = os.path.join(os.getcwd(), "instance", "ifro_requests.db")
