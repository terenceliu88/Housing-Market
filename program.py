"""
This is a plotly program that creates a graph
"""
import plotly.graph_objects as go
import csv


# Convert csv file to tuple[list]
def read_csv(filename: str) -> dict:
    """Return x and y values in filename"""
    data = {}
    with open(filename) as file:
        reader = csv.reader(file)

        for n in reader:
            if n[0][0:2] == 'q1':
                n[0] = '20' + n[0][3:5] + '-' + '01-01'
                data[n[0]] = float(n[1])
            elif n[0][0:2] == 'q2':
                n[0] = '20' + n[0][3:5] + '-' + '04-01'
                data[n[0]] = float(n[1])
            elif n[0][0:2] == 'q3':
                n[0] = '20' + n[0][3:5] + '-' + '07-01'
                data[n[0]] = float(n[1])
            elif n[0][0:2] == 'q4':
                n[0] = '20' + n[0][3:5] + '-' + '10-01'
                data[n[0]] = float(n[1])
            elif not n[0].isalpha() and not n[1].isalpha():
                data[n[0]] = float(n[1])

    return data


# Create line graph traces
def graph_data(data: dict[dict]) -> None:
    """
    Create a graph with plotly using the provided data
    """
    fig = go.Figure()
    colors = ['gold', 'purple', 'orange', 'lime', 'red', 'blue']

    for line in data:
        x_values = list(data[line].keys())
        y_values = list(data[line].values())

        fig.add_trace(go.Scatter(x=x_values, y=y_values,
                                mode='lines',
                                name=line,
                                line=dict(color=colors.pop(), width=4)))

    # Label axis
    fig.update_layout(title='Predicted House Pricing',
                    xaxis_title='Year',
                    yaxis_title='Money (Thousand)')

    fig.show()
