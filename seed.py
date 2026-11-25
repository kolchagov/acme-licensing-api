"""Idempotent demo data: 10 users, 10 customers, 10 products.

Run: python manage.py shell -c "exec(open('seed.py').read())"
"""
from accounts.models import User
from customers.models import Customer
from products.models import Product

PASSWORD = "Acme!2026"

USERS = [
    # (username, email, is_company, company_name, iban)
    ("vertex_systems", "office@vertex-systems.bg", True, "Vertex Systems Ltd.", "BG18RZBB91550123456789"),
    ("nova_soft", "sales@novasoft.bg", True, "NovaSoft Solutions Ltd.", "BG44BNBG96611000112233"),
    ("orbit_labs", "hello@orbitlabs.eu", True, "Orbit Labs EOOD", "BG29UNCR70001500123456"),
    ("quantum_web", "team@quantumweb.bg", True, "Quantum Web AD", "BG07STSA93000000123456"),
    ("delta_cloud", "info@deltacloud.bg", True, "Delta Cloud OOD", "BG63FINV91501000223344"),
    ("m.ivanova", "m.ivanova@mail.bg", False, None, None),
    ("g.petrov", "g.petrov@abv.bg", False, None, None),
    ("e.dimitrova", "e.dimitrova@gmail.com", False, None, None),
    ("s.kolev", "s.kolev@yahoo.com", False, None, None),
    ("v.stoyanova", "v.stoyanova@proton.me", False, None, None),
]

CUSTOMERS = [
    # (name, address, contact_person, uic, vat, phone, email)
    ("Techno Market Ltd.", "12 Vitosha Blvd., Sofia", "Ivan Petrov", "203456789", "BG203456789", "+359 2 9876543", "office@technomarket-demo.bg"),
    ("Balkan Logistics AD", "45 Industrial Zone, Plovdiv", "Maria Georgieva", "123456789", "BG123456789", "+359 32 654321", "contact@balkanlog-demo.bg"),
    ("Sunrise Consulting EOOD", "7 Tsar Osvoboditel, Varna", "Dimitar Kolev", "987654321", "BG987654321", "+359 52 123456", "hello@sunrise-consult.bg"),
    ("Green Energy Group", "88 Ring Road, Burgas", "Elena Marinova", "456789123", "BG456789123", "+359 56 789123", "info@greenenergy-demo.bg"),
    ("City Retail OOD", "3 Knyaz Alexander, Ruse", "Nikolay Todorov", "789123456", "BG789123456", "+359 82 456789", "sales@cityretail-demo.bg"),
    ("Alpha Insurance AD", "101 Cherni Vrah, Sofia", "Tanya Petrova", "321654987", "BG321654987", "+359 2 5551234", "claims@alpha-ins-demo.bg"),
    ("Danube Shipping EOOD", "19 Port Street, Vidin", "Georgi Dimitrov", "654987321", "BG654987321", "+359 94 431222", "office@danube-ship-demo.bg"),
    ("Mountain Hotels AD", "5 Pirin Str., Bansko", "Svetla Ivanova", "147258369", "BG147258369", "+359 749 88100", "reservations@mountainhotels-demo.bg"),
    ("Smart Agriculture Ltd.", "27 Dobrudzha Rd., Dobrich", "Krasimir Angelov", "369258147", "BG369258147", "+359 58 600700", "info@smartagro-demo.bg"),
    ("Metro Build EOOD", "64 Slivnitsa Blvd., Sofia", "Radostina Ilieva", "258147369", "BG258147369", "+359 2 8123456", "projects@metrobuild-demo.bg"),
]

PRODUCTS = [
    # (code, name, url, description)
    ("A01", "Acme Invoice Manager", "https://acme.example.com/invoice", "Invoicing, numbering and VAT reporting for small teams."),
    ("B02", "Acme Stock Keeper", "https://acme.example.com/stock", "Warehouse stock levels, batches and low-stock alerts."),
    ("C03", "Acme CRM Suite", "https://acme.example.com/crm", "Customer records, pipelines and activity reminders."),
    ("D04", "Acme Payroll Pro", "https://acme.example.com/payroll", "Monthly payroll, leave balances and payslip export."),
    ("E05", "Acme Docs Vault", "https://acme.example.com/docs", "Versioned document storage with audit trail."),
    ("F06", "Acme Helpdesk", "https://acme.example.com/helpdesk", "Ticket queue with SLA timers and canned replies."),
    ("G07", "Acme Analytics", "https://acme.example.com/analytics", "Dashboards over sales, licences and renewals."),
    ("H08", "Acme Booking Desk", "https://acme.example.com/booking", "Calendar booking for services and resources."),
    ("I09", "Acme Fleet Tracker", "https://acme.example.com/fleet", "Vehicle registry, servicing and fuel logs."),
    ("J10", "Acme Backup Guard", "", "Scheduled off-site backups with restore checks."),
]

for username, email, is_company, company_name, iban in USERS:
    user, created = User.objects.get_or_create(
        username=username,
        defaults=dict(email=email, is_company=is_company, company_name=company_name, iban=iban),
    )
    if created:
        user.set_password(PASSWORD)
        user.save()

for name, address, contact_person, uic, vat, phone, email in CUSTOMERS:
    Customer.objects.update_or_create(uic=uic, defaults=dict(
        name=name, address=address, contact_person=contact_person,
        vat=vat, phone=phone, email=email,
    ))

for code, name, url, description in PRODUCTS:
    Product.objects.get_or_create(code=code, defaults=dict(name=name, url=url, description=description))

print(
    f"users={User.objects.count()} customers={Customer.objects.count()} products={Product.objects.count()}"
)
