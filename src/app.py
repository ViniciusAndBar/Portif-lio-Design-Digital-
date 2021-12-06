from flask import app, Flask, render_template

minha_app = Flask(__name__)

@minha_app.route('/')
def home():
    return render_template('sobre mim.html', tittle='sobre mim')

@minha_app.route('/Interesses')
def interesses():
    return render_template('Interesses.html', tittle='interesses')

@minha_app.route('/Trabalhos')
def trabalhos():
    return render_template('Trabalhos Desenvolvidos.html', tittle='trabalhos desenvolvidos')

if __name__ == '__main__':
    minha_app.run('0.0.0.0')