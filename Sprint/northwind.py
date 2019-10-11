import sqlite3

# Connect to database
conn = sqlite3.connect('northwind_small.sqlite3')


# Cursor to read the database
cursor = conn.cursor()


# What are the ten most expensive items (per unit price) in the database?
ten_most_expensive_query = '''
    SELECT ProductName, UnitPrice FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;'''
ten_most_expensive = cursor.execute(ten_most_expensive_query).fetchall()
print(' The ten most expensive items and their prices :')
print('------------------------------------------------')
for info in ten_most_expensive:
    item = (info[0] + ':').ljust(24)
    price = info[1]
    print(f'{item} {price}')


# What is the average age of an employee at the time of their hiring?
average_age_query = '''
SELECT ROUND(AVG(HireDate - BirthDate), 2) AS average_age_on_hire
FROM Employee;
 '''
average_age = cursor.execute(average_age_query).fetchone()[0]
print(
    f' The average age of an employee at the time of hiring is {average_age}')


# (Stretch) How does the average age of employee at hire vary by city?
average_age_by_city_query = '''
SELECT ROUND(AVG(HireDate - BirthDate), 2) AS average_age_on_hire
FROM Employee
GROUP BY City
ORDER BY average_age_on_hire;
'''
average_age_by_city = cursor.execute(average_age_by_city_query).fetchall()
print(f' The average age of employees hire by city is {average_age_by_city}')


# What are the ten most expensive items (per unit price) in the database
# and their suppliers?
expensive_item_supplier_query = '''
SELECT ProductName, CompanyName FROM Product
INNER JOIN Supplier ON Product.SupplierID = Supplier.ID
ORDER BY UnitPrice DESC
LIMIT 10;
'''
expensive_item_supplier = cursor.execute(expensive_item_supplier_query).fetchall()
print(' The ten most expensive items with their supplier are:')
print('--------------------------------------------------')
for info in expensive_item_supplier:
    item = (info[0] + ':').ljust(24)
    supplier = info[1]
    print(f'{item} {supplier}')


# What is the largest category (by number of unique products in it)?
largest_category_query = '''
SELECT CategoryName, COUNT(DISTINCT Product.ID) AS NumberProducts
FROM Category
INNER JOIN Product ON Category.ID = Product.CategoryID
GROUP BY CategoryName
ORDER BY NumberProducts DESC
LIMIT 1;
'''
largest_category = cursor.execute(largest_category_query).fetchone()
print(f' {largest_category[0]} is the largest category with {largest_category[1]} unique products ')


# (Stretch) Who's the employee with the most territories?
employee_territories_query = '''
SELECT LastName, FirstName, COUNT(Territory.ID) as NumberTerritories
FROM Employee JOIN EmployeeTerritory AS et
ON Employee.ID = et.EmployeeID
JOIN Territory
ON et.TerritoryID = TerritoryID
GROUP BY Employee.ID
ORDER BY NumberTerritories DESC
LIMIT 1;
'''
employee_territories = cursor.execute(employee_territories_query).fetchone()
print(f'The employee who has the most territories : {employee_territories[2]} is {employee_territories[1]} {employee_territories[0]}')
