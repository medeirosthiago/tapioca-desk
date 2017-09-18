# coding: utf-8

ARTICLES_MAPPING = {
    'articles': {
        'resource': 'articles',
        'docs': 'http://dev.desk.com/API/articles/',
        'methods': ['POST', 'GET']
    },
    'article': {
        'resource': 'articles/{id}',
        'docs': 'http://dev.desk.com/API/articles/#show',
        'methods': ['GET', 'PATCH', 'DELETE']
    },
    'article_search': {
        'resource': 'articles/search',
        'docs': 'http://dev.desk.com/API/articles/#search',
        'methods': ['GET']
    }
}
