# coding: utf-8

CASES_MAPPING = {
    'cases_list': {
        'resource': 'cases',
        'docs': 'http://dev.desk.com/API/cases/#list',
        'methods': ['GET']
    },
    'cases_search': {
        'resource': 'cases/search',
        'docs': 'http://dev.desk.com/API/cases/#search',
        'methods': ['GET']
    },
    'cases_show': {
        'resource': 'cases/{case_id}',
        'docs': 'http://dev.desk.com/API/cases/#show',
        'methods': ['GET']
    },
    'cases_create': {
        'resource': 'cases',
        'docs': 'http://dev.desk.com/API/cases/#create',
        'methods': ['POST']
    },
    'cases_create_customer': {
        'resource': 'customers/{customer_id}/cases',
        'docs': 'http://dev.desk.com/API/cases/#create',
        'methods': ['POST']
    },
    'cases_update': {
        'resource': 'cases/{case_id}',
        'docs': 'http://dev.desk.com/API/cases/#update',
        'methods': ['PATCH']
    },
    'cases_delete': {
        'resource': 'cases/{case_id}',
        'docs': 'http://dev.desk.com/API/cases/#delete',
        'methods': ['DELETE']
    },
    'cases_forward': {
        'resource': 'cases/{case_id}/forward',
        'docs': 'http://dev.desk.com/API/cases/#forward',
        'methods': ['POST']
    },
    'cases_route': {
        'resource': 'cases/routing',
        'docs': 'http://dev.desk.com/API/cases/#routing',
        'methods': ['POST']
    },
    'cases_unsend': {
        'resource': 'cases/{case_id}/unsend',
        'docs': 'http://dev.desk.com/API/cases/#unsend',
        'methods': ['POST']
    },
    'cases_message_show': {
        'resource': 'cases/{case_id}/message',
        'docs': 'http://dev.desk.com/API/cases/#message-show',
        'methods': ['GET']
    },
    'cases_message_update': {
        'resource': 'cases/{case_id}/message',
        'docs': 'http://dev.desk.com/API/cases/#message-update',
        'methods': ['PATCH']
    },
    'cases_message_delete': {
        'resource': 'cases/{case_id}/message',
        'docs': 'http://dev.desk.com/API/cases/#message-delete',
        'methods': ['DELETE']
    },
    'cases_reply_list': {
        'resource': 'cases/{case_id}/replies',
        'docs': 'http://dev.desk.com/API/cases/#reply-list',
        'methods': ['GET']
    },
    'cases_replies_show': {
        'resource': 'cases/{case_id}/replies/{reply_id}',
        'docs': 'http://dev.desk.com/API/cases/#replies-show',
        'methods': ['GET']
    },
    'cases_replies_create': {
        'resource': 'cases/{case_id}/replies',
        'docs': 'http://dev.desk.com/API/cases/#reply-create',
        'methods': ['POST']
    },
    'cases_replies_update': {
        'resource': 'cases/{case_id}/replies/{reply_id}',
        'docs': 'http://dev.desk.com/API/cases/#replies-update',
        'methods': ['PATCH']
    },
    'cases_replies_delete': {
        'resource': 'cases/{case_id}/replies/{reply_id}',
        'docs': 'http://dev.desk.com/API/cases/#replies-delete',
        'methods': ['DELETE']
    },
    'cases_drafts': {
        'resource': 'cases/{case_id}/replies/draft',
        'docs': 'http://dev.desk.com/API/cases/#drafts-show',
        'methods': ['GET', 'POST', 'PATCH']
    },
    'cases_notes_list': {
        'resource': 'cases/{case_id}/notes',
        'docs': 'http://dev.desk.com/API/cases/#notes-list',
        'methods': ['GET']
    },
    'cases_notes_show': {
        'resource': 'cases/{case_id}/notes/{note_id}',
        'docs': 'http://dev.desk.com/API/cases/#notes-show',
        'methods': ['GET']
    },
    'cases_notes_create': {
        'resource': 'cases/{case_id}/notes',
        'docs': 'http://dev.desk.com/API/cases/#notes-create',
        'methods': ['POST']
    },
    'cases_notes_update': {
        'resource': 'cases/{case_id}/notes/{note_id}',
        'docs': 'http://dev.desk.com/API/cases/#notes-update',
        'methods': ['PATCH']
    },
    'cases_notes_delete': {
        'resource': 'cases/{case_id}/notes/{note_id}',
        'docs': 'http://dev.desk.com/API/cases/#notes-delete',
        'methods': ['DELETE']
    },
    'cases_attachments_url': {
        'resource': 'cases/{case_id}/attachments/{attch_id}/{url}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-url',
        'methods': ['GET']
    },
    'cases_attachments_list': {
        'resource': 'cases/{case_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-list',
        'methods': ['GET']
    },
    'cases_attachments_message_list': {
        'resource': 'cases/{case_id}/message/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-list',
        'methods': ['GET']
    },
    'cases_attachments_reply_list': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-list',
        'methods': ['GET']
    },
    'cases_attachments_show': {
        'resource': 'cases/{case_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-show',
        'methods': ['GET']
    },
    'cases_attachments_message_show': {
        'resource': 'cases/{case_id}/message/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-show',
        'methods': ['GET']
    },
    'cases_attachments_reply_show': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-show',
        'methods': ['GET']
    },
    'cases_attachments_create': {
        'resource': 'cases/{case_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-create',
        'methods': ['POST']
    },
    'cases_attachments_reply_create': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-create',
        'methods': ['POST']
    },
    'cases_attachments_message_create': {
        'resource': 'cases/{case_id}/message/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-create',
        'methods': ['POST']
    },
    'cases_attachments_delete': {
        'resource': 'cases/{case_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-delete',
        'methods': ['DELETE']
    },
    'cases_attachments_reply_delete': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-delete',
        'methods': ['DELETE']
    },
    'cases_attachments_message_delete': {
        'resource': 'cases/{case_id}/message/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-delete',
        'methods': ['DELETE']
    },
    'cases_macro_preview': {
        'resource': 'cases/{case_id}/macros/preview',
        'docs': 'http://dev.desk.com/API/cases/#macro_preview',
        'methods': ['POST']
    },
    'cases_feed': {
        'resource': 'cases/{case_id}/feed',
        'docs': 'http://dev.desk.com/API/cases/#feed',
        'methods': ['GET']
    },
    'cases_history': {
        'resource': 'cases/{case_id}/history',
        'docs': 'http://dev.desk.com/API/cases/#history',
        'methods': ['GET']
    },
    'cases_labels_list': {
        'resource': 'cases/{case_id}/labels',
        'docs': 'http://dev.desk.com/API/cases/#labels',
        'methods': ['GET']
    },
    'cases_links_list': {
        'resource': 'cases/{case_id}/links',
        'docs': 'http://dev.desk.com/API/cases/#links-list',
        'methods': ['GET', 'POST']
    },
    'cases_split_partial_cases_reply': {
        'resource': 'cases/{case_id}/replies/{reply_id}/splits',
        'docs': 'http://dev.desk.com/API/cases/#split',
        'methods': ['GET', 'POST']
    },
    'cases_split_partial_cases_message': {
        'resource': 'cases/{case_id}/message/splits',
        'docs': 'http://dev.desk.com/API/cases/#split',
        'methods': ['GET', 'POST']
    },
    'cases_facebook_likes': {
        'resource': 'cases/{case_id}/message/likes',
        'docs': 'http://dev.desk.com/API/cases/#likes-list',
        'methods': ['GET']
    },
}
