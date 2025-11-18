class Employee:
    """
    Represents an employee with the ability to update and display salary details.
    """

    def __init__(self, name, salary):
        """
        Initialize employee object.

        Args:
            name (str): Full name of the employee.
            salary (float): Current salary of the employee.
        """
        self._name = name
        self._salary = salary

    def increase_salary(self, percentage):
        """
        Increase salary by a given percentage.

        Args:
            percentage (float): Percentage increase to be applied.
        """
        if percentage > 0:
            self._salary += (self._salary * percentage / 100)

    def display_info(self):
        """Display employee details with formatted salary."""
        print(f"Employee Name: {self._name}, Salary: ₹{self._salary:,.2f}")

if __name__ == "__main__":
    employee = Employee("John Doe", 50000)
    employee.increase_salary(10)
    employee.display_info()