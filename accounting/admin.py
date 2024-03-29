from django.apps import apps
from django.contrib import admin

models = apps.get_models('accounting')

models_to_register = [ 'Accounting', 'Characteristic', 'Company',
                       'CompanyContact', 'EconomicActivity','Membership',
                       'Organization', 'Purchase', 'Sale',
                       'Subscription', 'Transaction', 'User', 'Stakeholder', 'Plan', 'PlanOrganization'
                    ]

for model in models:
    if model.__name__ in models_to_register:
      admin.site.register(model)
