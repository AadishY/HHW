# 📊 *Part A: Data Handling - Pandas Solutions*
---

## *Question 1*
### Create a pandas Series from a dictionary and apply all the attributes.
python
import pandas as pd
import numpy as np

data_dict = {'Delhi': 3000, 'Mumbai': 4000, 'Chennai': 5000, 'Surat': 4500}
series_from_dict = pd.Series(data_dict, name="City_Cases")
print(series_from_dict)

print(f"Index: {series_from_dict.index}")
print(f"Values: {series_from_dict.values}")
print(f"Data Type: {series_from_dict.dtype}")
print(f"Size: {series_from_dict.size}")
print(f"Is it empty? {series_from_dict.empty}")
print(f"Name of the Series: {series_from_dict.name}")

*Output:*

Delhi      3000
Mumbai     4000
Chennai    5000
Surat      4500
Name: City_Cases, dtype: int64
Index: Index(['Delhi', 'Mumbai', 'Chennai', 'Surat'], dtype='object')
Values: [3000 4000 5000 4500]
Data Type: int64
Size: 4
Is it empty? False
Name of the Series: City_Cases


---

## *Question 2*
### Find largest, smallest and filtered values from a Series of state areas.
python
import pandas as pd

areas = pd.Series({
    'Rajasthan': 342239,
    'Madhya Pradesh': 308252,
    'Maharashtra': 307713,
    'Uttar Pradesh': 240928,
    'Gujarat': 196024,
    'Karnataka': 191791,
    'Goa': 3702
}, name="State_Areas_km2")

print("--- Original Series ---")
print(areas)

print("\n--- Three Largest Areas ---")
print(areas.sort_values(ascending=False).head(3))

print("\n--- Three Smallest Areas ---")
print(areas.sort_values().head(3))

print("\n--- Areas > 50000 km² ---")
print(areas[areas > 50000])


---

## *Question 3*
### Create a Series with custom indices and calculate cubes of values.
python
import pandas as pd

indexes = ['p', 'q', 'r', 'n', 't', 'v']
data_list = [42, 15, 78, 55, 23, 89]
my_series = pd.Series(data_list, index=indexes, name="My_Values")

print("--- Original Series ---")
print(my_series)

print("\n--- Cubes of Series Values ---")
cubed_series = my_series ** 3
print(cubed_series)


---

## *Question 4*
### Create and modify a DataFrame for CORONA dataset.
python
import pandas as pd

data = {'State': ['Delhi', 'Mumbai', 'Chennai', 'Surat'],
        'Cases': [3000, 4000, 5000, 4500]}
corona_df = pd.DataFrame(data, index=[100, 110, 120, 130])
corona_df.index.name = 'ID'
print("--- Initial DataFrame ---")
print(corona_df)

corona_df['Recovery'] = [2500, 3200, 4100, 3800]
print("\n--- (a) After adding 'Recovery' ---")
print(corona_df)

corona_df['Deaths'] = [150, 200, 250, 180]
print("\n--- (b) After adding 'Deaths' ---")
print(corona_df)

corona_df.loc[140] = ['Pune', 6000, 5000, 300]
print("\n--- (c) After adding row for 'Pune' ---")
print(corona_df)

corona_df.insert(3, 'Percentage', (corona_df['Recovery'] / corona_df['Cases']) * 100)
print("\n--- (d) After inserting 'Percentage' ---")
print(corona_df)

del corona_df['Percentage']
print("\n--- (e) After deleting 'Percentage' ---")
print(corona_df)

corona_df.pop('Deaths')
print("\n--- (f) After popping 'Deaths' ---")
print(corona_df)

corona_df.loc[105] = ['Kolkata', 3500, 3000]
corona_df = corona_df.sort_index()
print("\n--- (g) After adding 'Kolkata' and sorting ---")
print(corona_df)

print("\n--- (h) Temporarily dropped columns ---")
print(corona_df.drop(columns=['Cases', 'State']))

print("\n--- Original DataFrame remains unchanged ---")
print(corona_df)


---

## *Question 5*
### Create a student DataFrame and show top and bottom records.
python
import pandas as pd

names = pd.Series(['Rohan', 'Priya', 'Amit', 'Sneha', 'Vivek'])
grades = pd.Series(['A', 'B', 'A', 'C', 'B'])
marks = pd.Series([92, 78, 95, 68, 81])

student_df = pd.DataFrame({
    'Name': names,
    'Grade': grades,
    'Marks': marks
})

print("--- Full Student DataFrame ---")
print(student_df)

print("\n--- (a) First Three Records ---")
print(student_df.head(3))

print("\n--- (b) Last Two Records ---")
print(student_df.tail(2))


---

## *Question 6*
### Create salary DataFrames and apply bonuses.
python
import pandas as pd

salary_data1 = {'Name': ['Raj', 'Sita', 'Tom', 'Anjali', 'Dev'],
                'Salary': [50000, 62000, 55000, 70000, 48000]}
df1 = pd.DataFrame(salary_data1)

salary_data2 = {'Name': ['John', 'Mia', 'Lee', 'Sara', 'Omar'],
                'Salary': [90000, 85000, 92000, 88000, 79000]}
df2 = pd.DataFrame(salary_data2)

print("--- (a) Original DataFrames ---")
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Add Bonus
df1['Salary'] += 5000
df2['Salary'] += 5000

print("\n--- (b) DataFrames After Adding Bonus ---")
print("DataFrame 1 with Bonus:")
print(df1)
print("\nDataFrame 2 with Bonus:")
print(df2)


---

## *Question 7*
### Create a DataFrame from lists and add a new column.
python
import pandas as pd

list1 = [10, 11, 12, 13, 14]
list2 = [23, 34, 45, 32, 65]
list3 = [55, 60, 65, 70, 75]

df_lists = pd.DataFrame({
    'Col1': list1,
    'Col2': list2,
    'Col3': list3
})
print("--- (a) Original DataFrame ---")
print(df_lists)

new_list = [1, 2, 3, 4, 5]
df_lists['Col4'] = new_list

print("\n--- (b) After Adding New Column ---")
print(df_lists)


---

## *Question 8*
### Handle missing values in a DataFrame.
python
import pandas as pd
import numpy as np

nan_data = [[23, 25, np.nan, np.nan],
            [34, np.nan, np.nan, np.nan],
            [43, 44, 45, 46]]
nan_df = pd.DataFrame(nan_data)
print("--- (a) DataFrame with NaN values ---")
print(nan_df)

print("\n--- (b) Replacing NaN with 0 ---")
print(nan_df.fillna(0))

replace_map = {0: -1, 1: -2, 2: -3, 3: -4}
print("\n--- (c) Replacing NaN with different values per column ---")
print(nan_df.fillna(value=replace_map))

print("\n--- (d) Forward-filling NaN values ---")
print(nan_df.fillna(method='ffill'))


---


aadish mere pass time ni hai isko plz apne GitHub pe save kar lo 🙏
