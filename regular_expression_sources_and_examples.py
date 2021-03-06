# -*- coding: utf-8 -*-
"""Regular Expression Sources and Examples.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OtXGLZ23RihaCb3hyei7AS2kd8CLjrh6

<a href="https://docs.python.org/3/library/re.html#module-re"> Python Standard Library re</a>

<a href="https://regex101.com/"> Test regular expression here </a>

<a href="https://github.com/ziishaned/learn-regex"> learn-regex github </a>

# Checking a Pair
"""

def displaymatch(match):
  if not match:
    return None
  return '<Match: %r, groups=%r>' % (match.group(), match.groups())

import re
valid = re.compile(r'^[a2-9tjqk]{5}')

displaymatch(valid.match('akt5q'))

pair = re.compile(r'.*(.).*\1')

displaymatch(pair.match('717ak'))

displaymatch(pair.match('354aa'))

"""# Making a Phone Book"""

text = """Ross McFluff 834.345.1254 155 Elm Street

Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way

Heather Albrecht: 548.326.4584 919 Park Place"""

import re
entries = re.split(r'\n+', text)

entries

[re.split(r':? ', entry, maxsplit=3) for entry in entries]

"""# Text Munging"""

def repl(m):
  import random
  innerWord = list(m.group(2))
  print(innerWord)
  random.shuffle(innerWord)
  print(innerWord)
  return m.group(1) + ''.join(innerWord) + m.group(3)

text = "Professor Abdolmalek, please report your absense promptly."
re.sub('(\w)(\w+)(\w)', repl, text)

import random
random.shuffle?

text = "He was carefully disguised but captured quickly by police."
re.findall(r'\w+ly', text)

for m in re.finditer(r'\w+ly', text):
  print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

re.match(r"\W(.)\1\W", " ff ")

re.match('\W(.)\1\W',' ff ')

re.match('\\W(.)\\1\\W',' ff ')

import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

"""# Writing a Tokenizer"""

import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line', 'column'])

def tokenize(code):
    keywords = {'IF', 'THEN', 'ENDIF', 'FOR', 'NEXT', 'GOSUB', 'RETURN'}
    token_specification = [
        ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',   r':='),           # Assignment operator
        ('END',      r';'),            # Statement terminator
        ('ID',       r'[A-Za-z]+'),    # Identifiers
        ('OP',       r'[+\-*\/]'),      # Arithmetic operators
        ('NEWLINE',  r'\n'),           # Line endings
        ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH', r'.'),            # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
        elif kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield Token(kind, value, line_num, column)

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

for token in tokenize(statements):
    print(token)

print(tokenRegex)

tokenRegex = r'(?P<NUMBER>\d+(\.\d*)?)|(?P<ASSIGN>:=)|(?P<END>;)|(?P<ID>[A-Za-z]+)|(?P<OP>\+\-\*\/)|(?P<NEWLINE>\n)|(?P<SKIP>[ \t]+)|(?P<MISMATCH>.)'

statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

re.finditer(tokenRegex, statements)

for mo in re.finditer(tokenRegex, statements):
  print(mo.lastgroup)
  print(mo.group())
  print(mo.start())
  print(mo.end())

