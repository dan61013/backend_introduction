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

@odd_func
def random_func(*args, **kwargs):
    input_num = random.randint(*args, **kwargs)
    return input_num

if __name__ == "__main__":
    # main()
    random_func(1, 1000)