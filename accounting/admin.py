from django.apps import apps
from django.contrib import admin

models = apps.get_models('accounting')

register_models = [ 'Accounting', 'Characteristic', 'Company',
                    'CompanyContact', 'EconomicActivity', 'Invitation',
                    'Membership', 'Organization', 'Purchase', 'Role', 'Sale',
                    'Subscription', 'Transaction', 'User', 'Stakeholder'
                  ]

for model in models:
    if model.__name__ in register_models:
      admin.site.register(model)
