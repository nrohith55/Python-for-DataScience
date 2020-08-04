
import re
a = '''Amit
saxena
Rohith 
raj
?pushpha

'''
var = re.compile(r'\bpu')

matches= var.findall(a)

print(matches)
