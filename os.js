/*

0. ANTES DE COMEÇAR

- Mudar as tabelas do portal de processamento para db de produção
- Mudar host db do portal de processamento para de produção

- Fazer backup de pinsprog de produção
- Copiar o portal de acompanhemento de os para versão 3
- Mudar o host do db do portal de acompanhemento  de os para de produção
- Acresentar a tabela de processamento v2

- Excluir a autenticação windows no index.js
- Exluir sistema de log dos pdfs no index.js

- Organizar as views - excluir as views das operação
- Organizar as routes - exluir os Routes e estrutura assim:
* userRoutes - login, dashboard, adicionar usuário, gerenciar
* osRoutes - 4 rotas (serachOS - Rota Dinâmica, searchOSPost, listOS, detailsOS - Rota Dinâmica)
* mapsRoutes - 4 rotas (serachMaps - Rota Dinâmica, searchMapsPost, listMaps, detailsMaps - Rota Dinâmica)
* plainRoutes - 4 rotas (serachPlains, searchPlainsPost, listPlains, detailsPlains)

- Organizar os controllers - excluir atual e seguir a lógica das rotas

- Organizar as rotas no index js

1. AUTENTICAÇÃO

- Instalar o pacote
npm install windows-authentication

- Lógica:
static loginPost(req, res) {
    const { user, password } = req.body;

    const queryUserAutorizade = User.findOne({where: {username = user}})

    const userAutorizade = queryUserAutorizade.dataValues.user

    autorizade = false

    if (!user) {
      res.render('auth/login', {
        message: 'Usuário não encontrado!',
      })

      return
    }

    windowsAuthentication
        .authenticate(user, password)
        .then((result) => {
            if(result) {
                console.log('Autorizado')
                autorizade = true
            } else {
                console.log('Não Autorizado')
            }
        })
        .cath((error) => {
            console.error('Erro de autenticação:', error);
        })
    
    if(aurorizade === true && user === userAutorizade) {
        req.session.userid = user.id
        req.session.user = queryUserAutorizade.dataValues.user
        req.session.matricula = queryUserAutorizade.dataValues.matricula
        req.session.display = true

        req.flash('message', 'Login realizado com sucesso!')

        req.session.save(() => {
            res.redirect('/dashboard')
        })

    } else {
        console.log('Usuário não autorizado')
    }
}

2. MAIN

* Passar as informação para main
{{user}}
{{matricula}}
{{userid}}
{{display}}

3. MENU

- Itens do menu:
* Listagens da OS
* Listagens dos Mapas
* Listagens das Planilhas
* Adicionar Usuário
* Exclusão e Listagem de Usuário
* Em destaque (Logout)

HTML
OBS: colocar script no main, com atributo defer
<a onclick=menuActivate>Menu Hamburguer</a>
<menu id="menuMain"></menu>

CSS
#menuMain {
    display: none
}

JS
const onClick = () => {
    if (menuMain.style.display == 'block') {
        menuMain.style.display = 'none'
    } else {
        menuMain.style.display = 'block'
    }
}

4. Dashboard

HTML
Copiar a estrutura do portal de processamento

CSS:
Copiar estilo do portal de processamento

Backend
Mudar para servidor de produção (lembrar de fazer backup antes)
* Primeira parte - manter
* CARD 1 - Ultimas OS
* CARD 2 - Ultimas aplicação maturador
* CARD 3 - Ultima aplicação de herbicida
* CARD 4 - Últimos Mapas linkados

5. Listagens da OS

* Exportar as tabelas do servidor de teste para produção do painel de processamento
* Mudar as configuração na aplicação

*Página consulta*

# Lado HTML
- Copiar a estrutura e estilo do configurador de ambiente do painel de processamento
- Usar de forma dinâmica
- Usar if e else para aparecer somente a numero da os ou busca geral

# Lado do Backend
static searchOS(req, res) {
    const id = req.params.id
    res.render('os/searchOS', {id})
}

static searchOSpost(req, res) {
    const id = req.params.id

    if(id === 'search_all') {
        const { operacao, status } = req.body

        req.session.operacao = operacao
        req.session.status = status

        req.session.save(() => {
        res.redirect('/os/results')
        }
    } else {
        const { num_os } = req.body
        req.session.num_os = num_os

        req.session.save(() => {
        res.redirect('/os/results_items/num_os')
        }
    }

}

*Página de Resultado*

# Lado do backend
static os(req, res){
    const operacao = req.session.operacao
    const status = req.session.status

    const cod_operacao = operacao.split(' - ')[1]

    if(status == Todos) {
        // Lógica que está sendo usada para consulta

        // Paginação

        // Se está vazio

        res.render('os/list', {os, paginate, empty})
    } else if(status == Fechado) {
        // Lógica que está sendo usada para consulta

        // Paginação

        // Se está vazio

        res.render('os/list', {os, paginate, empty})
    } else {
        // Lógica que está sendo usada para consulta

        // Paginação

        // Se está vazio

        res.render('os/list', {os, paginate, empty})
    }
}

# Lado do HTML
- Colocar Título da Consulta
- Usar a estilização da lisatgem atual
- Titulo de cada item é o numero da OS
- Colocar data de entrada
- Colocar a data de saída
- Botão para acessar a OS completa

*Página Individual da OS*

# Lado do backend
statis detailsOS(req, res) {
    const num_os = req.params.id

    // Consulta para bd das OS (Usar logica para agrupar e interar produtos em uma lista)
    const user = await OS.findOne({ where: { no_os: num_os } })

    // Consulta bd do Processamento
    const user = await Process.findOne({ where: { no_os: num_os } })

    res.render('os/list', {os, process})
}

# Lado do HTML
- Colocar Título da Consulta
- Interar os produtos
- Colocar as informações da listagem atual
- Colocar status do processamento

6. Listagens dos Mapas

OBS:
- Instalar: npm install express pdfjs-dist
- Usar no controller:
const path = require('path');
const fs = require('fs');

*Página consulta*

# Lado HTML
- Copiar a estrutura e estilo do configurador de ambiente do painel de processamento
- Usar de forma dinâmica
- Usar if e else para aparecer somente a numero da os ou busca geral

# Lado do Backend
static searchOS(req, res) {
    const id = req.params.id
    res.render('os/searchOS', {id})
}

static searchOSpost(req, res) {
    const id = req.params.id

    if(id === 'search_all') {
        const { operacao, unidade, piloto } = req.body

        req.session.operacao = operacao
        req.session.unidade = unidade
        req,session,piloto = piloto

        req.session.save(() => {
        res.redirect('/os/results')
        }
    } else {
        const { num_os } = req.body
        req.session.num_os = num_os

        req.session.save(() => {
        res.redirect('/os/results_items/num_os')
        }
    }

}

*Página de Resultado*

# Lado do backend
static os(req, res){
    const operacao = req.session.operacao
    const unidade = req.session.unidade
    const piloto = req.session.piloto

    const sepOperacao = operacao.split(' - ')
    const aplicacao = sepOperacao[1]
    const empresa = sepOperacao(' - ')[2]

    //  Lista de arquivos
    folder = Caminho dos PDS
    const files = fs.readdirSync(folder)
    files.filter(file => file.endsWith('.pdf'))

    res.render('maps/maps', {files})
}

# Lado do HTML
- Sequir o estilo e estrurura da consulta das OS

*Página Individual dos*
static listMaps(req, res) {
    const { filename } = req.params;
    const filePath = path.join(__dirname, 'pdfs', filename);

    const data = fs.readFileSync(filePath);
    res.contentType('application/pdf');
    res.send(data);
}

7. Listagens das Planilhas

OBS:
- Instalar: npm install xlsx
- Usar no controller:
const path = require('path');
const fs = require('fs');
const xlsx = require('xlsx');

*Página consulta*

# Lado HTML
- Copiar a estrutura e estilo do configurador de ambiente do painel de processamento
- Usar de forma dinâmica
- Usar if e else para aparecer somente a numero da os ou busca geral

# Lado do Backend
static searchOS(req, res) {
    const id = req.params.id
    res.render('os/searchOS', {id})
}

static searchOSpost(req, res) {
    const id = req.params.id

    if(id === 'search_all') {
        const { operacao, unidade, piloto } = req.body

        req.session.operacao = operacao
        req.session.unidade = unidade
        req.session.piloto = piloto

        req.session.save(() => {
        res.redirect('/os/results')
        }
    } else {
        const { num_os } = req.body
        req.session.num_os = num_os

        req.session.save(() => {
        res.redirect('/os/results_items/num_os')
        }
    }

}

*Página de Resultado*

# Lado do backend
static os(req, res){
    const operacao = req.session.operacao
    const unidade = req.session.unidade
    const piloto = req.session.piloto

    const sepOperacao = operacao.split(' - ')
    const aplicacao = sepOperacao[1]
    const empresa = sepOperacao(' - ')[2]

     //  Lista de arquivos
    folder = Caminho dos PDS
    const files = fs.readdirSync(folder)
    files.filter(file => file.endsWith('.xlsx') || file.endsWith('.xls'))

    res.render('maps/maps', {files})
}

# Lado do HTML
- Sequir o estilo e estrurura da consulta das OS

*Página Individual dos*
static listMaps(req, res) {
    const { filename } = req.params;
    const filePath = path.join(__dirname, 'excels', filename);

    const workbook = xlsx.readFile(filePath);
    const sheetName = workbook.SheetNames[0]; // Assume que estamos lendo a primeira planilha
    const excelData = xlsx.utils.sheet_to_json(workbook.Sheets[sheetName]);

    res.json(excelData);
}

8. Adicionar Usuário

* Verifcar se está funcionando

9. Exclusão e Listagem de Usuário

*  Verificar se está funcionado

10. Deploy no servidor

"start": "nodemon ./index.js dtgeo200 3100"

*/