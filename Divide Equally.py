Divide Equally
ProgramID- 9349
The program must accept four positive integers as the input. The program must divide the four integers
into two parts and print YES if the sum of integers in the first part is equal to the sum of integers in the
second part. Else the program must print NO as the output.
Boundary Condition(s):
1 <= Each integer value <= 10^8
Input Format:
The first line contains four positive integers separated by a space.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
17115
Output:
YES
Example Input/Output 2:
Input:
7325
Output:
NO

l=list(map(int,input().split()))
t=sum(l)
 if(t%2!=0):
 dp[0] =True;

print("NO");
exit(0)
ts=t//2;

dp=[False]*(ts+1)
for num in 1:
for j in range(ts,num-1,-1):
dp[j]=dp[j] or dp[j-num];
if(dp[ts]):
print("YES")
else:

print("NO");

