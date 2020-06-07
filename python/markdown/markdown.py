import re


def enclose(text, tag):
    return f'<{tag}>{text}</{tag}>'


def inline_tag(group, tag):
    return f'{group(1)}{enclose(group(2), tag)}{group(3)}'


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        if re.match('###### (.*)', line) is not None:
            line = enclose(line[7:], 'h6')
        elif re.match('## (.*)', line) is not None:
            line = enclose(line[3:], 'h2')
        elif re.match('# (.*)', line) is not None:
            line = enclose(line[2:], 'h1')
        m = re.match(r'\* (.*)', line)
        if m:
            if not in_list:
                in_list = True
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    curr = inline_tag(m1.group, 'strong')
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    curr = inline_tag(m1.group, 'em')
                line = f'<ul>{enclose(curr, "li")}'
            else:
                is_bold = False
                is_italic = False
                curr = m.group(1)
                m1 = re.match('(.*)__(.*)__(.*)', curr)
                if m1:
                    is_bold = True
                m1 = re.match('(.*)_(.*)_(.*)', curr)
                if m1:
                    is_italic = True
                if is_bold:
                    curr = inline_tag(m1.group, 'strong')
                if is_italic:
                    curr = inline_tag(m1.group, 'em')
                line = enclose(curr, 'li')
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', line)
        if not m:
            line = enclose(line, 'p')
        m = re.match('(.*)__(.*)__(.*)', line)
        if m:
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', line)
        if m:
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    if in_list:
        res += '</ul>'
    return res
