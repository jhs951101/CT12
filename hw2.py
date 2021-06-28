nums = []

for i in range(0, 5, 1):
    nums.append( int(input('정수 입력  :  ')) )

print('원본 리스트  :   ', nums)
print('결과 리스트  :   ', list(filter(lambda x: x%3 == 0, nums)) )
