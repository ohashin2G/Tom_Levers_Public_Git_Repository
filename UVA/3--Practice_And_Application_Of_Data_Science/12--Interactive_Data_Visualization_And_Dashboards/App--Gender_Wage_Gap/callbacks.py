from dash import Dash, dash_table, html, dcc, Output, Input, ctx
from datastructures import *
import plotly.express as px

app = Dash(
    __name__,
    external_stylesheets = [
        'https://codepen.io/chriddyp/pen/bWLwgP.css'
    ]
)

@app.callback(
    Output(
        component_id = 'title_of_figure',
        component_property = 'children'
    ),
    Input(
        component_id = 'button_labeled_Introduction',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Socioeconomic_Success_By_Sex',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Interactive_Bar_Plot',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Annual_Income_Versus_Occupational_Prestige',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Distributions_Of_Income_By_Sex_And_Occupational_Prestige',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Distributions_Of_Income_And_Occupational_Prestige_By_Sex',
        component_property = 'n_clicks'
    )
)
# The following formal parameters are required given the above inputs.
def generate_title_for_figure(
    number_of_clicks_of_button_labeled_Introduction,
    number_of_clicks_of_button_labeled_Socioeconomic_Success_By_Sex,
    number_of_clicks_of_button_labeled_Bar_Plot,
    number_of_clicks_of_button_labeled_Annual_Income_Versus_Occupational_Prestige,
    number_of_clicks_of_button_labeled_Distributions_Of_Income_By_Sex_And_Occupational_Prestige,
    number_of_clicks_of_button_labeled_Distributions_Of_Income_And_Occupational_Prestige_By_Sex
):
    button_clicked = ctx.triggered_id
    if (button_clicked == None) or (button_clicked == 'button_labeled_Introduction'):
        return 'Introduction'
    elif button_clicked == 'button_labeled_Socioeconomic_Success_By_Sex':
        return 'Socioeconomic Success By Sex'
    elif button_clicked == 'button_labeled_Interactive_Bar_Plot':
        return 'Interactive Bar Plot'
    elif button_clicked == 'button_labeled_Annual_Income_Versus_Occupational_Prestige':
        return 'Annual Income Versus Occupational Prestige'
    elif button_clicked == 'button_labeled_Distributions_Of_Income_By_Sex_And_Occupational_Prestige':
        return 'Distributions Of Income By Sex And Occupational Prestige'
    elif button_clicked == 'button_labeled_Distributions_Of_Income_And_Occupational_Prestige_By_Sex':
        return 'Distributions Of Income And Occupational Prestige By Sex'
    else:
        return 'Placeholder'
    
@app.callback(
    Output(
        component_id = 'figure',
        component_property = 'children'
    ),
    Input(
        component_id = 'button_labeled_Introduction',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Socioeconomic_Success_By_Sex',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Interactive_Bar_Plot',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Annual_Income_Versus_Occupational_Prestige',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Distributions_Of_Income_By_Sex_And_Occupational_Prestige',
        component_property = 'n_clicks'
    ),
    Input(
        component_id = 'button_labeled_Distributions_Of_Income_And_Occupational_Prestige_By_Sex',
        component_property = 'n_clicks'
    )
)
def generate_figure(
    number_of_clicks_of_button_labeled_Introduction,
    number_of_clicks_of_button_labeled_Socioeconomic_Success_By_Sex,
    number_of_clicks_of_button_labeled_Bar_Plot,
    number_of_clicks_of_button_labeled_Annual_Income_Versus_Occupational_Prestige,
    number_of_clicks_of_button_labeled_Distributions_Of_Income_By_Sex_And_Occupational_Prestige,
    number_of_clicks_of_button_labeled_Distributions_Of_Income_And_Occupational_Prestige_By_Sex
):
    button_clicked = ctx.triggered_id
    if (button_clicked == None) or (button_clicked == 'button_labeled_Introduction'):
        return html.Div(
            [
                dcc.Markdown(paragraph_1),
                dcc.Markdown(paragraph_2)
            ]
        )
    elif button_clicked == 'button_labeled_Socioeconomic_Success_By_Sex':
        return html.Div(
            dash_table.DataTable(
                data = data_frame.to_dict(orient = 'records'),
                sort_action = 'native'
            )
        )
    elif button_clicked == 'button_labeled_Interactive_Bar_Plot':
        return html.Div(
            [
                dcc.Graph(
                    id = 'bar_plot'
                ),
                'Select feature for which to create a bar plot.',
                dcc.Dropdown(
                    id = 'dropdown_menu_for_feature_whose_categories_forms_the_basis_of_bars',
                    options = list(description_to_feature_whose_categories_forms_the_basis_of_bars.keys()),
                    value = 'Job Satisfaction'
                ),
                html.Br(),
                'Select feature by which to group bars.',
                dcc.Dropdown(
                    id = 'dropdown_menu_for_feature_by_which_to_group',
                    options = list(description_to_feature_by_which_to_group.keys()),
                    value = 'None'
                )
            ]
        )
    elif button_clicked == 'button_labeled_Annual_Income_Versus_Occupational_Prestige':
        return dcc.Graph(figure = scatter_plot)
    elif button_clicked == 'button_labeled_Distributions_Of_Income_By_Sex_And_Occupational_Prestige':
        return dcc.Graph(figure = facet_grid)
    elif button_clicked == 'button_labeled_Distributions_Of_Income_And_Occupational_Prestige_By_Sex':
        return html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(figure = distributions_of_income_by_sex)
                    ],
                    style = {
                        'width': '48%',
                        'float': 'left'
                    }
                ),
                html.Div(
                    [            
                        dcc.Graph(figure = distributions_of_occupational_prestige_by_sex)
                    ],
                    style = {
                        'width': '48%',
                        'float': 'right'
                    }
                )
            ]
        )
    else:
        return 'Placeholder'

@app.callback(
    Output(
        component_id = 'bar_plot',
        component_property = 'figure'
    ),
    Input(
        component_id = 'dropdown_menu_for_feature_whose_categories_forms_the_basis_of_bars',
        component_property = 'value'
    ),
    Input(
        component_id = 'dropdown_menu_for_feature_by_which_to_group',
        component_property = 'value'
    )
)
def generate_bar_plot(
    description_of_feature_whose_categories_form_the_basis_of_bars,
    description_of_feature_by_which_to_group
):
    feature_whose_categories_forms_the_basis_of_bars = description_to_feature_whose_categories_forms_the_basis_of_bars[description_of_feature_whose_categories_form_the_basis_of_bars]
    horizontal_axis_label = feature_whose_categories_forms_the_basis_of_bars_to_bar_plot_horizontal_axis_label[feature_whose_categories_forms_the_basis_of_bars]
    feature_by_which_to_group = description_to_feature_by_which_to_group[description_of_feature_by_which_to_group]
    if feature_by_which_to_group == 'None':
        grouped_value_counts = (
            data_frame_of_data_of_General_Social_Survey.groupby(
                [
                    feature_whose_categories_forms_the_basis_of_bars
                ]
            )
            .size()
            .reset_index()
            .rename(
                columns = {
                    feature_whose_categories_forms_the_basis_of_bars: horizontal_axis_label,
                    0: 'number of people'
                }
            )
        )
        bar_plot = px.bar(
            grouped_value_counts,
            x = horizontal_axis_label,
            y = 'number of people',
            title = description_of_feature_whose_categories_form_the_basis_of_bars
        )
    else:
        grouped_value_counts = (
            data_frame_of_data_of_General_Social_Survey.groupby(
                [
                    feature_whose_categories_forms_the_basis_of_bars,
                    feature_by_which_to_group
                ]
            )
            .size()
            .reset_index()
            .rename(
                columns = {
                    feature_whose_categories_forms_the_basis_of_bars: horizontal_axis_label,
                    0: 'number of people'
                }
            )
        )
        bar_plot = px.bar(
            grouped_value_counts,
            x = horizontal_axis_label,
            y = 'number of people',
            title = description_of_feature_whose_categories_form_the_basis_of_bars,
            color = feature_by_which_to_group,
            barmode = 'group'
        )
    return bar_plot