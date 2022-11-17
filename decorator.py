# 不含參數的class-based decorator

class DecoratorClass01(object): # 沒有object也可以運作
    
    def __init__(self, name):
        self.name = name
        
    def __call__(self, *args, **kwargs):
        print(f"do something befor calling {self.name.__name__}")
        self.name(*args, **kwargs)
        print(f"do something after calling {self.name.__name__}")

class DecoratorClass02(object):
    
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
    
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"do something befor calling {func.__name__} with {self.name1}")
            func(*args, **kwargs)
            print(f"do something after calling {func.__name__} with {self.name2}")
        return wrapper

# @DecoratorClass01
@DecoratorClass02('Dan', 'Ken')
def my_func_01():
    print('main')

if __name__ == '__main__':
    my_func_01()