"""this code has a history of apple stock prices from march 17th 2021 to march 17th 2022. It will ask the user what date they want to see then give them four options of what kind of data they want to see about that date.
It will ask if they want to see the high, low, open, or close of apple stock on that paticular date.
"""



import csv
from pprint import pprint
apple=open('AAPL.csv')
dict_reader=csv.DictReader(apple)
pprint(dict_reader)
#creating empty dict
stockdate={}

#for loop to ask what data they want to see
for i in dict_reader:
    stockdate[i['Date']]={
        'High':i['High'],
        'Low': i['Low'],
        'Close': i['Close'],
        'Open':i['Open'],
    }
while True:


#input to ask what date they want to know about
    chosen_date=input('what date do you want to see the information for? or type done if you are done asking questions. Answer like so: 2022-01-01 That date would correlate to Jan first 2022')
    if chosen_date in stockdate:
#input to ask what specfically they want to know about that date
        chosen_data=input('what do you want to see? Open, Close, High, or Low? ')
        print(stockdate[chosen_date][chosen_data])
    elif chosen_date=='done':
        break



#finally, an else statement to give something back to the reader if they enter an invalid date.
    else:
        print ('we do not have data for that date.')

