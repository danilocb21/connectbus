# Connect Bus
Connect Bus - Serviço de Ouvidoria do Transporte Público da sua cidade.

## Projeto
A primeira parte do projeto consiste na criação de um sistema de ouvidoria em que os usuários possam enviar reclamações e/ou sugestões de melhorias para a prefeitura em relação ao transporte público local.  
Para isto, utilizaremos **HTML/CSS e JavaScript** para desenvolver o Front-End e o FrameWork **Django** com o SGBD **PostgreSQL** para o Back-End.  
(Continuação do projeto feito anteriormente)

# Tutorial - Instalação
## Python
Para rodar o programa, é necessário a instalação do **Python** e algumas dependências.  
Neste projeto, a versão utilizada é a ***3.11.6***  
Baixe aqui: https://www.python.org/downloads/release/python-3116/

## PostgreSQL
O banco de dados utilizado no projeto é o **PostgreSQL**. A versão utilizada é a ***16.1***  
Para administrá-lo, precisamos do **pgadmin**.  
Baixe aqui: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

## PowerShell
Por padrão, o PowerShell não permite a execução de scripts via linha de comando. Para permitir, é necessário alterar as políticas de restrição.  
Abra o powershell como administrador e execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
```

## Django
Após copiar o diretório utilizando o git clone, faça o ambiente virtual e o habilite. Depois entre na pasta da aplicação.
```bash
python -m venv env
env/Scripts/activate
cd transporte
```
Após ativar o ambiente virtual, instale as depedências que serão utilizadas no programa.
```bash
pip install -r requirements.txt
```
Agora, o ambiente está pronto para ser desenvolvido. Para iniciar o servidor, execute:
```bash
python .\manage.py runserver
```

## VSCode
A IDE ideal para o desenvolvimento do projeto é o Visual Studio Code.  
Algumas funcionalildades úteis é que ele pode ativar o ambiente virtual automaticamente e mostrar intellisense para o django.  
Criem uma pasta chamada ".vscode" e crie um arquivo "settings.json". Nele cole isso:
```json
{
    "python.terminal.activateEnvironment": true,
    "python.defaultInterpreterPath": "${workspaceFolder}\\env\\Scripts\\python.exe",
}
```
Além disso, baixem a extensão Django. Ela pode bagunçar o autocomplete do VScode, mas isto é solucionado bem simples.
- [ ] Abra as configurações do VSCode (Ctrl + ,)
- [ ] Clique em Extensions e vá até **Emmet**
- [ ] Em Emmet, ache **Include Languages** e adicione o item:
 django-html | html 

## Materiais úteis
https://docs.djangoproject.com/en/5.0/  
https://getbootstrap.com/docs/5.3/getting-started/introduction/  
https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8  
https://www.youtube.com/watch?v=sm1mokevMWk

## Git
Commands needed to run in git until then:
## Create a local and remote repository and first commit

| Command  | Action |
| --------| ------ |
| git init| Initialize the repository|
| git status | Shows the status of files in the folder|
| git add `path file` or `.` | To place a file in the staging area|
| git add `path file` or `.` | To put all files in the staging area|
| git commit -m "`any name`" | To add commit in the repository|
| git branch -M "main" | To change the name of the main branch from master to main|
| git remote add origin `remote repository link` | To link local repository to remote repository|
| git push -u origin `branch name` | To push to remote repository|

> OBS: To Refresh branch => add, commit and push (without "-u").

## Others Commands

| Command  | Action |
| --------| ------ |
| git checkout -b "`new branch`" | Create and log in a new branch |
| git checkout `branch existing` | Transition between branches |
| git merge `branch merge` | Join two branches |
| git clone `link to clone` | Pull a project on your machine |
| cd `name folder` | Log in the project |
| git pull | Update clone |
| git fetch origin `name branch` | Find all recent updates in branch |
| git reset --hard origin/`name branch` | Reset all in the current branch |
| git push -f origin `name branch` | Force all updates |
## Dictionary
- Fork => Pull a project to your remote repository;
- Pull Request => Asks the project owner to change the product;

## Copyright
&copy; 2024 Danilo C Beuttenmuller. All rights reserved.
