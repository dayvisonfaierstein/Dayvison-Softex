import time

print("Iniciando a Contagem da BOMBA!!!")
time.sleep(2)
for i in range (10, 0, -1):
    time.sleep(2)
    print(i)
print("BUM!!!")
print("Morreu às ", time.ctime(time.time()))