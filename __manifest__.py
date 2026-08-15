{
    'name': 'Indonesia Localization Improvement',
    'version': '19.0.1.0',
    'author': 'Owo Sugiana',
    'license': 'LGPL-3',
    'summary': 'Indonesian translation improvements and default localization',
    'description': (
        'An example of the improvement is that the translation of State in '
        'the Contacts menu should be Province, not Status.'),
    'category': 'Localizations',
    'pre_init_hook': 'pre_init',
    'data': [
        'data/res_company.xml',
        'data/res_lang.xml',
        'data/res_currency.xml',
        'data/ir_default.xml',
    ],
}
