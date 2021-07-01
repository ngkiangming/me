import pandas
xx.head() - give the top 5 rows
xx.value_counts - calculate the data
xx.columns - print columns
xx.iloc[] - give the information of the row
xx.column or xx["column"] - give the whole column
xx.[column].plot() - plot the data
xx["column"]xx["column"] < 3000].hist() -plot the data less than 3000
some_numbers[(some_numbers < 4) | (some_numbers > 97)] - this needs the round brackets
id_flows["Sector Name"].value_counts().plot(kind="bar") - combine 3 and 7 in bar
