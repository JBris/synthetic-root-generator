from celery import Celery, Task
import flask

class TaskQueue:
    """Thin wrapper for the Celery task worker.
    """

    def init_celery_app(self, app: flask.Flask) -> Celery:
        """Initialise a new Celery application.

        Args:
            app (flask.Flask): The Flask application.

        Returns:
            Celery: The new Celery application.
        """
        class FlaskTask(Task):
            def __call__(self, *args: object, **kwargs: object) -> object:
                with app.app_context():
                    return self.run(*args, **kwargs)

        celery_app = Celery(app.name, task_cls = FlaskTask)
        celery_app.config_from_object(app.config["CELERY"])
        celery_app.set_default()
        app.extensions["celery"] = celery_app
        return celery_app
