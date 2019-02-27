#!/usr/bin/env python2
# encoding: utf-8

# Importar psycopg2 para conectar-se ao Database
import psycopg2

# Aplicar uma função para chamada posterior do Database
DBNAME = "news"


def executar_db(query):

    """Conectar-se ao banco de dados, e executar a pesquisa
    retornando os resultados"""
    try:
        db = psycopg2.connect('dbname=' + DBNAME)
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e.pgerror)
        print(e.diag.message_detail)
        sys.exit(1)

    c = db.cursor()

    c.execute(query)

    rows = c.fetchall()

    db.close()

    return rows

# Perguntas e Respostas


def artigos_mais_visualizados():

    # Construindo a query
    query = """
        select articles.title, count(log.path) as num
        from log join articles
        on log.path = CONCAT('/article/', articles.slug) where 
        log.status = '200 OK' 
        group by articles.title 
        order by num Desc limit 3;
    """

    # Executando a query

    results = executar_db(query)

    # Função para imprimir os resultados de 'def artigos_mais_visualizados()':

    print('Os três artigos mais populares de todos os tempos são: \n')

    count = 1

    for i in results:

        number = '(' + str(count) + ') "'

        title = i[0]

        views = '" com ' + str(i[1]) + " visualizações"

        print(number + title + views)

        count += 1


def autores_mais_populares():

    # Construindo a query
    query = """
        select authors.name, count(log.path) as num
        from articles join authors
        on articles.author = authors.id
        join log on log.path like CONCAT('/article/', articles.slug) where
        log.status = '200 OK'
        group by authors.name
        order by num Desc limit 3;
    """

    # Executando a query

    results = executar_db(query)

    # Função para imprimir os resultados de 'def autores_mais_populares()':

    print('Os autores mais populares de todos os tempos são: \n')

    count = 1

    for i in results:

        print('(' + str(count) + ') ' + i[0] + ' com ' + str(i[1]) +
              " visualizações")

        count += 1


def dias_com_mais_de_1_por_cento_de_erro():

    # Construindo a query

    query = """
        select to_char(time::date, 'Month DD,YYYY'),
        (count(case when status != '200 OK' then 1 end)*100)::float/
        count(*) as num from log 
        group by time::date 
        order by num desc limit 1;
        
    """

    # Executando a query

    results = executar_db(query)

    # Função para imprimir os resultados de:
    # 'def dias_com_mais_de_1_por_cento_de_erro()':

    print('Em quais dias mais de 1% das requisições resultaram'
          'em erros? \n')

    for i in results:

        date = i[0]

        errors = str(round(i[1], 1)) + "%" + " erros"

        print(date + " -- " + errors)

# Imprimindo resultados no terminal

print('Resultado da Pesquisa:')
print('____________________________________')
artigos_mais_visualizados()
print('____________________________________')
autores_mais_populares()
print('____________________________________')
dias_com_mais_de_1_por_cento_de_erro()
