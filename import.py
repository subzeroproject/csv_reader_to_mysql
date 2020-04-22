import csv
import MySQLdb
import datetime

database = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='testcsv')
cursor = database.cursor()

sql = '''DROP TABLE IF EXISTS `csv` ; CREATE TABLE csv (customerid int, firstname varchar(255), lastname varchar(255), companyname varchar(255), billingaddress1 varchar(255), billingaddress2 varchar(255), city varchar(255), state varchar(255), postcode varchar(255), country varchar(255), phonenumber int, emailaddress varchar (255), createddate DATETIME)'''
cursor.execute(sql)

now = datetime.datetime(2020,4,22)
str_now = now.date().isoformat()

with open('customer.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        #print(row['customerid'], row['firstname'], row['lastname'],row['companyname'])
        sql2 = "INSERT INTO csv(customerid ,firstname, lastname, companyname, billingaddress1, billingaddress2, city, state, postcode, country, phonenumber, emailaddress, createddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql2,[(row['customerid'], row['firstname'], row['lastname'], row['companyname'], row['billingaddress1'], row['billingaddress2'], row['city'], row['state'], row['postalcode'], row['country'], row['phonenumber'], row['emailaddress'], row['createddate'])])
        database.commit()
