#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system

###########
# CLEAN
###########
# clean everything
print '=> Cleaning everything ...'
system('rm db.sqlite3')
print '=> Done'

###########
# CONF DB
###########
# sync db
print '=> Sync db + migrate'
system('python manage.py syncdb --noinput')
print '=> Done'

###########
# ADD DATA
###########
# create super user
print '=> Creating super user ...'
code = (
    "from django.contrib.auth.models import User",
    "u = User.objects.create_superuser('admin', 'admin@mailoo.org', 'admin')",
    "u.save()",
)
system('echo "%s" | python manage.py shell' % '\n'.join(code))
print '=> Done'

# create fake data
code = (
    "from sf.sf.models import Product, Position",
    "import faker",
    "f = faker.Faker()",
    "for i in range(20):",
    "    pos = Position()",
    "    pos.x = f.random_int(min=0, max=4)",
    "    pos.y = f.random_int(min=0, max=4)",
    "    pos.save()",
    "    p = Product()",
    "    p.position = pos",
    "    p.name = f.word()",
    "    p.expire = f.date_time_between(start_date='now', end_date='+30d')",
    "    p.nb = f.random_int(min=0, max=10)",
    "    p.calorie = f.random_int(min=0, max=1000)",
    "    p.save()",
    "",
)
system('echo "%s" | python manage.py shell' % '\n'.join(code))
print '=> Done'

#fake.date_time_between(start_date="-30y", end_date="now")
#fake.iso8601()                                       # 1993-12-04T02:47:48
