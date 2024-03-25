import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Generate Plotly figures
fig1 = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='lines', name='Figure 1'))
fig2 = go.Figure(go.Bar(x=['A', 'B', 'C'], y=[10, 20, 30], name='Figure 2'))
fig3 = go.Figure(go.Pie(labels=['A', 'B', 'C'], values=[40, 30, 20], name='Figure 3'))
fig4 = go.Figure(go.Scatter(x=[1, 2, 3], y=[10, 5, 8], mode='markers', name='Figure 4'))

# Create subplots
fig = make_subplots(rows=2, cols=2, subplot_titles=("Figure 1", "Figure 2", "Figure 3", "Figure 4"))
fig.add_trace(fig1.data[0], row=1, col=1)
fig.add_trace(fig2.data[0], row=1, col=2)
fig.add_trace(fig3.data[0], row=2, col=1)
fig.add_trace(fig4.data[0], row=2, col=2)

# Update layout
fig.update_layout(title_text="Plotly Figures", showlegend=False)

# Convert the figure to HTML
fig_html = fig.to_html(full_html=False)

# Create HTML file content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Plotly Figures</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>Plotly Figures</h1>
    {fig_html}
</body>
</html>
"""

# Write the HTML content to a file
with open('index.html', 'w') as f:
    f.write(html_content)
