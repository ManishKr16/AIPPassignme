# ============================================================================
# TASK 2: SRU_STUDENT CLASS WITH MANUAL COMMENTS
# ============================================================================

# Define the sru_student class to manage student information and operations
class sru_student:
    # Class variable to track the number of students created
    student_count = 0
    
    # Initialize the student object with personal and academic details
    def __init__(self, name, roll_no, hostel_status):
        # Store the student's full name as an instance variable
        self.name = name
        # Store the student's roll number for identification
        self.roll_no = roll_no
        # Store hostel status (True if in hostel, False otherwise)
        self.hostel_status = hostel_status
        # Initialize the total fees as 0
        self.total_fees = 0
        # Increment the student count whenever a new student is created
        sru_student.student_count += 1
    
    # Method to update the fees and add additional charges based on hostel status
    def fee_update(self, base_fee):
        # Set the base tuition fee for the student
        self.total_fees = base_fee
        # Check if student is living in hostel
        if self.hostel_status:
            # Add hostel charges of 5000 to total fees if student is in hostel
            self.total_fees += 5000
        # If student is not in hostel, add transportation charges
        else:
            # Add transportation charges of 2000 for day scholars
            self.total_fees += 2000
        # Return the updated total fees for confirmation
        return self.total_fees
    
    # Method to display all student details in a formatted manner
    def display_details(self):
        # Print a formatted header for student details
        print("\n" + "="*50)
        print("STUDENT DETAILS")
        print("="*50)
        # Display the student's name
        print(f"Name: {self.name}")
        # Display the student's roll number
        print(f"Roll No: {self.roll_no}")
        # Check hostel status and display appropriate message
        hostel_info = "Yes (In Hostel)" if self.hostel_status else "No (Day Scholar)"
        # Display the hostel status with readable format
        print(f"Hostel Status: {hostel_info}")
        # Display the total fees charged to the student
        print(f"Total Fees: Rs. {self.total_fees}")
        # Print a bottom border for formatting
        print("="*50 + "\n")
    
    # Class method to display total number of students
    @classmethod
    def display_student_count(cls):
        # Print the total count of student objects created
        print(f"Total Students Registered: {cls.student_count}")


# ============================================================================
# DEMONSTRATION AND TEST CASES
# ============================================================================

if __name__ == "__main__":
    # Create first student object with name, roll number, and hostel status
    student1 = sru_student("Raj Kumar", 101, True)
    # Update fees for student1 with base fee of 50000
    student1.fee_update(50000)
    # Display all details of student1
    student1.display_details()
    
    # Create second student object who is a day scholar
    student2 = sru_student("Priya Singh", 102, False)
    # Update fees for student2 with base fee of 50000
    student2.fee_update(50000)
    # Display all details of student2
    student2.display_details()
    
    # Create third student object
    student3 = sru_student("Anita Sharma", 103, True)
    # Update fees for student3 with base fee of 50000
    student3.fee_update(50000)
    # Display all details of student3
    student3.display_details()
    
    # Display the total count of all students created
    sru_student.display_student_count()


# ============================================================================
# AI-GENERATED COMMENTS (GitHub Copilot Style)
# ============================================================================

class sru_student_ai:
    """Student class with AI-generated inline comments"""
    # Tracks total number of student instances
    student_count = 0
    
    def __init__(self, name, roll_no, hostel_status):
        # Assign the name parameter to the instance
        self.name = name
        # Assign the roll number parameter to the instance
        self.roll_no = roll_no
        # Assign the hostel status boolean to the instance
        self.hostel_status = hostel_status
        # Initialize fees to zero
        self.total_fees = 0
        # Increment the class-level student counter
        sru_student_ai.student_count += 1
    
    def fee_update(self, base_fee):
        # Update the total fees with the base fee amount
        self.total_fees = base_fee
        # If student lives in hostel, add hostel charges
        if self.hostel_status:
            # Add 5000 rupees for hostel accommodation
            self.total_fees += 5000
        else:
            # Add 2000 rupees for daily transportation
            self.total_fees += 2000
        # Return the calculated total fees
        return self.total_fees
    
    def display_details(self):
        # Create a horizontal separator line for visual formatting
        print("\n" + "="*50)
        # Display the section title
        print("STUDENT DETAILS")
        # Print the separator again
        print("="*50)
        # Output the student's name
        print(f"Name: {self.name}")
        # Output the student's roll number
        print(f"Roll No: {self.roll_no}")
        # Determine hostel status text based on boolean value
        hostel_info = "Yes (In Hostel)" if self.hostel_status else "No (Day Scholar)"
        # Output the hostel status with descriptive text
        print(f"Hostel Status: {hostel_info}")
        # Output the total calculated fees
        print(f"Total Fees: Rs. {self.total_fees}")
        # Print the closing separator line
        print("="*50 + "\n")
    
    @classmethod
    def display_student_count(cls):
        # Print the total count of created student instances
        print(f"Total Students Registered: {cls.student_count}")


# ============================================================================
# COMPARISON ANALYSIS: MANUAL vs AI-GENERATED COMMENTS
# ============================================================================

comparison_analysis = """
MANUAL COMMENTS vs AI-GENERATED COMMENTS

1. COMMENT STYLE & TONE
   Manual:
   - Descriptive and contextual, explains WHY code does something
   - Uses conversational language
   - Provides business logic context
   
   AI:
   - Concise and technical, explains WHAT code does
   - More straightforward and action-oriented
   - Focuses on direct operations
   
2. LEVEL OF DETAIL
   Manual:
   - More verbose, provides reasoning and flow
   - Example: "Check if student is living in hostel" + reason
   - Includes explanations of outcomes
   
   AI:
   - Minimal but complete, no redundancy
   - Example: "If student lives in hostel, add hostel charges"
   - Direct action-oriented statements
   
3. CLARITY FOR BEGINNERS
   Manual:
   - Better for learning code logic and business requirements
   - Explains both HOW and WHY
   - Example: "Add hostel charges of 5000 to total fees if student is in hostel"
   
   AI:
   - Good for understanding code flow quickly
   - Explains WHAT happens at each step
   - Example: "Add 5000 rupees for hostel accommodation"
   
4. CODE MAINTENANCE
   Manual:
   - Easier to understand original intent
   - Better for future modifications
   - Helps identify business logic changes
   
   AI:
   - Easier to read for experienced developers
   - Less clutter in code
   - Still clear for debugging
   
5. SPECIFIC OBSERVATIONS
   
   a) Initialization (__init__)
      Manual: "Store the student's full name as an instance variable"
      AI: "Assign the name parameter to the instance"
      Winner: Manual (explains purpose, not just action)
   
   b) Fee Calculation
      Manual: "Add hostel charges of 5000 to total fees if student is in hostel"
              Explicitly mentions the amount and reason
      AI: "Add 5000 rupees for hostel accommodation"
          Mentions amount but less context about total fees
      Winner: Manual (more complete context)
   
   c) Hostel Status Display
      Manual: "Check hostel status and display appropriate message"
              + "Display the hostel status with readable format"
      AI: "Determine hostel status text based on boolean value"
          + "Output the hostel status with descriptive text"
      Winner: AI (more concise, equally clear)
   
   d) Class Variables
      Manual: "Class variable to track the number of students created"
      AI: "Tracks total number of student instances"
      Winner: Manual (slightly more descriptive)

6. REDUNDANCY
   Manual:
   - Some redundant comments (e.g., multiple lines explain same thing)
   - Could be consolidated for better readability
   
   AI:
   - Minimal redundancy
   - Every comment adds new information
   
7. BEST PRACTICES INSIGHTS
   
   For Production Code:
   - Use AI-generated style (less verbose, faster to read)
   - But include reasoning comments for complex logic
   
   For Educational Code:
   - Use manual style (explains context and purpose)
   - Helps learners understand not just HOW but WHY
   
   For Team Development:
   - Use a hybrid approach:
     * AI-style for straightforward operations
     * Manual-style for business logic and complex algorithms

8. OVERALL RECOMMENDATION
   
   Hybrid Approach:
   ✓ Use manual comments for business logic and algorithms
   ✓ Use AI-style comments for straightforward operations
   ✓ Combine them for maximum clarity and efficiency
   
   Manual comments are better for:
   - Teaching and learning
   - Complex business logic
   - Future maintenance and understanding intent
   
   AI-generated comments are better for:
   - Code readability for experienced developers
   - Reducing comment clutter
   - Faster code reviews

9. KEY TAKEAWAY
   AI-generated comments are technically accurate and useful, but they lack
   the contextual understanding of WHY code exists. Manual comments provide
   this crucial context, especially for educational and team environments.
   The ideal solution combines both approaches strategically.
"""

print(comparison_analysis)
