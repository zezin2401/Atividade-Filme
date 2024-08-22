from flask import Flask, render_template, request, redirect, url_for

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Lista para armazenar os filmes
filmes = []


@app.route('/', methods=['GET', 'POST'])
def index():
    # Verifica o método da solicitação
    if request.method == 'POST':
        # Obtém o nome e o gênero do filme do formulário
        filme_nome = request.form.get('filme')
        filme_genero = request.form.get('genero')

        # Adiciona o filme à lista se ambos os campos estiverem preenchidos
        if filme_nome and filme_genero:
            filmes.append({'nome': filme_nome, 'genero': filme_genero})

        # Redireciona para a rota de lista de filmes
        return redirect(url_for('list_filmes'))

    # Renderiza o template de adição de filmes
    return render_template('index.html')


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    # Verifica se o índice é válido
    if index < 0 or index >= len(filmes):
        # Redireciona para a lista de filmes se o índice for inválido
        return redirect(url_for('list_filmes'))

    # Verifica o método da solicitação
    if request.method == 'POST':
        # Obtém os novos valores do formulário
        novo_nome = request.form.get('filme')
        novo_genero = request.form.get('genero')

        # Atualiza o filme na lista se ambos os campos estiverem preenchidos
        if novo_nome and novo_genero:
            filmes[index] = {'nome': novo_nome, 'genero': novo_genero}

        # Redireciona para a rota de lista de filmes
        return redirect(url_for('list_filmes'))

    # Renderiza o template de edição de filme com os dados do filme atual
    return render_template('edit.html', index=index, filme=filmes[index])


@app.route('/list')
def list_filmes():
    # Renderiza o template de lista de filmes
    return render_template('list.html', filmes=filmes)


@app.route('/delete/<int:index>', methods=['GET', 'POST'])
def delete(index):
    # Verifica se o índice é válido
    if index < 0 or index >= len(filmes):
        # Redireciona para a lista de filmes se o índice for inválido
        return redirect(url_for('list_filmes'))

    # Verifica o método da solicitação
    if request.method == 'POST':
        # Remove o filme da lista pelo índice
        filmes.pop(index)
        # Redireciona para a rota de lista de filmes
        return redirect(url_for('list_filmes'))

    # Renderiza o template de confirmação de exclusão com os dados do filme
    return render_template('confirm_delete.html', index=index, filme=filmes[index])


if __name__ == '__main__':
    # Executa a aplicação Flask em modo de depuração se o script for executado diretamente
    app.run(debug=True)
