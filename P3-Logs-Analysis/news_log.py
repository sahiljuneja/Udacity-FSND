#!/usr/bin/env python3

import psycopg2
import argparse


def popular_articles():
    """Returns top 3 most accessed articles"""
    db = psycopg2.connect(database="news")
    cur = db.cursor()
    cur.execute("SELECT articles.id, articles.title, count(articles.id) \
                AS num FROM articles, log WHERE articles.slug LIKE \
                (split_part(log.path,'/', 3)) GROUP BY articles.id \
                ORDER BY num DESC LIMIT 3;")
    result = [row[1:3] for row in cur.fetchall()]
    db.close()
    return result


def popular_authors():
    """Returns authors with most article views combined"""
    db = psycopg2.connect(database="news")
    cur = db.cursor()
    cur.execute("SELECT articles.author, authors.name, count(articles.id) \
                AS num FROM authors, articles, log WHERE articles.slug LIKE \
                (split_part(log.path,'/', 3)) AND articles.author=authors.id \
                GROUP BY articles.author, authors.name ORDER BY num DESC;")
    result = [row[1:3] for row in cur.fetchall()]
    db.close()
    return result


def error_calc():
    """Returns days with more than 1% of bad requests"""
    db = psycopg2.connect(database="news")
    cur = db.cursor()
    cur.execute("SELECT subq2.time::date, subq2.num2 FROM (SELECT \
                log.time::date, (subq.num*100)/(count(log.status) \
                + subq.num)::float AS num2 FROM log, (SELECT \
                time::date, count(status) AS num FROM log WHERE \
                status != '200 OK' GROUP BY time::date ORDER BY \
                time::date DESC) AS subq WHERE log.time::date=subq.time::date\
                AND log.status = '200 OK' GROUP BY log.time::date, subq.num\
                ORDER BY log.time::date DESC) AS subq2 WHERE subq2.num2 > 1\
                ORDER BY subq2.time::date DESC;")
    result = [row[:2] for row in cur.fetchall()]
    db.close()
    return result


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Logs Analysis')
    parser.add_argument('--ques', type=int, default=1, help='question index')

    args = parser.parse_args()
    ques = args.ques

    if ques == 1:
        print("Searching for top 3 most-accessed articles...")
        result = popular_articles()
        print("The top 3 most-accessed articles are: ")
        for idx in range(1, 4):
            print("{0}. '{1}' with {2} views").format(idx, result[idx-1][0],
                                                      result[idx-1][1])
    elif ques == 2:
        print("Searching for authors with most combined articles views...")
        result = popular_authors()
        print("The authors with the most combined articles views are: ")
        for idx in range(1, 5):
            print("{0}. '{1}' with {2} views").format(idx, result[idx-1][0],
                                                      result[idx-1][1])
    else:
        print("Searching for days with more than 1% of bad requests ...")
        result = error_calc()
        print("Day(s) with more than 1% of bad requests:")
        print("{0} with {1:.2g}% of bad requests").format(result[0][0],
                                                          result[0][1])
