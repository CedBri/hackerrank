# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

for _ in range(N):
    # Get number of cubes
    num_cubes = int(input())
    side_length = list(map(int, input().strip().split()))
    is_good = "Yes"
    
    if max(side_length) not in (side_length[0], side_length[-1]):
        is_good = "No"
    print(is_good)
