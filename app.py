

import dash
from dash import dcc
from dash import html

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Sample data for the list of lists
list_of_lists = [
    {"name": "List 1", "items": ["Item 1.1", "Item 1.2", "Item 1.3"]},
    {"name": "List 2", "items": ["Item 2.1", "Item 2.2", "Item 2.3"]},
    {"name": "List 3", "items": ["Item 3.1", "Item 3.2", "Item 3.3"]}
]

# Define main list items as checkboxes
main_list_items = dcc.Checklist(
    id='main-list',
    options=[{'label': list_item['name'], 'value': list_item['name']} for list_item in list_of_lists]
)

# Define child lists initially hidden
child_lists = [html.Ul(id=f'list-{i}', style={'display': 'none'}) for i in range(len(list_of_lists))]

# Define app layout
app.layout = html.Div([
    html.H1("Collapsible List of Lists Example"),
    main_list_items,
    *child_lists
])

# Callback to show/hide child lists based on main list item selection
@app.callback(
    Output('list-0', 'style'),
    Output('list-1', 'style'),
    Output('list-2', 'style'),
    [Input('main-list', 'value')]
)
def toggle_child_lists(selected_items):
    styles = [{'display': 'none'} for _ in range(len(list_of_lists))]
    if selected_items:
        for item in selected_items:
            index = next((i for i, list_item in enumerate(list_of_lists) if list_item['name'] == item), None)
            if index is not None:
                styles[index] = {'display': 'block'}
    return styles[0], styles[1], styles[2]

if __name__ == '__main__':
    app.run_server(debug=True)

