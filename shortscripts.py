#-- Factorising numbers
import primefac

print("Give an integer: ")
num = int(input())
out = list(primefac.primefac(num))
print("The factors are: ", out)

#-- Increase dimensionality of array
x[np.newaxis,:]
# or
x[:,np.newaxis]

#-- Tile arrays (replicate matrices)
np.tile(x[np.newaxis,:],(2,1))
