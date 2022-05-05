"""
You are given an array ‘Arr’ consisting of ‘N’ distinct integers and a positive integer ‘K’. Find out Kth smallest and Kth largest element of the array. It is guaranteed that K is not greater than the size of the array.
Example:
Let ‘N’ = 4,  ‘Arr’ be [1, 2, 5, 4] and ‘K’ = 3.
then the elements of this array in ascending order is [1, 2, 4, 5].  Clearly, the 3rd smallest and largest element of this array is 4 and 2 respectively.
Input Format:
The first line of input contains an integer ‘T’ denoting the number of test cases.
The next 2*T lines represent the ‘T’ test cases.

The first line of each test case contains two space-separated integers  ‘N’ and ‘K’ respectively.

The second line of the test case contains ‘N’ space-separated integers representing elements of the array ‘Arr’.
Output Format :
For each test case, print a line consisting of two space-separated integers that represent the Kth smallest and Kth largest elements of the array.
Note:
You do not need to print anything, it has already been taken care of. Just implement the given function. In the given function, you need to return an array consisting of 2 integers, where the first integer gives Kth smallest element and the second integer gives the Kth largest element.
Constraints:
1 <= T <= 50
1 <= N <= 10^4
1 <= K <= N
-10^9 <= Arr[i] <= 10^9

Where ‘T’ is the total number of test cases, ‘N’ is the size of array ‘Arr’ and Arr[i] is the element of the given array.

Time limit: 1 sec
Sample Input 1:
2
4 4
5 6 7 2
4 3
1 2 5 4
Sample Output 1:
7 2
4 2
Explanation Of Sample Input 1:
Test case 1:
Here, ‘N’ = 4, ‘Arr’ = [5, 6, 7, 2] and ‘K’ = 3.
Elements of the array in ascending order are [2, 5, 6, 7]
Thus the 4rd smallest and 4rd largest elements of this array are 7 and 2 respectively.

Test case 2:
See problem statement for an explanation.
Sample Input 2:
 2
 1 1
 2
 5 1
 5 4 3 2 1
Sample Output 2:
 2 2
 1 5
"""


def kthSmallLarge(arr, n, k):
    # Write your code here
    arr.sort()
    return arr[k-1], arr[-k]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(kthSmallLarge(arr, n, k))
