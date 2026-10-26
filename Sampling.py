import numpy as np

np.random.seed(42)
puppies = np.array([1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1])

p = puppies.mean()
print("Mean", p)
print("Standard Deviation", puppies.std())
print("Variance", puppies.var())

np.random.choice(puppies, size = (1, 5), replace = True)
np.random.choice(puppies, size = (1, 5), replace = True).mean()

print("\nSampling distribution with size 5\n")
samplep = []

for i in range(10000): 
    sample = np.random.choice(puppies, 5, replace = True)
    samplep.append(sample.mean())
    samplep = np.array(samplep)

sm = samplep.mean()

print("Mean", samplep.mean())
print("Standard Deviation", samplep.std())
print("Variance", samplep.var())

print("\nSampling distribution with size 20\n")
twenty_samplep = []

for i in range(10000): 
    sample = np.random.choice(puppies, 20, replace = True)
    twenty_samplep.append(sample.mean())
    twenty_samplep = np.array(twenty_samplep)

print("New Mean", twenty_samplep.mean())
print("New Standard Deviation", twenty_samplep.std())
print("New Variance", twenty_samplep.var())