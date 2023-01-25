from flask import Flask,send_file,render_template,request
from Bank_ai import Predict_Score
import os 

# PEOPLE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER


@app.route('/')
def homePage():
    return render_template("index.html")

@app.route('/data',methods = ['GET', 'POST'])
def data_getter():
    return render_template("index2.html")


@app.route('/data/prediction',methods = ['GET', 'POST'])
def hello_ai():
    if request.method == 'GET':
        return "Error Not Found 404"
    if request.method == 'POST':
        data = dict(request.form)         
        row_data = [ 25 , 
        int(data['annual_income']) , 
        int(data['monthly_inhand_salary']) , 
        int(data['num_bank_accounts'] ), 
        int(data['num_credit_card']) , 
        int(data['interest_rate']) , 
        int(data['Num_of_Loan']), 
        int(data['Delay_from_due_date']) , 
        int(data['num_of_delayed_payment']) , 
        int(data['changed_credit_limit']) , 
        int(data['num_credit_inquiries']) , 
        int(data['credit_mix']) , 
        int(data['Loan_To_Debt']), 
        int(data['credit_utilization_ratio']) , 
        int(data['credit_history_age'] ), 
        int(data['Total_EMI_per_month']) , 
        int(data['Amount_invested_monthly']) , 
        int(data['Monthly_Balance'] ), 
        data['TypeofLoan'], 
        data['Month'] , 
        data['JobTitle'] , 
        data['MinAmount'] , 
        data['Behavior']  
        ]
        results = Predict_Score(row_data)
        if results == 0 :
            return render_template("prediction_0.html")
        elif results == 1 :
            return render_template("prediction_1.html")
        else :
            return render_template("prediction_2.html")

if __name__ == "__main__":
    app.run(debug=True , port=9000)
