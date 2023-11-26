import dash
from dash import dcc, html

app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Mad Libs"),
    dcc.Input(id='noun-input', type='text', placeholder='Enter a noun'),
    dcc.Input(id='verb-input', type='text', placeholder='Enter a verb'),
    dcc.Input(id='adjective-input', type='text', placeholder='Enter an adjective'),
    html.Button('Generate Mad Libs', id='submit-button', n_clicks=0),
    html.Div(id='mad-libs-output', style={'marginTop': 20})
])

# Define the callback to update the output based on user input
@app.callback(
    dash.dependencies.Output('mad-libs-output', 'children'),
    [dash.dependencies.Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('noun-input', 'value'),
     dash.dependencies.State('verb-input', 'value'),
     dash.dependencies.State('adjective-input', 'value')]
)
def update_output(n_clicks, noun, verb, adjective):
    if n_clicks > 0:
        mad_libs_sentence = f"Once upon a time, there was a {noun} who loved to {verb} in the {adjective} forest."
        return html.Div([
            html.H3("Generated Mad Libs:"),
            html.P(mad_libs_sentence)
        ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True,host = '127.0.0.1')
