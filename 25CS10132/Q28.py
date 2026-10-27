import pandas as pd
import plotly.express as px

# 1. Load the student examination data for Mathematics
data = {
    "Student": [
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "S10",
    ],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
}

df = pd.DataFrame(data)

# 2. Create an interactive bar chart using Plotly Express (Fixed parameter name)
fig = px.bar(
    df,
    x="Student",
    y="Mathematics",
    title="Marimport pandas as pd
import plotly.express as px

# 1. Load the student examination data for Mathematics
data = {
    "Student": [
        "S1",
        "S2",
        "S3",
        "S4",
        "S5",
        "S6",
        "S7",
        "S8",
        "S9",
        "S10",
    ],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
}

df =Traceback (most recent call last):
  File "/home/nitcslab/Bikram(Python)/25CS10132/Q28.py", line 24, in <module>
    fig = px.bar(
          ^^^^^^^
TypeError: bar() got an unexpected keyword argument 'color_continuousscale'
nitcslab@nitcslab-OptiPlex-5060:~$ 

 pd.DataFrame(data)

# 2. Create an interactive bar chart using Plotly Express
fig = px.b
    df,
    x="Student",
    y="Mathematics",
    Traceback (most recent call last):
  File "/home/nitcslab/Bikram(Python)/25CS10132/Q28.py", line 24, in <module>
    fig = px.bar(
          ^^^^^^^
TypeError: bar() got an unexpected keyword argument 'color_continuousscale'
nitcslab@nitcslab-OptiPlex-5060:~$ 

title="Marks Obtained by Students in Mathematics",
    labels={"Student": "Student ID", "Mathematics": "Mathematics Marks"},
    text="Mathematics",
    color="Mathematics",
    color_continuousscale="Blues",
)

# Customize layout for better appearance
fig.update_traces(texttemplate="%{text}", textposition="outside")
fig.update_layout(
    xaxis_title="Student",
    yaxis_title="Marks",
    Traceback (most recent call last):
  File "/home/nitcslab/Bikram(Python)/25CS10132/Q28.py", line 24, in <module>
    fig = px.bar(
          ^^^^^^^
TypeError: bar() got an unexpected keyword argument 'color_continuousscale'
nitcslab@nitcslab-OptiPlex-5060:~$ 

uniformtext_minsize=8,
    uniformtext_mode="hide",
)

# 3. Save the interactive chart as an HTML file instead of fig.show()
fig.write_html("math_marks_chart.html")
print("Chart successfully saved as 'math_marks_chart.html'!")ks Obtained by Students in Mathematics",
    labels={"Student": "Student ID", "Mathematics": "Mathematics Marks"},
    text="Mathematics",
    color="Mathematics",
    color_continuous_scale="Blues",  # Corrected argument name here
)

# Customize layout for better appearance
fig.update_traces(texttemplate="%{text}", textposition="outside")
fig.update_layout(
    xaxis_title="Student",
    yaxis_title="Marks",
    uniformtext_minsize=8,
    uniformtext_mode="hide",
)

# 3. Display the interactive chart
fig.show()