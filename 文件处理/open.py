import time
with open('jxl','w+',encoding='utf-8') as f:
    t = time.asctime()
    f.write(t)     #写完之后，光标位置在最后
    f.seek(0)
    a = f.readlines()
print(a)











