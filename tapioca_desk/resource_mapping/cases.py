# coding: utf-8

CASES_MAPPING = {
    'cases': {
        'resource': 'cases',
        'docs': 'http://dev.desk.com/API/cases/',
        'methods': ['POST', 'GET']
    },
    'case': {
        'resource': 'cases/{id}',
        'docs': 'http://dev.desk.com/API/cases/#show',
        'methods': ['GET', 'PATCH', 'DELETE']
    },
    'case_search': {
        'resource': 'cases/search',
        'docs': 'http://dev.desk.com/API/cases/#search',
        'methods': ['GET']
    }
}
