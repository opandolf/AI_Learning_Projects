from preprocess import preprocess_values
import pandas as pd

data = preprocess_values()

df = pd.DataFrame(data).transpose()
# print(df.head(10))
# print(df.tail())

# prev = data[(str([0,1,1,1,0,0,0,0,0]), 4)]['value'] + data[(str([0,0,0,0,0,1,1,0,0]), 4)]['value']
# actual = data[(str([0,1,1,1,1,0,0,0,0]), 4)]['value'] + data[(str([0,0,0,0,1,1,1,0,0]), 4)]['value']
# print(actual - prev)

# print(data[(str([0,0,0,0,-1,-1,0,0,0]), 4)])
# print(data[(str([0,0,0,-1,-1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,-1,0,0,0]), 4)])
# print(data[(str([0,0,0,1,-1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,1,0,0,0]), 4)])
# print(data[(str([0,0,0,1,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print()

# print(data[(str([0,0,0,0,-1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,-1,1,1,1,0]), 4)])
# print(data[(str([0,0,0,-1,1,1,1,0,0]), 4)])
# print(data[(str([0,0,-1,1,1,1,0,0,0]), 4)])
# print(data[(str([0,-1,1,1,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,-1,1,0,0,0]), 4)])
# print(data[(str([0,0,0,-1,1,0,0,0,0]), 4)])
# print()


# print(data[(str([0,0,0,0,-1,-1,0,0,0]), 4)])
# print(data[(str([0,0,0,-1,-1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,-1,1,1,0,0]), 4)])
# print(data[(str([0,0,0,-1,1,1,0,0,0]), 4)])
# print(data[(str([0,0,-1,1,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print()

# print(data[(str([0,0,0,0,-1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,-1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,-1,1,0,0,0]), 4)])
# print(data[(str([0,0,0,-1,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,1,0,0,0]), 4)])
# print(data[(str([0,0,0,1,1,0,0,0,0]), 4)])
# print()

# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)])
# print("----------------------------------")

# print(-data[(str([0,0,0,0,0,0,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,-1,0,0,0,0]), 4)]['value'])
# print()

# print(-data[(str([0,0,0,0,0,1,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,-1,1,0,0,0]), 4)]['value'])
# print()

# print(-data[(str([0,0,0,0,0,0,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,-1,0,0,0,0]), 4)]['value'])
# print()

# print(-data[(str([0,0,0,0,0,0,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,-1,0,0,0,0]), 4)]['value'])
# print("----------------------------------")

# print(-data[(str([0,0,0,0,0,-1,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,1,-1,0,0,0]), 4)]['value'])
# print()

# print(-data[(str([0,0,0,0,0,0,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)]['value'])
# print()

# print(-data[(str([0,0,0,0,0,1,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,1,1,0,0,0]), 4)]['value'])
# print()

# print(-data[(str([0,0,0,0,0,0,0,0,0]), 4)]['value'])
# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)]['value'])


# print(data[(str([1,-1,-1,1]), 3)])
# print(data[(str([1,-1,-1,1]), 0)])

# print(data[(str([0,1,-1,-1,1,0,-1,1,0]), 4)])

# print(data[(str([0,0,0,0,1,0,0,0,0]), 4)]['value'] * 4)
# print()

# print(data[(str([0,0,0,0,1,0,0,1,0]), 4)]['value'] * 1)
# print(-data[(str([0,0,0,0,0,0,0,1,0]), 4)]['value'] * 1)
# print(data[(str([0,1,0,0,1,0,0,0,0]), 4)]['value'] * 1)

print(-data[(str([0,0,-1,1,0,0,0,0,0]), 4)]['value'])
print(data[(str([0,0,-1,1,1,0,0,0,0]), 4)]['value'])

