from flask import Blueprint
#definindo rota de blueprint para autenticação de usuário
auth = Blueprint('auth', __name__)

from . import views