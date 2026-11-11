"Student Grade Management System"

GRADE_SCALE = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]


def get_valid_mark(subject):
   while True:
      raw = input(f" Enter mark for {subject} (0-100): ").strip()
      try:
         mark = float(raw)
      except ValueError:
         print(" Invalid input: please enter a number.")
         continue
      if 0 <= mark <= 100:
         return mark
      print(" Invalid input: mark must be between 0 and 100.")


def get_valid_count(prompt):
   while True:
      raw = input(prompt).strip()
      if raw.isdigit() and int(raw) > 0:
         return int(raw)
      print(" Invalid input: enter a whole number greater than 0.")


def calculate_average(marks):
  return sum(marks) / len(marks)


def get_letter_grade(average):
   for cutoff, letter in GRADE_SCALE:
     if average >= cutoff:
         return letter

     
def display_results(students):
    print("\n" + "=" * 52)
    print(f"{'Student':<20}{'Average':>10}{'Grade':>8}")
    print("-" * 52)
    for name, marks in students:
       avg = calculate_average(marks)
       print(f"{name:<20}{avg:>10.2f}{get_letter_grade(avg):>8}")
    print("=" * 52)


def main():
  students = []
  print("STUDENT GRADE MANAGEMENT SYSTEM")
  while True:
   name = input("\nStudent name: ").strip()
   if not name:
      print(" Invalid input: name cannot be empty.")
      continue
   count = get_valid_count("Number of subjects: ")
   marks = [get_valid_mark(f"subject {i}") for i in range(1, count + 1)]
   students.append((name, marks))
   if input("Add another student? (y/n): ").strip().lower() != "y":
      break
  display_results(students)

if __name__ == "__main__":
 main()