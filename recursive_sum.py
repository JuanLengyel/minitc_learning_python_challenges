def recursiveSum(upperRange):
    if upperRange == 1:
        return 1
    
    return upperRange + recursiveSum(upperRange - 1)

def run():
    input_number = int(raw_input("Type the upper limit of the sum: "))
    print(recursiveSum(input_number))

if __name__ == "__main__":
    run()