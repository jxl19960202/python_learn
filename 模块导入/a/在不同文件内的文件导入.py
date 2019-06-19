#在a/'在不同文件内的文件导入 导入b文件夹下的2.py文件
new_path = os.path.dirname(os.path.dirname(__file__))#os.path.dirname(__file__)返回该文件的上一级文件
sys.path.append(new_path)
m1 = __import__('b.2')
