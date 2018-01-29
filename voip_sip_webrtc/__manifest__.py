# -*- coding: utf-8 -*-
{
    'name': "Voip Communication",
    'version': "1.6.5",
    'author': "Sythil Tech",
    'category': "Tools",
    'support': "steven@sythiltech.com.au",
    'summary': "Make video calls with other users inside your system",
    'license':'LGPL-3',
    'data': [
        'views/voip_sip_webrtc_templates.xml',
        'views/res_users_views.xml',
        'views/voip_call_views.xml',
        'views/voip_call_template_preview_views.xml',
        'views/voip_call_template_views.xml',
        'views/voip_ringtone_views.xml',
        'views/voip_account_views.xml',
        'views/voip_settings_views.xml',
        'views/res_partner_views.xml',
        'views/voip_media_views.xml',
        'views/voip_message_compose_views.xml',
        'views/ir_actions_server_views.xml',
        'views/voip_message_template_views.xml',
        'views/menus.xml',
        'security/ir.model.access.csv',
        'data/voip_ringtone.xml',
        'data/voip_settings.xml',
        'data/voip.codec.csv',
        'data/voip.account.action.type.csv',
        'data/ir.cron.csv',
        'data/mail.message.subtype.csv',
    ],
    'demo': [],
    'depends': ['web','crm','bus'],
    'qweb': ['static/src/xml/*.xml'],
    'images':[
        'static/description/1.jpg',
        'static/description/2.jpg',
    ],
    'installable': True,
}