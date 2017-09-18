# coding: utf-8

CASES_MAPPING = {
    'case_list': {
        'resource': 'cases',
        'docs': 'http://dev.desk.com/API/cases/#list',
        'methods': ['GET']
    },
    'case_search': {
        'resource': 'cases/search',
        'docs': 'http://dev.desk.com/API/cases/#search',
        'methods': ['GET']
    },
    'case_show': {
        'resource': 'cases/{case_id}',
        'docs': 'http://dev.desk.com/API/cases/#show',
        'methods': ['GET']
    },
    'case_create': {
        'resource': 'cases',
        'docs': 'http://dev.desk.com/API/cases/#create',
        'methods': ['POST']
    },
    'case_create_customer': {
        'resource': 'customers/{customer_id}/cases',
        'docs': 'http://dev.desk.com/API/cases/#create',
        'methods': ['POST']
    },
    'case_update': {
        'resource': 'cases/{case_id}',
        'docs': 'http://dev.desk.com/API/cases/#update',
        'methods': ['PATCH']
    },
    'case_delete': {
        'resource': 'cases/{case_id}',
        'docs': 'http://dev.desk.com/API/cases/#delete',
        'methods': ['DELETE']
    },
    'case_forward': {
        'resource': 'cases/{case_id}/forward',
        'docs': 'http://dev.desk.com/API/cases/#forward',
        'methods': ['POST']
    },
    'case_route': {
        'resource': 'cases/routing',
        'docs': 'http://dev.desk.com/API/cases/#routing',
        'methods': ['POST']
    },
    'case_unsend': {
        'resource': 'cases/{case_id}/unsend',
        'docs': 'http://dev.desk.com/API/cases/#unsend',
        'methods': ['POST']
    },
    'case_message_show': {
        'resource': 'cases/{case_id}/message',
        'docs': 'http://dev.desk.com/API/cases/#message-show',
        'methods': ['GET']
    },
    'case_message_update': {
        'resource': 'cases/{case_id}/message',
        'docs': 'http://dev.desk.com/API/cases/#message-update',
        'methods': ['PATCH']
    },
    'case_message_delete': {
        'resource': 'cases/{case_id}/message',
        'docs': 'http://dev.desk.com/API/cases/#message-delete',
        'methods': ['GET', 'PATCH', 'DELETE']
    },
    'case_reply_list': {
        'resource': 'cases/{case_id}/replies',
        'docs': 'http://dev.desk.com/API/cases/#reply-list',
        'methods': ['GET']
    },
    'case_reply_show': {
        'resource': 'cases/{case_id}/replies/{reply_id}',
        'docs': 'http://dev.desk.com/API/cases/#replies-show',
        'methods': ['GET']
    },
    'case_reply_create': {
        'resource': 'cases/{case_id}/replies',
        'docs': 'http://dev.desk.com/API/cases/#reply-create',
        'methods': ['POST']
    },
    'case_reply_update': {
        'resource': 'cases/{case_id}/replies/{reply_id}',
        'docs': 'http://dev.desk.com/API/cases/#replies-update',
        'methods': ['PATCH']
    },
    'case_reply_delete': {
        'resource': 'cases/{case_id}/replies/{reply_id}',
        'docs': 'http://dev.desk.com/API/cases/#replies-delete',
        'methods': ['DELETE']
    },
    'case_draft': {
        'resource': 'cases/{case_id}/replies/draft',
        'docs': 'http://dev.desk.com/API/cases/#drafts-show',
        'methods': ['GET', 'POST', 'PATCH']
    },
    'case_note_list': {
        'resource': 'cases/{case_id}/notes',
        'docs': 'http://dev.desk.com/API/cases/#notes-list',
        'methods': ['GET']
    },
    'case_note_show': {
        'resource': 'cases/{case_id}/notes/{note_id}',
        'docs': 'http://dev.desk.com/API/cases/#notes-show',
        'methods': ['GET']
    },
    'case_note_create': {
        'resource': 'cases/{case_id}/notes',
        'docs': 'http://dev.desk.com/API/cases/#notes-create',
        'methods': ['POST']
    },
    'case_note_update': {
        'resource': 'cases/{case_id}/notes/{note_id}',
        'docs': 'http://dev.desk.com/API/cases/#notes-update',
        'methods': ['PATCH']
    },
    'case_note_delete': {
        'resource': 'cases/{case_id}/notes/{note_id}',
        'docs': 'http://dev.desk.com/API/cases/#notes-delete',
        'methods': ['DELETE']
    },
    'case_attachment_url': {
        'resource': 'cases/{case_id}/attachments/{attch_id}/{url}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-url',
        'methods': ['GET']
    },
    'case_attachment_list': {
        'resource': 'cases/{case_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-list',
        'methods': ['GET']
    },
    'case_attachment_message_list': {
        'resource': 'cases/{case_id}/message/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-list',
        'methods': ['GET']
    },
    'case_attachment_reply_list': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-list',
        'methods': ['GET']
    },
    'case_attachment_show': {
        'resource': 'cases/{case_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-show',
        'methods': ['GET']
    },
    'case_attachment_message_show': {
        'resource': 'cases/{case_id}/message/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-show',
        'methods': ['GET']
    },
    'case_attachment_reply_show': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-show',
        'methods': ['GET']
    },
    'case_attachment_create': {
        'resource': 'cases/{case_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-create',
        'methods': ['POST']
    },
    'case_attachment_reply_create': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-create',
        'methods': ['POST']
    },
    'case_attachment_message_create': {
        'resource': 'cases/{case_id}/message/attachments',
        'docs': 'http://dev.desk.com/API/cases/#attachments-create',
        'methods': ['POST']
    },
    'case_attachment_delete': {
        'resource': 'cases/{case_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-delete',
        'methods': ['DELETE']
    },
    'case_attachment_reply_delete': {
        'resource': 'cases/{case_id}/replies/{reply_id}/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-delete',
        'methods': ['DELETE']
    },
    'case_attachment_message_delete': {
        'resource': 'cases/{case_id}/message/attachments/{attch_id}',
        'docs': 'http://dev.desk.com/API/cases/#attachments-delete',
        'methods': ['DELETE']
    },
    'case_macro_preview': {
        'resource': 'cases/{case_id}/macros/preview',
        'docs': 'http://dev.desk.com/API/cases/#macro_preview',
        'methods': ['POST']
    },
    'case_feed': {
        'resource': 'cases/{case_id}/feed',
        'docs': 'http://dev.desk.com/API/cases/#feed',
        'methods': ['GET']
    },
    'case_history': {
        'resource': 'cases/{case_id}/history',
        'docs': 'http://dev.desk.com/API/cases/#history',
        'methods': ['GET']
    },
    'case_label_list': {
        'resource': 'cases/{case_id}/labels',
        'docs': 'http://dev.desk.com/API/cases/#labels',
        'methods': ['GET']
    },
    'case_link_list': {
        'resource': 'cases/{case_id}/links',
        'docs': 'http://dev.desk.com/API/cases/#links-list',
        'methods': ['GET', 'POST']
    },
    'case_split_partial_case_reply': {
        'resource': 'cases/{case_id}/replies/{reply_id}/splits',
        'docs': 'http://dev.desk.com/API/cases/#split',
        'methods': ['GET', 'POST']
    },
    'case_split_partial_case_message': {
        'resource': 'cases/{case_id}/message/splits',
        'docs': 'http://dev.desk.com/API/cases/#split',
        'methods': ['GET', 'POST']
    },
    'case_facebook_likes': {
        'resource': 'cases/{case_id}/message/likes',
        'docs': 'http://dev.desk.com/API/cases/#likes-list',
        'methods': ['GET']
    },
}
