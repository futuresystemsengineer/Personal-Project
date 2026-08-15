def main():
    greeting = str(input("Greeting: "))
    print(f"${value(greeting)}")

def value(greeting=""):
    greeting_lower = greeting.lower()
    if greeting_lower.startswith("h"):
        if greeting_lower.startswith("hello"):
            cash = 0
        else:
            cash = 20
    else:
        cash = 100
    return int(cash)

if __name__ == "__main__":
    main()