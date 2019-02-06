# N = int(input())
# P = 0.1 * int(input())

# def sqrtFun(N):
#     sqrt = N ** 0.5
#     return sqrt
    

# ans = round(sqrtFun(N),P)
# print(ans)
# ans = sqrtFun(N,P)
# print('%{0}f'.format(P) %ans)
#1
number = int(input("Enter a number to find the square root : "))
P = 0.1 * int(input())
#2
if number < 0 :
  print("Please enter a valid number.")
else :
  #3
  sq_root = number ** 0.5
  #4
  print("Square root of {} is {} ".format(number,sq_root))