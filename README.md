## Manual de reprodução da atividade de Rede Complexas.

Neste repositório encontra-se a atividade 1 de redes complexas. Os algoritimos
implementados estão todos dentro do script grafo.py.

### Dependências e configuração do ambiente

Dependências resolvidas com o pip estão contidas no arquivo pip-r.txt

Dependências resolvidas com o apt (Debian, Ubuntu e Linux Mint, etc...) estão
contidas no arquivo req.txt

#### As dependências devem ser instaladas para o funcionamento correto do algoritmo.

### instalação dos pacotes pip via virtualenv

#### A instalação do pacote python3-venv pode ser necessária caso ainda não esteja intalado.

Criando ambiente virtual

$ python3 -m venv env

Ativando ambiente virtual

$ source env/bin/activate

Instalando o pacote wheel (para instalação dos demais pacotes com extensão .whl)

$ python -U wheel

Instalando as dependências do pip

$ python -Ur -install pip-r.txt

### Execução

Com o ambiente virtual ativado: $ source env/bin/activate

$ python grafo.py

### Base de dados utilizadas retiradas de http://www-personal.umich.edu/~mejn/netdata/

1. Political Blogs
2. Books Abouts US Politics (Padrão configurada no construtor do script).
3. Condensed matter collaborations 1999
4. Condensed matter collaborations 2003
5. Condensed matter collaborations 2005

### Saída do script

O script executa os algoritimos e por consequente as análises de acordo com a ordem de demandas
da lista de exercícios. Todas as informações são imprimidas diretamente na tela.
O plot da rede é armazenado em PDF no caminho plots/rede.pdf. Ao lugar de colocar o grau
como número associado ao vértice, preservei o nome do livro (base de dados 2) e adicionei
o grau do vértice ao parâmetro "size". Logo vértices com grau maior possuem tamanho maior
no plot da rede.
