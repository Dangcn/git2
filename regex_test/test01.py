
def deduplication(array):
    i = 0
    if array.__class__ != list:
        print("it is not list")
    elif sorted(array) == array or sorted(array,reverse=True)==array:
        if len(array) == 1:
            return len(array)
        else:
            while i<len(array):
                j = i+1
                while j<len(array):
                    if array[i] == array[j]:
                        del array[j]
                    else:
                        break
                i+=1
            return len(array)
    else:
        print("it is not sorted")

if __name__=="__main__":
    # 测试用例一，非列表
    array1 = 'a'
    deduplication(array1)
    # 测试用例二，列表未排序
    array2 = [1,3,2,4]
    deduplication(array2)
    # 测试用例三，列表长度为1
    array3 = [11]
    print(deduplication(array3))
    # 测试用例四，正向排序列表
    array4 = [1,1,2,2,3,4,5,6]
    print(deduplication(array4))
    # 测试用例五，反向排序
    array5 = ['z','y','x','x','b','a']
    print(deduplication(array5))