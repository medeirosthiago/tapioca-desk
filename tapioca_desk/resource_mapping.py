# coding: utf-8

RESOURCE_MAPPING = {
    'resource_name': {
        'resource': 'resource_url',
        'docs': 'http://www.documentation.com/link/to/resource/documentation'
    },

    # Articles
    'articles': {
        'resource': 'https://{site}.desk.com/api/v2/articles',
        'docs': 'http://dev.desk.com/API/articles/',
        'methods': ['POST', 'GET']
    }
}
