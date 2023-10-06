
def check(s):
  A = {'a', 'e', 'i', 'o', 'u'}
 
  if len(A.difference(set(s.lower())))==0:
    print('accepted')
  else:
    print('not accepted')

s='SEEquoiaL'

check(s)
