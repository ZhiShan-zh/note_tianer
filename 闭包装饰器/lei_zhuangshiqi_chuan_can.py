
def add(num):
    class Check(object):
        # 使用类创建实例对象时，给实例对象赋予初始化的一些属性
        def __init__(self, fn):  # fn = comment
            self.__fn = fn

        def __call__(self, *args, **kwargs):
            print("登陆")
            print(num)
            self.__fn(*args, **kwargs)  # comment()

    return Check



# 被装饰的函数
@add(8)  # comment = Check(comment)
def comment(a, b):
    print("发表评论")
    print(a + b)


comment(6, 6)
