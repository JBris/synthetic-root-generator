from flask import Flask, redirect
from flask_cors import CORS
from graphql_server.flask import GraphQLView
from graphql_api.schema import schema
from services.config import Config
from services.cache import Cache
from tasks.task_queue import TaskQueue

app = Flask(__name__)
CORS(app)
config = Config()
cache = Cache(config.get("REDIS_HOST", "redis"), config.get("REDIS_PORT", 6379))
queue = TaskQueue()
app.config["CONFIG"] = config
app.config["CACHE"] = cache
app.config["TASK_QUEUE"] = queue
app.config["JSON_SORT_KEYS"] = False

app.config["CELERY"] = {
    "broker_url": config.get("CELERY_BROKER_URL", "redis://redis:6379/0"),
    "result_backend": config.get("CELERY_RESULT_BACKEND", "redis://redis:6379/0"),
    "task_ignore_result": True
}

celery_app = queue.init_celery_app(app)
app.config["CELERY_APP"] = celery_app

@app.route("/")
def home():
    return redirect("graphql", code = 303)

app.add_url_rule(
    '/graphql',
    view_func = GraphQLView.as_view(
        'graphql',
        schema = schema,
        graphiql = True,
        batch = True
    )
)

if __name__ == '__main__':
    app.run(
        host = config.get('FLASK_HOST', '0.0.0.0'), 
        port = config.get('FLASK_PORT', '5000')
    )
