# Generated by Django 4.1.4 on 2023-02-11 23:36

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('state', django_fsm.FSMField(choices=[('created', 'created'), ('verified', 'verified'), ('banned', 'banned')], default='created', max_length=50, protected=True, verbose_name='User state')),
                ('current_sign_in_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('last_sign_in_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('current_organization', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='accounting_user_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Accounting',
                'verbose_name_plural': 'Accountings',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('tax_refered', models.CharField(max_length=50, verbose_name='tax refered')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('join_code', models.CharField(max_length=6, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[('draft', 'draft'), ('created', 'created'), ('published', 'published'), ('hidden', 'hidden'), ('finished', 'finished')], default='draft', max_length=50, protected=True, verbose_name='Plan state')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=50)),
                ('company_quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=20)),
                ('current_partner', models.BooleanField(default=False)),
                ('legal_representative', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.company')),
            ],
            options={
                'verbose_name': 'Stakeholder',
                'verbose_name_plural': 'Stakeholders',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('document_type', models.CharField(choices=[('DH', 'de_honorarios'), ('DCV', 'de_compraventa'), ('DPDS', 'de_prestacion_de_servicios'), ('CDPE', 'comprobante_de_pago_electronico'), ('LDCP', 'libros_de_contabilidad_principal'), ('LC', 'libro_caja'), ('LD', 'libro_diario'), ('LM', 'libro_mayor'), ('LDH', 'libro_de_honorarios'), ('LDIYB', 'libro_de_inventarios_y_balances'), ('LDC', 'libros_de_control'), ('LF', 'libro_fut'), ('LA', 'libros_auxiliares'), ('LDCOMP', 'libro_de_compras'), ('LDREM', 'libro_de_remuneraciones'), ('LDRET', 'libro_de_retenciones'), ('NDC', 'notas_de_credito'), ('NDB', 'notas_de_debito'), ('LETDCAM', 'letras_de_cambio'), ('P', 'pagares')], max_length=20)),
                ('transaction_type', models.CharField(choices=[('C', 'compra'), ('V', 'venta')], max_length=20)),
                ('rut_customer_or_supplier', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('folio', models.CharField(max_length=20)),
                ('document_date', models.DateField()),
                ('acknowledgement_date', models.DateField()),
                ('exempt_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('net_total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('code_other_tax', models.CharField(max_length=20)),
                ('value_other_tax', models.DecimalField(decimal_places=3, max_digits=10)),
                ('other_tax', models.CharField(max_length=20)),
                ('nce_or_nde_on_purchase_invoice', models.CharField(max_length=20)),
                ('claim_date', models.DateField()),
                ('total_iva_withheld', models.DecimalField(decimal_places=2, max_digits=20)),
                ('partial_iva_withheld', models.DecimalField(decimal_places=2, max_digits=20)),
                ('own_iva', models.DecimalField(decimal_places=2, max_digits=20)),
                ('third_party_iva', models.DecimalField(decimal_places=2, max_digits=20)),
                ('rut_liquid_commission_invoice', models.CharField(max_length=20)),
                ('net_liquid_commission_invoice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('commission_exempt_liquid_invoice', models.DecimalField(decimal_places=2, max_digits=20)),
                ('iva_out_of_time', models.DecimalField(decimal_places=2, max_digits=20)),
                ('type_of_document_reference', models.CharField(max_length=20)),
                ('folio_reference_document', models.CharField(max_length=20)),
                ('foreign_recipients_identity_number', models.CharField(max_length=20)),
                ('nationality_foreign_recipients', models.CharField(max_length=20)),
                ('construction_company_loan', models.DecimalField(decimal_places=2, max_digits=20)),
                ('free_zone_tax', models.DecimalField(decimal_places=2, max_digits=20)),
                ('packaging_warranty', models.DecimalField(decimal_places=2, max_digits=20)),
                ('no_cost_sales_indicator', models.CharField(max_length=20)),
                ('periodic_service_indicator', models.CharField(max_length=20)),
                ('non_billable_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_amount_period', models.DecimalField(decimal_places=2, max_digits=20)),
                ('ticket_sales_national_transportation', models.DecimalField(decimal_places=2, max_digits=20)),
                ('sale_of_international_transportation_tickets', models.DecimalField(decimal_places=2, max_digits=20)),
                ('accounting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.accounting')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('document_type', models.CharField(choices=[('DH', 'de_honorarios'), ('DCV', 'de_compraventa'), ('DPDS', 'de_prestacion_de_servicios'), ('CDPE', 'comprobante_de_pago_electronico'), ('LDCP', 'libros_de_contabilidad_principal'), ('LC', 'libro_caja'), ('LD', 'libro_diario'), ('LM', 'libro_mayor'), ('LDH', 'libro_de_honorarios'), ('LDIYB', 'libro_de_inventarios_y_balances'), ('LDC', 'libros_de_control'), ('LF', 'libro_fut'), ('LA', 'libros_auxiliares'), ('LDCOMP', 'libro_de_compras'), ('LDREM', 'libro_de_remuneraciones'), ('LDRET', 'libro_de_retenciones'), ('NDC', 'notas_de_credito'), ('NDB', 'notas_de_debito'), ('LETDCAM', 'letras_de_cambio'), ('P', 'pagares')], max_length=20)),
                ('transaction_type', models.CharField(choices=[('C', 'compra'), ('V', 'venta')], max_length=20)),
                ('rut_customer_or_supplier', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=100)),
                ('folio', models.CharField(max_length=20)),
                ('document_date', models.DateField()),
                ('acknowledgement_date', models.DateField()),
                ('exempt_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('net_total', models.DecimalField(decimal_places=3, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=3, max_digits=10)),
                ('code_other_tax', models.CharField(max_length=20)),
                ('value_other_tax', models.DecimalField(decimal_places=3, max_digits=10)),
                ('other_tax', models.CharField(max_length=20)),
                ('nce_or_nde_on_purchase_invoice', models.CharField(max_length=20)),
                ('amount_of_recoverable_iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_of_non_recoverable_iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('non_recoverable_iva_code', models.CharField(max_length=2)),
                ('net_fixed_asset', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fixed_asset_iva', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva_common_use', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_without_right_to_credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva_not_withheld', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cigars', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tobacco_cigarettes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('elaborated_cigars', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accounting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.accounting')),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
            },
        ),
        migrations.CreateModel(
            name='PlanOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[('created', 'created'), ('active', 'active'), ('inactive', 'inactive')], default='created', max_length=50, protected=True, verbose_name='PlanOrganization state')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.organization')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.plan')),
            ],
            options={
                'verbose_name': 'PlanOrganization',
                'verbose_name_plural': 'PlanOrganizations',
            },
        ),
        migrations.AddField(
            model_name='organization',
            name='plans',
            field=models.ManyToManyField(through='accounting.PlanOrganization', to='accounting.plan'),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.IntegerField()),
                ('state', django_fsm.FSMField(choices=[('created', 'created'), ('invited', 'invited'), ('active', 'active'), ('inactive', 'inactive'), ('removed', 'removed'), ('suspended', 'suspended')], default='created', max_length=50, protected=True, verbose_name='Membership state')),
                ('invitation_code', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('roles', models.ManyToManyField(related_name='memberships', to='accounting.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Membership',
                'verbose_name_plural': 'Memberships',
            },
        ),
        migrations.CreateModel(
            name='JoinRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[('created', 'created'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='created', max_length=50, protected=True, verbose_name='Join request state')),
                ('reviewed_by', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to='accounting.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Join request',
                'verbose_name_plural': 'Join requests',
            },
        ),
        migrations.CreateModel(
            name='EconomicActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField()),
                ('category', models.CharField(max_length=20)),
                ('taxable', models.BooleanField()),
                ('start_at', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.company')),
            ],
            options={
                'verbose_name': 'Economic Activity',
                'verbose_name_plural': 'Economic Activities',
            },
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('cellphone_number', models.CharField(max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.company')),
            ],
            options={
                'verbose_name': 'Company Contact',
                'verbose_name_plural': 'Company Contacts',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_at', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.company')),
            ],
            options={
                'verbose_name': 'Characteristic',
                'verbose_name_plural': 'Characteristics',
            },
        ),
        migrations.AddField(
            model_name='accounting',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='accounting.company'),
        ),
    ]
