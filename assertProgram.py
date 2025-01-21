# Function to calculate the square of a number
def square(num):
    return num * num

# Test cases
assert square(2) == 4, "Test case failed: square(2) should return 4"
assert square(3) == 9, "Test case failed: square(3) should return 9"
assert square(0) == 0, "Test case failed: square(0) should return 0"

print("All test cases passed!")

# Failing example
assert square(4) == 16, "Test case failed: square(-2) should return -4"'''
'''def avg(scores):
    assert len(scores)!=0,"The list is empty"
    return sum (scores)/len(scores)
scores2=[67,59,86,75,91]
print("The avg of score score2",avg(scores2))

scores1=[]
print("The avg of score score2",avg(scores1))
