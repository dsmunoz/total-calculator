# total-calculator

This project calculates some comisions and discounts based on some bussiness rules

##Requirements
 
- python3.9 
- pip https://pip.pypa.io/en/stable/
- venv https://docs.python.org/3/library/venv.html
##Running local server

1. Install virtualenv (if you don't have it installed already)
```bash
$ pip install virtualenv
```
2. Initialize virtual environment 
```bash
$ source venv\bin\activate
```
3. Install requirements
```bash
$ pip install -r requirements.txt
```
4. Run local server
```bash
$ flask run 
```

Now you should be able to make request to http://127.0.0.1:5000

##Running tests

Within venv and root folder:
```bash
$ pytest
```

##Usage

There is only one route defined: 
1. `calculate-total`. 

This is a `GET` route and the next URI parameters are required to make a call:

1. `state` can be any and only one of [YN, CA, AZ, TX, OH]
2. `type` can be any and only one of [normal, premium]
3. `km` a numeric value
4. `base_amount` a numeric value

call route example: 
```bash
http://127.0.0.1:5000/calculate-total?state=OH&type=premium&km=30.1&base_amount=20.4
```

###Structure

This projects is based in three main parts:
1. Validations: There is a file within services called `validator.py` which is in charge of making sure that
the request is valid.
2. Bussiness rules: there is a json file called comission_percentages.json in the root folder 
that takes into account the following points in order to simplify the calculation.
   - There is discounts applied to the base_amount sent.
   - There is a commission applied depending on `type` and `state`.
   - There is a tax applied called `iva`.
   - There is a discount applied to the total_amount.
3. Process: once we have a validated request and the bussines rules set, we need a file to process the comission_percentages.json
and apply the formula to calculate the total.

   