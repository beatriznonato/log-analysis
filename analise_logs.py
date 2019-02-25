#!/usr/bin/env python2

# Importar psycopg2 para conectar-se ao Database
import psycopg2

# Aplicar uma função para chamada posterior do Database
DBNAME = "news"


def executar_db(query):

    """Conectar-se ao banco de dados, e executar a pesquisa
    retornando os resultados"""

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
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
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
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
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
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """

    # Executando a query

    results = executar_db(query)

    # Função para imprimir os resultados de:
    # 'def dias_com_mais_de_1_por_cento_de_erro()':

    print('Em quais dias mais de 1% das requisições resultaram'
          'em erros? \n')

    for i in results:

        date = i[0].strftime('%B %d, %Y')

        errors = str(round(i[1]*100, 1)) + "%" + " erros"

        print(date + " -- " + errors)

# Imprimindo resultados no terminal

print('Resultado da Pesquisa:')
print('____________________________________')
artigos_mais_visualizados()
print('____________________________________')
autores_mais_populares()
print('____________________________________')
dias_com_mais_de_1_por_cento_de_erro()
