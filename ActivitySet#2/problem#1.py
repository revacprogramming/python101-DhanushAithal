

def add(a, b):
    return  a+b


def main():
    a = int(input("Enter 1st Number? "))
    b = int(input("Enter 2nd Number? "))

    c = add(a, b)
    print(f"sum of {a} and {b} is  {c}")

if __name__=='__main__':
 main()