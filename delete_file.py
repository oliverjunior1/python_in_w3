# import os
# os.remove('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\demofile2.txt')
###############################################
import os
if os.path.exists('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\demofile2.txt'):
    os.remove('C:\\Users\\Olive\\Downloads\\Visual Studio Code\\W3\\python\\demofile2.txt')
else:
    print('The file does not exist')
###############################################

