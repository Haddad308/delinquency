## Package used in deployment 
import joblib
import warnings 
warnings.filterwarnings("ignore")

## loading models 
model = joblib.load("model.h5")
scalar = joblib.load("scalar.h5")

## Functions to pre-process the data 
def loanType(loan):  
    if loan == "Credit Builder" :
        return  [1,0,0,0,0,0,0,0]
    elif loan == "Personal Loan" :
        return  [0,1,0,0,0,0,0,0]
    elif loan == "Debt Consolidation" :
        return  [0,0,1,0,0,0,0,0]
    elif loan == "Student" :
        return  [0,0,0,1,0,0,0,0]
    elif loan == "Payday" :
        return  [0,0,0,0,1,0,0,0]
    elif loan == "Mortgage" :
        return  [0,0,0,0,0,1,0,0]
    elif loan == "Auto" :
        return  [0,0,0,0,0,0,1,0]
    elif loan == "Home Equity" :
        return  [0,0,0,0,0,0,0,1]
    else :
        return  [0,0,0,0,0,0,0,1]
def month(month):
    if month == "August" :
        return  [1,0,0,0,0,0,0]
    elif month == "February" :
        return  [0,1,0,0,0,0,0]
    elif month == "January" :
        return  [0,0,1,0,0,0,0]
    elif month == "July" :
        return  [0,0,0,1,0,0,0]
    elif month == "June" :
        return  [0,0,0,0,1,0,0]
    elif month == "March" :
        return  [0,0,0,0,0,1,0]
    elif month == "May" :
        return  [0,0,0,0,0,0,1]
    elif month == "April" :
        return  [0,0,0,0,0,0,0]
    else :
        return  [0,0,0,0,0,0,0]
def jobTitle(title): 
    if title == "Architect" :
        return  [1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif title == "Developer" :
        return  [0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif title == "Doctor" :
        return  [0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    elif title == "Engineer" :
        return  [0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif title == "Entrepreneur" :
        return  [0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif title == "Journalist" :
        return  [0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif title == "Lawyer" :
        return  [0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif title == "Manager" :
        return  [0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    elif title == "Mechanic" :
        return  [0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    elif title == "Media_Manager" :
        return  [0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    elif title == "Musician" :
        return  [0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    elif title == "Scientist" :
        return  [0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    elif title == "Teacher" :
        return  [0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    elif title == "Writer" :
        return  [0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    elif title == "Accountant" :
        return  [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    else :
        return  [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def Payment(pay):
    if pay == "Yes" :
        return  [1]
    else :
        return  [0]
def Behavior(behave): 
    if behave == "High spent Medium value payments" :
        return  [1,0,0,0,0]
    elif behave == "High spent Small value payments" :
        return  [0,1,0,0,0]
    elif behave == "Low spent Large value payments" :
        return  [0,0,1,0,0]
    elif behave == "Low spent Medium value payments" :
        return  [0,0,0,1,0]
    elif behave == "Low spent Small value payments" :
        return  [0,0,0,0,1]
    elif behave == "High spent Large value payments" :
        return  [0,0,0,0,0]
    else :
        return  [0,0,0,0,0]
def Convert(data):
    final_data = []
    ## The all numerical data 
    final_data.extend(data[:18])
    ## 19 Type of loan 
    final_data.extend(loanType(data[18]))
    ## 20 Month 
    final_data.extend(month(data[19]))
    ## 21 Job title 
    final_data.extend(jobTitle(data[20]))
    # ## 22 Payment_of_Min_Amount
    final_data.extend(Payment(data[21]))
    # ## 23 Payment Behavior
    final_data.extend(Behavior(data[22]))
    
    return final_data
def Predict_Score(data):

    ## covert Data 
    data = Convert(data)
    return model.predict(scalar.transform([data]))[0] 
