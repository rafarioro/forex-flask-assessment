from flask import Flask, request, render_template, redirect, flash, session
from currency_converter import CurrencyConverter

app = Flask(__name__)
app.secret_key = "key"

@app.route("/", methods=['GET', 'POST'])
def converterApp():
    """Start of the program"""
    
    
 
    return render_template("index.html") 
    




@app.route('/converted', methods=["POST"])
def convertedValue():
    """Shows value converted"""
    c = CurrencyConverter()
    valueFrom = request.form["value1"]
    valueTo = request.form["value2"]
    amountToConvert = request.form["amount"]

    currencies = ["USD", "GBP", "EUR", "JPY", "AUD", "CAD"]
       
    if len(amountToConvert) == 0:
        flash("Error - Please an amount to convert")
        return redirect("/")  
    
    elif len(valueTo) == 0 or len(valueFrom) == 0:
        flash("Error - Enter correct values for all fields")
        return redirect("/")  

    elif valueFrom in currencies and valueTo in currencies:
        flash("Here is your value")
        newValue = round(c.convert(amountToConvert, valueFrom, valueTo), 2)
        return render_template('converted.html', convertedValue = newValue)

    else:
        flash("Error - Check your inputs")
        return redirect("/")

    



    