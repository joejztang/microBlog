from app import create_app, db, cli
from app.models import User, Post, Notification, Message, Task
# from app.search import add_to_index, remove_from_index, query_index

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification, 'Task': Task}
