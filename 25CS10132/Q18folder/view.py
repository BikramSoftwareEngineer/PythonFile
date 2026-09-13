class ReportView:
    @staticmethod
    def show_menu():
        print("\n--- Salary Report Generator ---")
        print("1. View Detailed Salary Report by Department")
        print("2. View Overall Department-Wise Summary")
        print("3. Exit")
        return input("Enter choice (1-3): ")

    @staticmethod
    def get_department_input():
        return input("Enter Department Name (e.g., IT, HR, Finance): ")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_department_report(department, records):
        print(f"\n--- Salary Report for Department: {department} ---")
        if not records:
            print("No records found for this department.")
            return

        print(f"{'ID':<6} {'Name':<15} {'Designation':<18} {'Salary (₹)':<10}")
        print("-" * 55)
        for row in records:
            print(f"{row[0]:<6} {row[1]:<15} {row[2]:<18} {row[3]:<10.2f}")

    @staticmethod
    def display_summary_report(summary):
        print("\n--- Department-Wise Salary Summary ---")
        if not summary:
            print("No employee data available.")
            return

        print(f"{'Department':<15} {'Employees':<10} {'Total Salary (₹)':<18} {'Avg Salary (₹)':<15}")
        print("-" * 62)
        for row in summary:
            print(f"{row[0]:<15} {row[1]:<10} {row[2]:<18.2f} {row[3]:<15.2f}")