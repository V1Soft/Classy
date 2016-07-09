class Object(object):
    def __init__(self, key, attribs):
        self.key = key
        self.attribs = attribs

class Attribute(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
classes = []

def parse(source):
    parsedScript = [[]]
    word = ''
    for char in source:
        if char == '{':
            parsedScript.append([])
            if word:
                parsedScript[-1].append(word)
                word = ''
        elif char == '}':
            if word:
                parsedScript[-1].append(word)
                word = ''
            temp = parsedScript.pop()
            parsedScript[-1].append(temp)
        elif char in ('\t', '\n'):
            if word:
                parsedScript[-1].append(word)
                word = ''
        else:
            word += char
    return parsedScript[0]

def lex(parsedScript):
    attributes = []
    for word in parsedScript:
        for attrib in word[1:]:
            attributes.append(Attribute(attrib.split(' ')[0], attrib.split(' ')[1]))
        if word[0].endswith(' '):
            classes.append(Object(word[:-1], attributes))
        else:
            classes.append(Object(word[0], attributes))
    
print(parse('''foobar {\tfoo bar\n\tbar foo\n}'''))
lex(parse('''foobar {\tfoo bar\n\tbar foo\n}'''))
for obj in classes:
    print('obj key: >' + obj.key + '<')
    for attr in obj.attribs:
        print('\tattr key: >' + attr.key + '<')
        print('\tattr value: >' + attr.value + '<')
