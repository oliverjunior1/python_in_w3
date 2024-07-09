# import re

# txt = 'The rain in Spain'
# x = re.search('^The.*Spain$', txt)

# if x:
#     print('Yes! We have a match!')
# else:
#     print('No match')

###############################################

# import re

# txt = 'The rain in Spain'
# x = re.search("Portugal", txt)
# print(x)

###############################################

# import re

# txt = 'The rain in Spain'
# x = re.split('\s', txt)
# print(x)

###############################################
# import re

# txt = 'The rain in Spain'
# x = re.split('\s', txt, 1)
# print(x)
###############################################
# import re

# txt = 'The rain in Spain'
# x = re.sub('\s', '9', txt)
# print(x)
###############################################
# import re

# txt = 'The rain in Spain'
# x = re.sub('\s', '9', txt, 2)
# print(x)

###############################################
# import re

# txt = 'The rain in Spain'
# x = re.search('ai', txt)
# print(x)
###############################################
# import re

# txt = 'The rain in Spain'
# x = re.search(r'\bS\w+', txt)
# print(x.span())

###############################################
# import re

# txt = 'The rain in Spain'
# x = re.search(r'\bS\w+', txt)
# print(x.string)
###############################################
import re

txt = 'The rain in Spain'
x = re.search(r'\bS\w+', txt)
print(x.group())
###############################################
###############################################