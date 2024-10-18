import psutil
from pprint import pprint

dict1 = {proc.name()+'_'+str(proc.memory_info().rss/1024):proc.memory_info().rss/1024
         for proc in psutil.process_iter()}

print(sum(val for val in dict1.values())/1024/(8*1024)*100)
print(len([val for key,val in dict1.items() if key[:11]=='svchost.exe']))

list1 = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
pprint(list1)

with open('processes.csv', 'w', encoding='utf-8') as file:
    for i in list1:
        print(*i, file = file, sep = ';')