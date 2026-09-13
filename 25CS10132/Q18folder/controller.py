from models import ReportModel
from view import ReportView

class ReportController:
    def __init__(self):
        self.model = ReportModel()
        self.view = ReportView()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '1':
                dept = self.view.get_department_input()
                records = self.model.get_department_employees(dept)
                self.view.display_department_report(dept, records)

            elif choice == '2':
                summary = self.model.get_department_summary()
                self.view.display_summary_report(summary)

            elif choice == '3':
                self.view.display_message("Exiting report generator. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again.")