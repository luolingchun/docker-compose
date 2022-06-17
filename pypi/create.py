# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2021/2/8 17:19
from bandersnatch import main

temp = """1 23 * * * bandersnatch sync {cmd} >> /var/log/pypi.log\n# Don't remove this line ."""

with open('requirements.txt', 'r') as f:
    lines = f.readlines()
cmd = ' '.join([line.split('==')[0] for line in lines])

cron = temp.format(cmd=cmd)
print(cron)

with open('crontab', 'w', newline='\n') as f:
    f.write(cron)

print('success')
