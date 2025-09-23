# Python Fundamentals Workshop for Architecture & Building Science Students
# Jupyter Notebook Template (Extended Version)

# --- INTRODUCTION ---
# This notebook will guide you through Python basics, working with data structures,
# using Pandas for data analysis, and making visualizations.

# --- USEFUL RESOURCES ---
# - Official Python Tutorial: https://docs.python.org/3/tutorial/
# - W3Schools Python Tutorial: https://www.w3schools.com/python/
# - Pandas Documentation: https://pandas.pydata.org/docs/
# - Matplotlib Documentation: https://matplotlib.org/stable/contents.html
# - Jupyter Notebook Documentation: https://jupyter-notebook.readthedocs.io/en/stable/
# - Stack Overflow (for coding questions): https://stackoverflow.com/
# - Python for Data Analysis (book by Wes McKinney): https://www.oreilly.com/library/view/python-for-data/9781491957653/
# - Automate the Boring Stuff with Python (book by Al Sweigart): https://automatetheboringstuff.com/

# --- USEFUL KEYBOARD SHORTCUTS ---
# - Run cell: Shift + Enter
# - Insert cell above: A
# - Insert cell below: B
# - Delete cell: D, D (press D twice)
# - Undo cell deletion: Z
# - Save notebook: Ctrl + S (Cmd + S on Mac)
# - Toggle cell type (code/markdown): Y (code), M (markdown)
# - Comment/uncomment line: Ctrl + / (Cmd + / on Mac)


# --- PART 1: PYTHON BASICS ---

# Variables and Types
length = 5  # meters (int)
width = 3  # meters (int)
height = 2.8  # meters (float)
building_type = "Residential"  # string
zip_code = "94103"  # string, even if it looks like a number
air_conditioned = True  # boolean

print("Length:", length)
print("Width:", width)
print("Height:", height)
print("Building type:", building_type)
print("ZIP code:", zip_code)
print("Air conditioned:", air_conditioned)

print("Type of height:", type(height))
print("Type of building type:", type(building_type))
print("Type of ZIP code:", type(zip_code))
print("Type of air conditioned:", type(air_conditioned))

# Only numerical types (int, float) can be used in math operations.
area = length * width
volume = length * width * height
print("Room area:", area, "m²")
print("Room volume:", volume, "m³")

# Strings cannot be directly multiplied or added with numbers:
# Example: zip_code * 2 will repeat the string instead of calculating.
print(zip_code * 2)

# Type conversion
zip_as_number = int(zip_code)  # Convert string to integer
print(zip_as_number * 2)  # Now this will do a numerical operation

# Other type conversions are
height_str = str(height)  # float to string
length_float = float(length)  # int to float
print("Height as string:", height_str)
print("Length as float:", length_float)


# --- Lists and Slicing ---
room_sqm = [12, 18, 25, 9, 15]  # areas of rooms in m²
print("Room areas:", room_sqm)

# Indexing and slicing
print("First room:", room_sqm[0])
print("Last two rooms:", room_sqm[-2:])
print("Every second room:", room_sqm[::2])

# List methods
room_sqm.append(20)  # add new room
print("After append:", room_sqm)

room_sqm.remove(9)  # remove a room
print("After remove:", room_sqm)

room_sqm.sort(ascending=True)  # sort values
print("Sorted:", room_sqm)

# --- Dictionaries ---
building_data = {
    "Building type": "Office",
    "Sqm": 1000,
    "Height": 18.2,
    "Air conditioned": True,
}
print("Dictionary:", building_data)

# Accessing values
print("Building size:", building_data["Sqm"])

# Adding new key-value pair
building_data["Cooling Set Point"] = 25
print("Updated dict:", building_data)


# --- Loops and Logical statements ---

# Loop through list
for area in room_sqm:
    print(area, "m²")

# Loop through keys and values
for key, value in building_data.items():
    print(key, "->", value)

# if-elif-else statements
if building_data["Sqm"] > 500:
    print("Large building")
elif building_data["Sqm"] > 100:
    print("Medium building")
else:
    print("Small building")

# Combining loops and conditions
for area in room_sqm:
    if area < 10:
        print(area, "m² -> Too small!")
    elif area < 20:
        print(area, "m² -> Medium")
    else:
        print(area, "m² -> Large")


# Functions and Modules
def energy_use_intensity(energy_use, floor_area):
    """Calculate Energy Use Intensity (EUI) in kWh/m²
    energy_use: in kWh
    floor_area: in m²
    """
    eui = energy_use / floor_area
    return eui


eui_value = energy_use_intensity(12000, 200)  # 12000 kWh, 200 m²
print("EUI:", eui_value)


# Import custom functions
from functions import calculate_eui

eui_value2 = calculate_eui(15000, 300)  # 15000 kWh, 300 m²
print("EUI from imported function:", eui_value2)


# Importing a module
import math

circle_area = math.pi * (5**2)  # Area of circle with radius
print("Circle area with radius 5:", circle_area)


# Installing existing libraries (collection of modules)
# `pip install pythermalcomfort`

from pythermalcomfort.models import pmv_ppd

result = pmv_ppd(
    ta=25, tr=25, vel=0.1, rh=50, met=1.2, clo=0.5
)  # Predict thermal comfort
print("PMV and PPD:", result)


# --- PART 2: PANDAS BASICS / WORKING WITH DATAFRAMES ---
import pandas as pd

# Create a dataset of monthly energy usage (kWh)
data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
    "Energy_kWh": [320, 280, 300, 250, 200, 180, 170, 190, 220, 260, 300, 330],
    "Temperature_C": [2, 4, 8, 12, 18, 22, 25, 24, 20, 14, 8, 4],
}

df = pd.DataFrame(data)
print(df.head())

# Summary statistics
print(df.describe())

# Column selection
print(df["Energy_kWh"].head())

# Row selection (slicing)
print(df.iloc[0:3])  # first three rows

# Slicing backwards
print(df.iloc[-3:])  # last three rows

# Conditional filtering
summer = df[df["Temperature_C"] > 20]
print("Summer months:")
print(summer)

# Filtering with multiple conditions
moderate = df[(df["Temperature_C"] > 10) & (df["Energy_kWh"] < 250)]
print("Moderate weather, low energy use:")
print(moderate)

# Add new column
df["Energy_per_degree"] = df["Energy_kWh"] / df["Temperature_C"]
print(df.head())

# --- Preprocessing ---

# Drop a column
df_no_temp = df.drop(columns=["Temperature_C"])
print(df_no_temp.head())

# Drop rows with NaN values
example_df = pd.DataFrame({"A": [1, 2, None, 4], "B": ["x", None, "y", "z"]})
print("Original:")
print(example_df)

clean_df = example_df.dropna()
print("After dropna:")
print(clean_df)

# Fill missing values
filled_df = example_df.fillna({"A": 0, "B": "missing"})
print("After fillna:")
print(filled_df)

# Merge DataFrames
materials = pd.DataFrame(
    {"Material": ["Brick", "Concrete", "Glass"], "ThermalConductivity": [0.6, 1.7, 0.8]}
)

prices = pd.DataFrame(
    {"Material": ["Brick", "Concrete", "Glass"], "Price_per_unit": [50, 80, 120]}
)

merged = pd.merge(materials, prices, on="Material")
print("Merged DataFrame:")
print(merged)

# Loop with DataFrames
for idx, row in df.iterrows():
    if row["Energy_kWh"] > 300:
        print(row["Month"], "-> High energy use")


# Using functions with DataFrames
def classify_energy_use(energy):
    if energy > 300:
        return "High"
    elif energy > 200:
        return "Medium"
    else:
        return "Low"


df["Energy_Class"] = df["Energy_kWh"].apply(classify_energy_use)
print(df)


# --- PART 3: DATA VISUALIZATION ---
import matplotlib.pyplot as plt

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Energy_kWh"], marker="o")
plt.title("Monthly Energy Consumption")
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")
plt.show()

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Month"], df["Energy_kWh"], color="skyblue")
plt.title("Energy Consumption by Month")
plt.xlabel("Month")
plt.ylabel("Energy (kWh)")
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Energy_kWh"], bins=5, edgecolor="black")
plt.title("Distribution of Energy Consumption")
plt.xlabel("Energy (kWh)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df["Temperature_C"], df["Energy_kWh"])
plt.title("Energy Use vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Energy (kWh)")
plt.show()

# --- PART 4: EXERCISE IDEAS ---

# Exercise 1: Compute total floor area of all rooms in the list 'rooms'.

# Exercise 2: Write a loop to check which rooms in 'room_data' are larger than 15 m².

# Exercise 3: In the DataFrame df, calculate the average monthly energy use.

# Exercise 4: Filter months where energy use is below 200 kWh.

# Exercise 5: Create a histogram of energy consumption values.

# Exercise 6: Drop the 'Temperature_C' column from df and display the result.

# Exercise 7: Merge two new DataFrames: one with building names and one with energy consumption.

# --- PART 5: MINI-PROJECT ---
# Load the provided dataset (e.g., building energy usage or material properties).
# 1. Load CSV into a DataFrame.
# 2. Show first 5 rows.
# 3. Compute summary statistics.
# 4. Clean the data (drop columns, handle NaN values).
# 5. Filter data by some condition (e.g., high energy use).
# 6. Merge with another dataset if available.
# 7. Create at least two visualizations (bar chart, line plot, histogram, etc.).

# Open datasets to practice with:
# - ASHRAE Global Thermal Comfort Database II: https://github.com/CenterForTheBuiltEnvironment/ashrae-db-II
