from functools import wraps

# 不含參數的function-based Decorator

def decorator_01(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'do something before calling function {func.__name__}')
        func(*args, **kwargs)
        print(f'do something after calling function {func.__name__}')
    return wrapper

def decorator_02(t01, t02):
    def outer_wrapper(func): #
        @wraps(func)
        def wrapper(*args, **kwargs): # 執行第二層，wrapper function
            print(f'do something before calling function {func.__name__} with {t01}') # 先執行
            func(*args, **kwargs) # 第二執行順序, ,main function
            print(f'do something after calling function {func.__name__} with {t02}') # 最後執行
        return wrapper # 3. 呼叫僅接收function地址，會自動被裝飾器傳入
    return outer_wrapper # 傳到第一層function

@decorator_02('Dan', 'Ken') # 2. 發現有裝飾器，先執行decorator function
def main():
    print('main test')
    
if __name__ == '__main__':
    main() # 1. 執行main function