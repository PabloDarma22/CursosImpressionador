from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario, Post

#
with app.app_context():
    database.drop_all()
    database.create_all()

with app.app_context():
    Usuario.query.all()
    meus_usuarios = Usuario.query.first()
