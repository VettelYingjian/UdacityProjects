#!/usr/bin/env python3

import psycopg2

DBNAME = 'news'


def count_most_read_article():
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("""select count(log.path) as totalViews, articles.title, authors.name
        from log, articles, authors
        where log.path != '\'
        and articles.slug = substr(log.path, length('/article/')+1)
        and articles.author = authors.id
        group by articles.title, authors.name
        order by totalViews desc
        limit 3;""")
    posts = cur.fetchall()
    conn.close()
    return posts


def print_most_read_article():
    print("The top 3 most viewed articles are:")
    for item in count_most_read_article():
        print("'" + str(item[1]) + "'" + ", by the author " +
              str(item[2] + " with %d views" % int(item[0])))


def count_most_read_author():
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("""select count(authors.name) as total, authors.name
        from log, articles, authors
        where log.path != '\'
        and articles.slug = substr(log.path, length('/article/')+1)
        and articles.author = authors.id
        group by authors.name
        order by total desc;""")
    posts = cur.fetchall()
    conn.close()
    return posts


def print_most_read_author():
    print("The most popular authors of all time are:")
    for items in count_most_read_author():
        print(str(items[1]) + ' -- ' + str(items[0]) + ' views')


def count_errors():
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()
    cur.execute("""
        select concat(round(statuslog.errorRate,1),'%') as errorPercentage,
        to_char(statuslog.errorDate, 'Month DD, YYYY') as date
        from
        (
        select date(log.time) as errorDate,
        (sum(case when substr(log.status,1,3)::integer >= 400
        then 1
        else 0
        end
        ) * 100)::decimal /
        count(log.status) as errorRate
        from log group by errorDate)
        as statuslog
        group by statuslog.errorDate, statuslog.errorRate
        having round(statuslog.errorRate,1) > 1
        """)
    posts = cur.fetchall()
    conn.close()
    return posts


def print_count_errors():
    print("The most popular authors of all time are:")
    for items in count_errors():
        print(str(items[1]) + ' -- ' + str(items[0]) + ' errors')


if __name__ == '__main__':
    print_most_read_article()
    print('\n')
    print_most_read_author()
    print('\n')
    print_count_errors()
    
