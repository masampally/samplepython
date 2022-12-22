from module_init import app
from module_init import debug
from module_init import graphql_mapping


from schema import schema
# from schema import Mutation

from flask_graphql import GraphQLView

view_func = GraphQLView.as_view(
    'graphql', 
    schema=schema, 
    graphiql=True
)

app.add_url_rule(graphql_mapping, view_func=view_func)

if __name__ == '__main__':
    app.run(debug=debug, port=5050)
