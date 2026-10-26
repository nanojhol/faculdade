"""
Sweet Cupcake Gourmet — Aplicação Web em Flask (Padrão MVC)
Projeto Integrador Transdisciplinar em Engenharia de Software II (Turma_001)

Camada Principal de Inicialização e Configuração
"""

import os
from flask import Flask, render_template
from controllers.routes import routes_bp
from models.database import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'pit2-confeitaria-gourmet-segredo-chave-2026')

# Registra o controlador de rotas (Controller)
app.register_blueprint(routes_bp)

# Garante que as tabelas SQLite (3FN) e dados iniciais existam
with app.app_context():
    init_db()


# Tratamento de Erros Amigável (Conforme requisito do PIT II p. 34)
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template(
        'base.html',
        error_title="Página não encontrada (404)",
        error_msg="O endereço solicitado não foi localizado em nossa confeitaria."
    ), 404


@app.errorhandler(500)
def erro_interno_servidor(e):
    return render_template(
        'base.html',
        error_title="Instabilidade Temporária (500)",
        error_msg="Ocorreu uma instabilidade interna ao processar seu pedido. Tente novamente em instantes."
    ), 500


if __name__ == '__main__':
    # Inicialização para testes em ambiente local
    porta = int(os.environ.get('PORT', 5000))
    print(f"🧁 Confeitaria Sweet Cupcake rodando localmente em: http://127.0.0.1:{porta}")
    app.run(host='0.0.0.0', port=porta, debug=True)
