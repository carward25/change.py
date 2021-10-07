#
C = int(input("Please enter an amount in cents less than a dollar: "))

print("Your change will be:",)

print("Q: ", C//25)
C = C%25
print("D :", C//10)
C = C%10
print("N: ", C//5)
C = C%5
print("P: ", C//1)
C = C%1

