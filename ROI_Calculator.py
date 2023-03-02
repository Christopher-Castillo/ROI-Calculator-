class RoiCalc():
    def __init__(self, income=0, expenses=0, cashflow=0, roi=0):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.roi = roi

    def get_income(self):
        self.income = int(input('What is the monthly rental income for this property?: '))

    def get_expenses(self):
        tax = int(input('Enter the monthly tax amount: '))
        insurance = int(input('Enter the monthly insurance amount: '))
        utilities = int(input('Enter the monthly utilities amount: '))
        repairs = int(input('How much are you saving for repairs monthly?: '))
        capex = int(input('How much are you saving for CapEx monthly?: '))
        prop_man = int(input('How much is paid to the property manager monthly?:  '))
        mortgage = int(input('What is your monthly mortgage cost?:  '))
        self.expenses = tax + insurance + utilities + repairs + capex + prop_man + mortgage

    def calculate_cash_flow(self):
        self.cashflow = self.income - self.expenses
        print("Cash flow: %s" % (self.cashflow))

    def calculate_roi(self):
        self.cashflow = self.cashflow * 12
        overall_investment = int(input("What was the total investment you made on this property?:  "))
        self.roi = (self.cashflow / overall_investment) * 100
        print(f"Your cash on cash ROI is: {self.roi}%")
        return self.roi
    
roi_calc = RoiCalc()

# Get user input for rental property
roi_calc.get_income()
roi_calc.get_expenses()

# Calculate cash flow and ROI
roi_calc.calculate_cash_flow()
roi_calc.calculate_roi()
