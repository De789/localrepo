# print("hello world")

# class Outer():
#     def f1(self):
#         print("outer function")
#     class inner():
#         def f2(self):
#             print("inner function")

# Outer().inner().f2()
# l=[12,210,34,3,67,76]
# max=l[0]
# position=0 
# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
#         position=i
# print(f"Maximum number :{max} with position :{position}")


original=[1,2,[21,32,45],8]

def nested_list(original):
    new=[]
    for item in original:
        if isinstance(item,list):
           new.extend(nested_list(item))
        else:
            new.append(item)
    return new 
print(nested_list(original))
    


