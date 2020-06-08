import re


def enclose(text, tag):
    return f'<{tag}>{text}</{tag}>'


def inline_tag(group, tag):
    return f'{group(1)}{enclose(group(2), tag)}{group(3)}'


def check_for_formatting(text):
    if match := re.match('(.*)__(.*)__(.*)', text):
        text = inline_tag(match.group, 'strong')
    if match := re.match('(.*)_(.*)_(.*)', text):
        text = inline_tag(match.group, 'em')
    return text


def check_headings(line):
    for i in range(6, 0, -1):
        if re.match(f'{"#"*i} (.*)', line):
            return enclose(line[i+1:], f'h{i}')
    return line


def parse(markdown):
    res = ''
    in_list = in_list_append = False
    for line in markdown.split('\n'):
        line = check_headings(line)
        if match := re.match(r'\* (.*)', line):
            if not in_list:
                in_list = True
                curr = check_for_formatting(match.group(1))
                line = f'<ul>{enclose(curr, "li")}'
            else:
                curr = check_for_formatting(match.group(1))
                line = enclose(curr, 'li')
        else:
            in_list_append = in_list if in_list else in_list_append
            in_list = False

        line = check_for_formatting(line)
        line = line if re.match('<h|<ul|<li', line) else enclose(line, 'p')
        line = '</ul>' + line if in_list_append else line
        in_list_append = False
        res += line
    res += '</ul>' if in_list else ''
    return res