# Instructions
# 1. Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
# 2. Create a Company type that employees can work for. A company should have a business name, address, and industry type.
# 3. Create two companies, and 5 people who want to work for them.
# 4. Assign 2 people to be employees of the first company.
# 5. Assign 3 people to be employees of the first company.
# 6. Output a report to the terminal the displays a business name, and its employees.
# For example:

# Acme Explosives is in the chemical industry and has the following employees
#    * Michael Chang
#    * Martina Navritilova

# Jetways is in the transportation industry and has the following employees
#    * Serena Williams
#    * Roger Federer
#    * Pete Sampras

class Employee:
    def __init__(self, name, job_title, start_date):
        self.name = name
        self.job_title = job_title
        self.start_date = start_date

class Company:
    def __init__(self, name, address, industry_type):
        self.name = name
        self.address = address
        self. industry_type = industry_type
        self.employees = list()

    def print_company_info(self):
        print(f'{self.name} is in the {self.industry_type} and has the following employees:')
        for employee in self.employees:
            print(f'*{employee.name}')

michael_chang = Employee("Michael Chang", "Manager", "5/14/20")
samual_jackson = Employee("Samuel Jackson", "HR", "4/20/20")
ronni_mcdonald = Employee("Ronni McDonald", "Stocker", "3/11/20")
rover_johnson = Employee("Rover Johnson", "Researcher", "6/14/20")
george_yo = Employee("George Yo", "Researcher", "5/14/20")

acme_explosives = Company("Acme Explosives", "456 Blow It Up Rd", "chemical industry")
jetways = Company("Jetways", "123 Flex Away St", "transportation inducstry")

acme_explosives.employees.append(michael_chang)
acme_explosives.employees.append(samual_jackson)
jetways.employees.append(ronni_mcdonald)
jetways.employees.append(rover_johnson)
jetways.employees.append(george_yo)

acme_explosives.print_company_info()
jetways.print_company_info()

