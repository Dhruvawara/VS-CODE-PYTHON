# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())

#     x = list(arr)
#     m = max(x)
#     x.sort()
#     for y in range(len(x)):
#         if x[y] == m:
#             x[y] = -100

#     print(max(x))











# if __name__ == '__main__':
#     ls = []
#     x=int(input())
#     for _ in range(x):
#         name = input()
#         score = float(input())
#         ls.append([name,score])
#     print(ls)
#     ls.sort()
#     print(ls)

#     m= 100
#     for y in range(len(ls)):
#         if ls[y][1] < m:
#             m = ls[y][1]

#     print(m) 
    
#     for y in range(len(ls)):
#         if ls[y][1] == m:
#             ls[y][1] = 100
    
#     print(ls)
#     m=100
#     for y in range(len(ls)):
#         if ls[y][1] < m:
#             m = ls[y][1]

#     print(m)
#     for y in range(len(ls)):
#         if ls[y][1] == m:
#             print(ls[y][0])

#     print(ls)    
    





# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     # print(student_marks['Malika'])
#     query_name = input()

#     x = student_marks[query_name]
#     print("%.2f"%(sum(x)/len(x)))




# def mutate_string(string, position, character):
#     x= list(string)
#     x[position] = character
#     return ''.join(x)

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)






