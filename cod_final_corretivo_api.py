'''
Paginação

- Lado flask

import math

# Paginação
page = request.args.get('page', 1, type=int)
count_hist = Process.query.filter_by(id='corretivos_dt').count()
total_pages =  int(math(count_items / per_page))
next_page = int(page + 1)
last_page = int(page - 1)

# Query com limite de página
hist = Process.query.filter_by(id='corretivos_dt').paginate(page=page, per_page=10)

- Lado html

{% if count_item <= 10 %}

<p> {{ page }} </p>

{% else %}

{% if page == 1 %}

<i class="bi bi-chevron-left"></i>
<p> {{ page }} </p>
<a href="{{url_for('page_historico_correivos_dt', page=next_page)}}">
    <i class="bi bi-chevron-right"></i>
</a>

{% elif page == total_pages %}

<a href="{{url_for('page_historico_correivos_dt', page=last_page)}}">
    <i class="bi bi-chevron-left"></i>
</a>
<p> {{ page }} </p>
<i class="bi bi-chevron-right"></i>

{% else %}

<a href="{{url_for('page_historico_correivos_dt', page=last_page)}}">
    <i class="bi bi-chevron-left"></i>
</a>
<p> {{ page }} </p>
<a href="{{url_for('page_historico_correivos_dt', page=next_page)}}">
    <i class="bi bi-chevron-right"></i>
</a>

{% endif %}

{% endif %}

'''

'''
Caminho dos arquivos[socket main]

- Manter a consulta no banco de dados
- Quando for diferente de None, manter a lógica atual

- Quando for igual a None:

* OBS = colocar o files e file_num no ínicio de todas as funções
files = []
file_num = 0

try:
    PATH = ''
    for path, sub_path, file in os.walk(PATH):
        for file_name in file:
            PATH_JOIN = os.path.join(path, file_name)
            name_file = os.path.basename(PATH_JOIN)
            files.append(name_file)
    
    file_num = len(files)

exception:
    file_num = 0

'''

'''
Função para pausar o processo

... Lógica do código

if file_num != 0
    thread = threading.Thread(target=minha_thread)
    thread.start()

usar outro socket para receber a reposta de pausa

@socketio.on('finish_process_corretivo_dt')
def pause_process_corretivo_dt(res_pause_process):
    if res_pause_process == 'pause_process_corretivo_dt':
        print("Encerrar processo")
        pause_process = threading.Event()
        encerrar_event.set() 
        thread.join() 

'''

'''
Rodar o processo

- Manter a lógica atual

- Caso não o script, por causa do python2
process = subprocess.Popen(['python2', caminho_script_python2],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)

'''

'''
Fazer autenticação entre plataformas

- Por equanto, faz redirecionamento para tela login

'''

'''
Adicionar o domínio na aplicação

cd caminho/para/sua/aplicacao
set FLASK_APP=nome_do_seu_app.py
flask run --host=0.0.0.0 --port=5000

'''

'''

- Depois de finalizado a plataforma, deletar:
* socket_err_process
* socket_file_none
* dashboard_rasc
* start process (caso não for usar)
* verificar no qrquivos codigos e imports que não estão sendo utilizados e deletar

'''