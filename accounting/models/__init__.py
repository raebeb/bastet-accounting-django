from .accounting import Accounting
from .characteristic import Characteristic
from .company import Company
from .company_contact import CompanyContact
from .economic_activity import EconomicActivity
from .invitation import Invitation
from .membership import Membership
from .organization import Organization
from .purchase import Purchase
from .role import Role
from .sale import Sale
from .subscription import Subscription
from .transaction import Transaction
from .user import User
from .stakeholder import Stakeholder

# TODO: pass all import to dinamic import
# import os
# os.chdir('accounting/models')
# for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))
