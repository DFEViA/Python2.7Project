#!/usr/bin/python
# -*- coding: UTF-8 -*-

#yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator。

#可以无穷产生奇数的函数
'''def odd():
    n=1
    while True:
        yield n
        n+=2
odd_num = odd()
count = 0
for o in odd_num:
    if count >=5: break
    print(o)
    count +=1'''

#手动编写迭代器可以实现类似的效果
'''class Iter:
    def __init__(self):
        self.start=-1
    def __iter__(self):
        return self
    def next(self):
        self.start +=2 
        return self.start
I = Iter()
for count in range(5):
    print(next(I))'''

#题外话： 生成器是包含有__iter()和next__()方法的，所以可以直接使用for来迭代，而没有包含StopIteration的自编Iter来只能通过手动循环来迭代。
#生成器没有办法使用return来返回值。
#生成器支持的方法
'''
close()

手动关闭生成器函数，后面的调用会直接返回StopIteration异常。

send()

生成器函数最大的特点是可以接受外部传入的一个变量，并根据变量内容计算结果后返回。
这是生成器函数最难理解的地方，也是最重要的地方，实现后面我会讲到的协程就全靠它了。
'''
'''def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive

g=gen()
print(g.send(None))     
print(g.send('aaa'))
print(g.send(3))
print(g.send('e'))'''
'''
执行流程：

通过g.send(None)或者next(g)可以启动生成器函数，并执行到第一个yield语句结束的位置。此时，执行完了yield语句，但是没有给receive赋值。yield value会输出初始值0注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。
通过g.send(‘aaa’)，会传入aaa，并赋值给receive，然后计算出value的值，并回到while头部，执行yield value语句有停止。此时yield value会输出”got: aaa”，然后挂起。
通过g.send(3)，会重复第2步，最后输出结果为”got: 3″
当我们g.send(‘e’)时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。

'''

'''
throw()

用来向生成器函数送入一个异常，可以结束系统定义的异常，或者自定义的异常。
throw()后直接跑出异常并结束程序，或者消耗掉一个yield，或者在没有下一个yield的时候直接进行到程序的结尾。
'''
'''def gen():
    while True: 
        try:
            yield 'normal value'
            yield 'normal value 2'
            print('here')
        except ValueError:
            print('we got ValueError here')
        except TypeError:
            break

g=gen()
print(next(g))
print(g.throw(ValueError))
print(next(g))
print(g.throw(TypeError))'''
'''
print(next(g))：会输出normal value，并停留在yield ‘normal value 2’之前。
由于执行了g.throw(ValueError)，所以会跳过所有后续的try语句，也就是说yield ‘normal value 2’不会被执行，然后进入到except语句，打印出we got ValueError here。然后再次进入到while语句部分，消耗一个yield，所以会输出normal value。
print(next(g))，会执行yield ‘normal value 2’语句，并停留在执行完该语句后的位置。
g.throw(TypeError)：会跳出try语句，从而print(‘here’)不会被执行，然后执行break语句，跳出while循环，然后到达程序结尾，所以跑出StopIteration异常。

'''
'''def flatten(nested):
 
    try:
        #如果是字符串，那么手动抛出TypeError。
        if isinstance(nested, str):
            raise TypeError
        for sublist in nested:
            #yield flatten(sublist)
            for element in flatten(sublist):
                #yield element
                print('got:', element)
    except TypeError:
        #print('here')
        yield nested
 
L=['aaadf',[1,2,3],2,4,[5,[6,[8,[9]],'ddf'],7]]
for num in flatten(L):
    print(num)'''

'''
总结

按照鸭子模型理论，生成器就是一种迭代器，可以使用for进行迭代。
第一次执行next(generator)时，会执行完yield语句后程序进行挂起，所有的参数和状态会进行保存。再一次执行next(generator)时，会从挂起的状态开始往后执行。在遇到程序的结尾或者遇到StopIteration时，循环结束。
可以通过generator.send(arg)来传入参数，这是协程模型。
可以通过generator.throw(exception)来传入一个异常。throw语句会消耗掉一个yield。可以通过generator.close()来手动关闭生成器。
next()等价于send(None)
'''
'''
def test():
    yield 1
    yield 2
    yield 3

g = test()
for i in g:
    print i
'''
def count():
    def sum(b):
        return b
    return sum
c = count()
print c(3)
