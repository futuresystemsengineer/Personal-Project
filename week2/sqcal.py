def main():
    n = int(input("Number: "))
    print(f"{n} squared is", square(n))

def square(n):
    return n * n

if __name__ == "__main__":
    main()