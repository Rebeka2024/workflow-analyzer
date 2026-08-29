# GTM AI Workflow Optimizer
# This program analyzes a business workflow and identifies
# potential opportunities for AI and automation.


# This function analyzes the workflow using information provided by the user.
def analyze_workflow(company, industry, employees, current_time,
                     repetitive, manual_data, research, summaries):

    # Display the title of the analysis.
    print("\nGTM WORKFLOW ANALYSIS")
    print("---------------------")

    # Display the company and workflow information.
    print(f"Company: {company}")
    print(f"Industry: {industry}")
    print(f"Employees: {employees}")
    print(f"Current processing time: {current_time} minutes")

    # Display recommendations based on the user's answers.
    print("\nIdentified Opportunities:")

    # Keep track of how many automation opportunities were identified.
    opportunities = 0

    # Recommend automation if the workflow is repetitive.
    if repetitive == "yes":
        print("- Automate repetitive tasks")
        opportunities += 1

    # Recommend reducing manual data entry when applicable.
    if manual_data == "yes":
        print("- Reduce manual data entry through automation")
        opportunities += 1

    # Recommend AI-assisted research when research is part of the workflow.
    if research == "yes":
        print("- Use AI-assisted research")
        opportunities += 1

    # Recommend AI-generated summaries when summaries are required.
    if summaries == "yes":
        print("- Use AI to generate standardized summaries")
        opportunities += 1

    # If no opportunities were identified, display a different message.
    if opportunities == 0:
        print("- No immediate automation opportunities identified")

    # Estimate a 50% reduction in processing time.
    # This is a project assumption, not a real-world measurement.
    estimated_time = current_time * 0.5

    # Calculate how much time could potentially be saved.
    time_saved = current_time - estimated_time

    # Assign an automation opportunity level based on the number
    # of opportunities and the amount of processing time.
    if opportunities >= 3 or current_time >= 30:
        automation_level = "HIGH"
    elif opportunities >= 1 or current_time >= 15:
        automation_level = "MEDIUM"
    else:
        automation_level = "LOW"

    # Display the estimated results.
    print(f"\nEstimated optimized processing time: {estimated_time:.1f} minutes")
    print(f"Potential time savings: {time_saved:.1f} minutes per record")

    # Display the overall automation opportunity.
    print(f"Automation Opportunity: {automation_level}")


# Ask the user for information about the company and workflow.
company = input("Enter company name: ")
industry = input("Enter industry: ")

# Convert the employee count from text into an integer.
employees = int(input("Enter employee count: "))

# Convert the processing time from text into a decimal number.
current_time = float(input("Enter current processing time (minutes): "))


# Ask questions about the workflow to identify potential improvements.
repetitive = input("Is the workflow repetitive? (yes/no): ").lower()
manual_data = input("Does the workflow involve manual data entry? (yes/no): ").lower()
research = input("Does the workflow require research? (yes/no): ").lower()
summaries = input("Does the workflow require creating summaries? (yes/no): ").lower()


# Run the workflow analysis using the information collected above.
analyze_workflow(
    company,
    industry,
    employees,
    current_time,
    repetitive,
    manual_data,
    research,
    summaries
)
# Example Output:
#
# GTM WORKFLOW ANALYSIS
# ---------------------
# Company: Acme Software
# Industry: SaaS
# Employees: 500
# Current processing time: 30.0 minutes
#
# Identified Opportunities:
# - Automate repetitive tasks
# - Reduce manual data entry through automation
# - Use AI-assisted research
# - Use AI to generate standardized summaries
#
# Estimated optimized processing time: 15.0 minutes
# Potential time savings: 15.0 minutes per record
# Automation Opportunity: HIGH
