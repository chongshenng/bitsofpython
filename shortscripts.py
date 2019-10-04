#-- Factorising numbers
import primefac

print("Give an integer: ")
num = int(input())
out = list(primefac.primefac(num))
print("The factors are: ", out)
