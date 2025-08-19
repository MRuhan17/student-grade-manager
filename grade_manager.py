import json
import matplotlib.pyplot as plt

# Load data from JSON file
def load_data(filename="data.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Save data back to JSON
def save_data(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Calculate average marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Assign grade based on average
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

# Display all students with their grades
def display_students(data):
    print("\n--- Student Records ---")
    for roll, info in data.items():
        avg = calculate_average(info["marks"])
        grade = assign_grade(avg)
        print(f"{info['name']} (Roll {roll}) -> Average: {avg:.2f}, Grade: {grade}")

# Visualization: Average Marks per Student
def visualize_data(data):
    names = [info["name"] for info in data.values()]
    averages = [calculate_average(info["marks"]) for info in data.values()]

    plt.figure(figsize=(8, 5))
    plt.bar(names, averages, color="skyblue", edgecolor="black")
    plt.xlabel("Students")
    plt.ylabel("Average Marks")
    plt.title("Average Marks per Student")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()

# Leaderboard visualization (sorted by rank)
def leaderboard(data):
    # Sort students by average descending
    sorted_data = sorted(data.items(), key=lambda x: calculate_average(x[1]["marks"]), reverse=True)
    
    names = [info["name"] for _, info in sorted_data]
    averages = [calculate_average(info["marks"]) for _, info in sorted_data]

    plt.figure(figsize=(8, 5))
    bars = plt.barh(names, averages, color="lightgreen", edgecolor="black")
    plt.xlabel("Average Marks")
    plt.title("Leaderboard - Top Students")
    plt.gca().invert_yaxis()  # Top scorer on top
    
    # Add average labels next to bars
    for bar, avg in zip(bars, averages):
        plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                 f"{avg:.1f}", va="center")

    plt.tight_layout()
    plt.show()

# Main menu
def main():
    data = load_data()

    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Display all students")
        print("2. Add a new student")
        print("3. Visualize student averages")
        print("4. Show Leaderboard")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_students(data)
        elif choice == "2":
            roll = input("Enter Roll Number: ")
            name = input("Enter Student Name: ")
            marks = list(map(int, input("Enter marks separated by space: ").split()))
            data[roll] = {"name": name, "marks": marks}
            save_data(data)
            print("Student added successfully!")
        elif choice == "3":
            visualize_data(data)
        elif choice == "4":
            leaderboard(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
