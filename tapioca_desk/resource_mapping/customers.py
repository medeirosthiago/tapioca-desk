# coding: utf-8

CUSTOMERS_MAPPING = {
    'customers_list': {
        'resource': 'customers',
        'docs': 'http://dev.desk.com/API/customers/#list',
        'methods': ['GET']
    },
    'customers_show': {
        'resource': 'customers/{id}',
        'docs': 'http://dev.desk.com/API/customers/#show',
        'methods': ['GET']
    },
    'customers_create': {
        'resource': 'customers',
        'docs': 'http://dev.desk.com/API/customers/#create',
        'methods': ['POST']
    },
    'customers_update': {
        'resource': 'customers/{id}',
        'docs': 'http://dev.desk.com/API/customers/#update',
        'methods': ['PATCH']
    },
    'customers_search': {
        'resource': 'customers/search',
        'docs': 'http://dev.desk.com/API/customers/#search',
        'methods': ['GET']
    },
    'customers_list_cases': {
        'resource': 'customers/{id}/cases',
        'docs': 'http://dev.desk.com/API/customers/#cases-list',
        'methods': ['GET']
    },
    'customers_merge': {
        'resource': 'customers/{id}/merge',
        'docs': 'http://dev.desk.com/API/customers/#merge',
        'methods': ['POST']
    },
}
