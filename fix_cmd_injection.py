with open('notes/command-injection.md', 'r') as f:
    content = f.read()

old = '## Blacklisted Command Bypass'
first_idx = content.find(old)
if first_idx != -1:
    second_idx = content.find(old, first_idx + 1)
    if second_idx != -1:
        content = content[:second_idx] + '### Blacklisted Command Bypass' + content[second_idx+len(old):]

lines = content.split('\n')
in_win_table = False
new_lines = []
for i, line in enumerate(lines):
    if '### Blacklisted Command Bypass' in line and i > 60:
        in_win_table = True
        new_lines.append(line)
        continue
    if in_win_table and line.startswith('|'):
        parts = line.split('|')
        stripped = [p.strip() for p in parts]
        if len(stripped) >= 4:
            col1 = stripped[1]
            col2 = stripped[2]
            new_lines.append('| ' + col2.ljust(40) + ' | ' + col1.ljust(93) + ' |')
        else:
            new_lines.append(line)
    else:
        if in_win_table and not line.startswith('|'):
            in_win_table = False
        new_lines.append(line)

with open('notes/command-injection.md', 'w') as f:
    f.write('\n'.join(new_lines))

print('Done')
