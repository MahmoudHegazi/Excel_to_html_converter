df = pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
وحفظ البيانات الى ملف html أو sql أو اي قاعدة بيانات

print(df.to_html()) 
import sqlite3

# connect to the database
# the database file will be worldbank.db
# note that sqlite3 will create this database file if it does not exist already
conn = sqlite3.connect('worldbank.db')

# TODO: output the df_merged dataframe to a SQL table called 'tablename'.
# HINT: Use the to_sql() method
# HINT: Use the conn variable for the connection parameter
# HINT: You can use the if_exists parameter like if_exists='replace' to replace a table if it already exists

df.to_sql('tablename', con = conn, if_exists='replace', index=False)


# connect to the data base
conn = sqlite3.connect('worldbank.db')

# get a cursor
cur = conn.cursor()

# drop tables created previously to start fresh
cur.execute("DROP TABLE IF EXISTS test")
cur.execute("DROP TABLE IF EXISTS indicator")
cur.execute("DROP TABLE IF EXISTS projects")
cur.execute("DROP TABLE IF EXISTS gdp")
cur.execute("DROP TABLE IF EXISTS population")

# TODO create the projects table including project_id as a primary key
# HINT: Use cur.execute("SQL Query")
cur.execute("CREATE TABLE projects (project_id TEXT PRIMARY KEY, countryname TEXT, countrycode TEXT, totalamt REAL, year INTEGER);")

# TODO: create the gdp table including (countrycode, year) as primary key
# HINT: To create a primary key on multiple columns, you can do this:
# CREATE TABLE tablename (columna datatype, columnb datatype, columnc dataype, PRIMARY KEY (columna, columnb));
cur.execute("CREATE TABLE gdp (countryname TEXT, countrycode TEXT, year INTEGER, gdp REAL, PRIMARY KEY (countrycode, year));")

# TODO: create the gdp table including (countrycode, year) as primary key
cur.execute("CREATE TABLE population (countryname TEXT, countrycode TEXT, year INTEGER, population REAL, PRIMARY KEY (countrycode, year));")

# commit changes to the database. Do this whenever modifying a database
conn.commit()


# TODO:insert project values into the projects table
# HINT: Use a for loop with the pandas iterrows() method
# HINT: The iterrows() method returns two values: an index for each row and a tuple of values
# HINT: Some of the values for totalamt and year are NaN. Because you've defined
# year and totalamt as numbers, you cannot insert NaN as a value into those columns.
# When totaamt or year equal NaN, you'll need to change the value to something numeric
# like, for example, zero

for index, values in df_projects.iterrows():
    project_id, countryname, countrycode, totalamt, year = values
    
    if totalamt == 'nan':
        totalamt = 0
    if year == 'nan':
        year = 0
    
    sql_string = 'INSERT INTO projects (project_id, countryname, countrycode, totalamt, year) VALUES ("{}", "{}", "{}", {}, {});'.format(project_id, countryname, countrycode, totalamt, year)
    cur.execute(sql_string)

conn.commit()

# TODO: insert gdp values into the gdp table
for index, values in df_indicator[['countryname', 'countrycode', 'year', 'gdp']].iterrows():
    countryname, countrycode, year, gdp = values
        
    sql_string = 'INSERT INTO gdp (countryname, countrycode, year, gdp) VALUES ("{}", "{}", {}, {});'.format(countryname, countrycode, year, gdp)
    cur.execute(sql_string)

conn.commit()


# TODO: insert population values into the population table
for index, values in df_indicator[['countryname', 'countrycode', 'year', 'population']].iterrows():
    countryname, countrycode, year, population = values
        
    sql_string = 'INSERT INTO population (countryname, countrycode, year, population) VALUES ("{}", "{}", {}, {});'.format(countryname, countrycode, year, population)
    cur.execute(sql_string)

conn.commit()

# run this command to see if your tables were loaded as expected
sqlquery = "SELECT * FROM projects JOIN gdp JOIN population ON projects.year = gdp.year AND projects.countrycode = gdp.countrycode AND projects.countrycode = population.countrycode AND projects.year=population.year;"
result = pd.read_sql(sqlquery, con=conn)
result.shape

conn.commit()
conn.close()
