import json
import os

DATA_FILE = "data.json"

# ---------------------------
# Load & Save Helpers
# ---------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------------------
# Student Operations
# ---------------------------
def add_student(data):
    roll = input("Enter roll number: ")
    if roll in data:
        print("⚠️ Student already exists!")
        return
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks (comma separated): ").split(",")))
    data[roll] = {"name": name, "marks": marks}
    print("✅ Student added successfully!")

def view_students(data):
    if not data:
        print("No records found.")
        return
    for roll, info in data.items():
        print(f"{roll} - {info['name']} | Marks: {info['marks']}")

def search_student(data):
    roll = input("Enter roll number to search: ")
    if roll in data:
        print(f"Found: {data[roll]['name']} | Marks: {data[roll]['marks']}")
    else:
        print("❌ Student not found.")

def update_student(data):
    roll = input("Enter roll number to update: ")
    if roll not in data:
        print("❌ Student not found.")
        return
    marks = list(map(int, input("Enter new marks (comma separated): ").split(",")))
    data[roll]["marks"] = marks
    print("✅ Marks updated successfully!")

def delete_student(data):
    roll = input("Enter roll number to delete: ")
    if roll in data:
        del data[roll]
        print("🗑️ Student deleted.")
    else:
        print("❌ Student not found.")

def calculate_stats(data):
    if not data:
        print("No records to calculate.")
        return
    all_marks = [sum(info["marks"]) / len(info["marks"]) for info in data.values()]
    avg = sum(all_marks) / len(all_marks)
    topper = max(data.items(), key=lambda x: sum(x[1]["marks"]) / len(x[1]["marks"]))
    lowest = min(data.items(), key=lambda x: sum(x[1]["marks"]) / len(x[1]["marks"]))
    print(f"📊 Class Average: {avg:.2f}")
    print(f"🏆 Topper: {topper[1]['name']} ({topper[0]})")
    print(f"📉 Lowest: {lowest[1]['name']} ({lowest[0]})")

# ---------------------------
# Main Menu
# ---------------------------
def main():
    data = load_data()
    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Stats")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            calculate_stats(data)
        elif choice == "7":
            save_data(data)
            print("💾 Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
