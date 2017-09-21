# coding: utf-8

COMPANIES_MAPPING = {
    'companies_list': {
        'resource': 'companies',
        'docs': 'http://dev.desk.com/API/companies/#list',
        'methods': ['GET']
    },
    'companies_show': {
        'resource': 'companies/{id}',
        'docs': 'http://dev.desk.com/API/companies/#show',
        'methods': ['GET']
    },
    'companies_create': {
        'resource': 'companies',
        'docs': 'http://dev.desk.com/API/companies/#create',
        'methods': ['POST']
    },
    'companies_update': {
        'resource': 'companies/{id}',
        'docs': 'http://dev.desk.com/API/companies/#update',
        'methods': ['PATCH']
    },
    'companies_search': {
        'resource': 'companies/search',
        'docs': 'http://dev.desk.com/API/companies/#search',
        'methods': ['GET']
    },
    'companies_list_cases': {
        'resource': 'companies/{id}/cases',
        'docs': 'http://dev.desk.com/API/companies/#cases-list',
        'methods': ['GET']
    },
    'companies_customers': {
        'resource': 'companies/{id}/customers',
        'docs': 'http://dev.desk.com/API/companies/#customers-list',
        'methods': ['GET']
    },
}

