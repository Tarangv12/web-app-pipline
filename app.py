import sys

def process_data():
    print("--- Starting Data Processing ---")
    data = [10, 20, 30, 40]
    total = sum(data)
    
    print(f"Data: {data}")
    print(f"Calculated Total: {total}")
    
    expected_total = 100
    if total != expected_total:
        print(f"ERROR: Expected {expected_total}, but got {total}")
        sys.exit(1)
    else:
        print("SUCCESS: Logic check passed!")

if __name__ == "__main__":
    process_data()