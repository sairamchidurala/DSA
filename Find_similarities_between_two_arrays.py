"""
You have been given two arrays/list ‘ARR1’ and ‘ARR2’ consisting of ‘N’ and ‘M’ integers respectively.
Your task is to return the number of elements common to ‘ARR1’ and ‘ARR2’ and the number of elements in
the union of ‘ARR1’ and ‘ARR2’.
Example:
Let’s assume ‘ARR1’ is [1,2,3,4,5] and ‘ARR2’ is [2,4,6,8]. Elements common to ‘ARR1’ and ‘ARR2’ are [2,4]
as they occur in both ‘ARR1’ and ‘ARR2’. Therefore the number of elements common to ‘ARR1’ and ‘ARR2’ is 2.
Union of ‘ARR1’ and ‘ARR2’ is [1,2,3,4,5,6,8]. Therefore the number of distinct elements in the union of
‘ARR1’ and ‘ARR2’ is 7. So, the answer will be 2 7.
Note:
1. ‘ARR1’ consists of distinct integers i.e no number occurs twice in array/list.

2. ‘ARR2’ consists of distinct integers i.e no number occurs twice in array/list.
Input Format:
The first line contains a single integer ‘T’ representing the number of test cases.

The first line of each test case contains two single space-separated integers ‘N' and ‘M’ representing the
size of the array/list ‘ARR1’ and ‘ARR2’ respectively.

The second line of input of each test case contains ‘N’ single space-separated integers representing the
array/list elements of ‘ARR1’.

The third line and the last line of input of each test contains ‘M’ single space-separated integers representing
the array/list elements of ‘ARR2’.
Output Format:
For each test case, return the number of elements common to ‘ARR1’ and ‘ARR2’ and the number of distinct elements
in the union of ‘ARR1’ and ‘ARR2’.
Note:
You do not need to print anything; it has already been taken care of. Just implement the function.
Constraints:
1 <= T <= 10
1 <= N <= 1000
1 <= M <= 1000
1 <= ‘arr1[i]’ <= 10^5
1 <= ‘arr2[i]’ <= 10^5

Time Limit: 1sec
Sample Input 1:
2
2 2
1 2
3 4
2 1
2 3
3
Sample Output 1:
0 4
1 2
Sample Output 1 Explanation:
Test case 1:

‘ARR1’ is [1,2]
‘ARR2’ is [3,4]
Elements common to ‘ARR1’ and ‘ARR2’ are []. Therefore the number of elements common to ‘arr’ and ‘brr’ is 0.
The union of ‘ARR1’ and ‘ARR2’ is [1,2,3,4]. Therefore the number of distinct elements in the union of ‘ARR1’
and ‘ARR2’ is 4.

Therefore the answer is 0 4.

Test case 2:

‘ARR1’ is [2,3].
‘ARR2’ is [3]
Elements common to ‘ARR1’ and ‘ARR2’ are [3]. Therefore the number of elements common to ‘ARR1’ and ‘ARR2’ is 1.
The union of ‘ARR1’ and ‘ARR2’ is [2,3]. Therefore the number of distinct elements in the union of ‘ARR1’ and
‘ARR2’ is 2.

Therefore the answer is 1 2.
Sample Input 2:
2
5 3
1 2 3 4 5
4 6 2
1 2
1
3 2
Sample Output 2:
2 6
0 3
"""


def findSimilarity(arr1, arr2, n, m):
	res = []
	c = 0
	for i in arr1+arr2:
		if i not in res:
			res.append(i)
	for i in arr1:
		if i in arr2:
			c += 1
			arr2.remove(i)
	return c, len(res)


for _ in range(int(input())):
	n, m = map(int, input().split())
	arr1 = list(map(int, input().split()))
	arr2 = list(map(int, input().split()))
	res = findSimilarity(arr1, arr2, n, m)
	print(res[0], res[1])
