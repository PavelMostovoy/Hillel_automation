from data import generate_data

our_data = generate_data(5)
new_data = generate_data(12)

print(next(our_data))
print(next(our_data))
print(next(our_data))
print(next(our_data))
print("*" * 8)
print(next(new_data))
print(next(new_data))
print(next(new_data))
print(next(new_data))
