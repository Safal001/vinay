n = int(input("Enter number of tests: "))

marks = []

for i in range(n):
    marks.append(int(input("Enter marks: ")))

longest = [marks[0]]
current = [marks[0]]

start = 1
longest_start = 1

for i in range(1, n):
    if marks[i] > marks[i - 1]:
        current.append(marks[i])
    else:
        if len(current) > len(longest):
            longest = current
            longest_start = start

        current = [marks[i]]
        start = i + 1

if len(current) > len(longest):
    longest = current
    longest_start = start

longest_end = longest_start + len(longest) - 1

print("Longest improving sequence:", tuple(longest))
print("Number of tests:", len(longest))
print("Test range:", (longest_start, longest_end))