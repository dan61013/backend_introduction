import random

def main():
    """
    雙層巢狀迴圈
    """
    for i in 'ABCD':
        for j in range(1,6):
            print("{} - {}".format(i, j))

# 裝飾器 odd_fun & random_fun
def odd_func(func):
    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if (int)(num) % 2 != 0:
            print("{}為奇數".format(num))
        else:
            print("{}為偶數".format(num))
    return wrapper

def decorator_01(func):
    def wrapper(*args):
        print('裝飾器1開始')
        func(*args)
        print('裝飾器1結束')
    return wrapper

def decorator_02(func):
    def wrapper(*args):
        print('裝飾器2開始')
        func(*args)
        print('裝飾器2結束')
    return wrapper

@odd_func
def random_func(*args, **kwargs):
    input_num = random.randint(*args, **kwargs)
    return input_num

@decorator_01
@decorator_02
def function_01(*args):
    print("我是函數 傳入參數為: {}".format(*args))
    
def factory_01(num):
    def odd_found(func):
        def wrapper():
            if int(num) % 2 != 0:
                print("{} 判斷為奇數".format(num))
            else:
                print("{} 判斷為偶數".format(num))
            func()
        return wrapper
    return odd_found

@factory_01(random.randint(1,10))
def function_02():
    print('我才是本體')

if __name__ == "__main__":
    # main()
    # random_func(1, 1000)
    # function_01(123)
    function_02()