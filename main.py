a, first, second, third = input(), input(), input(), input()

a = a.replace(' ', '')
a = a.replace('(', '')
a = a.replace(')', '')
a = a.replace('-', '')
a = a.replace('+7', '8')

if len(a) == 7:
    a = '8495' + a

nums = [first, second, third]

for i in range(len(nums)):
    nums[i] = nums[i].replace(' ', '')
    nums[i] = nums[i].replace('(', '')
    nums[i] = nums[i].replace(')', '')
    nums[i] =nums[i].replace('-', '')
    nums[i] = nums[i].replace('+7', '8')

for i in nums:
    if len(i) == 7:
        i = '8495' + i
    if i == a:
        print('YES')
    else:
        print('NO')