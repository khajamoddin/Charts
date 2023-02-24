import plotly.express as px
import pandas as pd

# Read in file
file_path = input("Enter file path: ")
if file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
elif file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith(".json"):
    df = pd.read_json(file_path)
else:
    print("Invalid file format. Please provide a file in .xlsx, .csv, or .json format.")
    exit()

# Generate chart
chart_type = input("Enter chart type (e.g. scatter, bar, line, pie): ")
x_axis_col = input("Enter name of column for X-axis: ")
y_axis_col = input("Enter name of column for Y-axis: ")
chart_title = input("Enter chart title: ")
fig = px.scatter(df, x=x_axis_col, y=y_axis_col, title=chart_title) if chart_type == "scatter" else \
      px.bar(df, x=x_axis_col, y=y_axis_col, title=chart_title) if chart_type == "bar" else \
      px.line(df, x=x_axis_col, y=y_axis_col, title=chart_title) if chart_type == "line" else \
      px.pie(df, names=x_axis_col, values=y_axis_col, title=chart_title) if chart_type == "pie" else None
if not fig:
    print("Invalid chart type. Please choose from scatter, bar, line, or pie.")
    exit()

# Show chart
fig.show()
