def calculate_average(scores):
    return sum(scores) / len(scores)

def find_highest(scores):
    return max(scores)

def find_lowest(scores):
    return min(scores)

def process_scores(scores):
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

if __name__ == "__main__":
    scores = [85, 90, 78, 92, 88]
    process_scores(scores)