from pathlib import Path
import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

BANCO = Path(__file__).with_name('servimatch.db')

def iniciar_banco():
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute('''
            CREATE TABLE IF NOT EXISTS profissionais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                servico TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        ''')
        quantidade = conexao.execute(
            'SELECT COUNT(*) FROM profissionais'
        ).fetchone()[0]
        if quantidade == 0:
            conexao.executemany(
                'INSERT INTO profissionais (nome, servico, cidade) VALUES (?, ?, ?)',
                [
                    ('Ana Souza', 'Eletricista', 'Valença'),
                    ('João Santos', 'Encanador', 'Valença'),
                    ('Marina Costa', 'Técnica de informática', 'Cairu')
                ]
            )


@app.route('/')
def inicio():
    
    return render_template('index.html')


if __name__ == '__main__':
    iniciar_banco()
    app.run(host='127.0.0.1', port=5000, debug=False)
