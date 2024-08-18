num_input = int(input())
for i in range(num_input):
    a = int(input())
    s = list(map(int, input().split()))
    # print(s)
    if(len(s)>2):
        print("NO")
    if(abs(s[0]-s[1])<2):
        print("NO")
    else:
        print("YES")
