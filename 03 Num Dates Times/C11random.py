import random
# example 01
values = [1, 2, 3, 4, 5, 6]
random.choice(values)

# sampling
random.sample(values, 2)

# shuffle
random.shuffle(values)

# randint
random.randint(0, 100)

# random
random.random()

# getrandbits
random.getrandbits(200)

# seed
random.seed() # Seed based on system time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data