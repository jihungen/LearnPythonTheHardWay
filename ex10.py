# -*- coding: utf-8 -*-
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

single_quote_cat = 'I\'m using single-quote in single-quote.'
double_quote_cat = "I'm using \"double-quote\" in double-quote."
korean_cat = u'나는 한국 고양이.'
backspace_cat = 'I\'m a backspace cat\b.'
combined_cat = 'I\'m combining the escape sequences like \'%s\'.'

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print single_quote_cat
print double_quote_cat
print korean_cat
print backspace_cat
print combined_cat % 'this'

# %r show the character that I exactly typed.
print 'Use r for printing %r' % backspace_cat
print 'Use s for printing %s' % backspace_cat

# infinite loop. Randomly choose the one of sticks
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
