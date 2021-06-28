def gcd(a, b):
    if a <= 0:
        return b
    elif b <= 0:
        return a

    if a > b:
        num1 = a
        num2 = b
    else:
        num1 = b
        num2 = a

    return gcd(num1%num2, num2)

def lcm(a, b):
    return (a*b) / gcd(a, b)

nums = []

for i in range(0, 2, 1):
    nums.append( int(input('정수' + str(i+1) + ' 입력  :  ')) )

print( str(nums[0]) + ',  ' + str(nums[1]) + '의 최대공약수  : ', gcd(nums[0], nums[1]) )
print( str(nums[0]) + ',  ' + str(nums[1]) + '의 최소공배수  : ', lcm(nums[0], nums[1]) )
