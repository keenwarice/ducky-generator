from itertools import product

def generate_ducky_script(password_length):
    filename = f"ducky_script_{password_length}.txt"
    with open(filename, "w") as f:
        for i in range(10):
            f.write(f"STRING {str(i) * password_length}\nENTER\n")
        for combo in product(range(10), repeat=password_length):
            if len(set(combo)) > 1:
                f.write(f"STRING {''.join(map(str, combo))}\nENTER\n")
    print(f"ducky script saved as {filename}")

password_length = int(input("enter password length: "))
generate_ducky_script(password_length)
