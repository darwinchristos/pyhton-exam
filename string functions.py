Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a="Python eXAm"
>>> a.capitalize()
'Python exam'
>>> a.lower()
'python exam'
>>> a.upper()
'PYTHON EXAM'
>>> a.count('y')
1
>>> len(a)
11
>>> find('e')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    find('e')
NameError: name 'find' is not defined
>>> a.find('e')
7
>>> a.swapcase()
'pYTHON ExaM'
>>> a.title()
'Python Exam'
>>> a.split()
['Python', 'eXAm']
