class Roi():

    def __init__(self, price, income, costs):
        self.price = price
        self.income = income
        self.costs = costs
    
        yearlyincome = income * 12
        yearlycosts = costs * 12
        yearlyincomeafter = yearlyincome - yearlycosts
        roi = yearlyincomeafter / price
        roiper = roi * 100
        print(f'ROI percentage is {roiper}% per year')
        return None


price = float(input("What is the investment cost(Downpayment +Closing costs +Rehab budget +Misc other): "))
income = float(input("What is the monthly income(Rental Income + Laundry Income + Storage Income + Misc Income): "))
costs = float(input("What is the costs per month(Taxes + Insurance + Water/Sewer + Garbage + Electric/Gas + HOA Fee + Lawn/Snow + Vacancy + Repairs + CapEx + Prop. Mgmt + Mortgage): "))

croi = Roi(price, income, costs)
