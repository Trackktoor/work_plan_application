from app import app
import view
from WorkPlan.workPlanBlueprint import work_plan
from flask_graphql import GraphQLView
from app import app
from schema.schema import shema

app.register_blueprint(work_plan, url_prefix='/work_plan')

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=shema,
        graphiql=True  # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run()