# Open the file and read lines into a list
with open('/mnt/D_Drive/VS CODE/GIT/ASCII-pookalam/plan2.txt', 'r') as file:
    lines = file.read().strip().split('\n')

# Iterate through each line and print it
for line in lines:
    print(line)
