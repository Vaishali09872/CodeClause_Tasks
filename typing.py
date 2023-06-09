import time

def typing_test():
    prompt = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence as quickly and accurately as possible:")
    print(prompt)
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    elapsed_time = end_time - start_time
    accuracy = sum([1 for i in range(len(prompt)) if prompt[i] == user_input[i]]) / len(prompt)
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Accuracy: {accuracy:.0%}")

if __name__ == "__main__":
    typing_test()