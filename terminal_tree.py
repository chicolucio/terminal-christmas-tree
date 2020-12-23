def tree(height=13, screen_width=80):
    star = ('*', '***')
    if height % 2 != 0:
        height += 1
    body = ['/_\\', '/_\_\\']
    trunk = '[___]'
    begin = '/'
    end = '\\'
    pattern = '_/'
    j = 5
    for i in range(7, height + 1, 2):
        middle = pattern + (i - j) * pattern
        line = ''.join([begin, middle[:-1], end])
        body.append(line)
        middle = middle.replace('/', '\\')
        line = ''.join([begin, middle[:-1], end])
        body.append(line)
        j += 1

    return '\n'.join(line.center(screen_width) for line in (*star, *body, trunk))


if __name__ == '__main__':
    print(tree())