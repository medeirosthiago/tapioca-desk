# coding: utf-8

LABELS_MAPPING = {
    'labels_list': {
        'resource': 'labels',
        'docs': 'http://dev.desk.com/API/labels/#list',
        'methods': ['GET']
    },
    'labels_show': {
        'resource': 'labels/{id}',
        'docs': 'http://dev.desk.com/API/labels/#show',
        'methods': ['GET']
    },
    'labels_create': {
        'resource': 'labels',
        'docs': 'http://dev.desk.com/API/labels/#create',
        'methods': ['POST']
    },
    'labels_update': {
        'resource': 'labels/{id}',
        'docs': 'http://dev.desk.com/API/labels/#update',
        'methods': ['PATCH']
    },
    'labels_delete': {
        'resource': 'labels/{id}',
        'docs': 'http://dev.desk.com/API/labels/#delete',
        'methods': ['DELETE']
    },
    'labels_search': {
        'resource': 'labels/search',
        'docs': 'http://dev.desk.com/API/labels/#search',
        'methods': ['GET']
    },
}
