from flask import render_template, request, redirect, url_for
from models.task_model import task_list_db

def register_routes(app):
    
    @app.route('/')
    def index():
        tasks = task_list_db.to_list()
        return render_template('index.html', tasks=tasks)

    @app.route('/add', methods=['POST'])
    def add_task():
        title = request.form.get('taskTitle', '').strip()
        description = request.form.get('taskDesc', '').strip()
        if title:
            task_list_db.append(title, description) 
        return redirect(url_for('index'))

    @app.route('/toggle/<int:task_id>')
    def toggle_task(task_id):
        task_list_db.toggle_status(task_id)
        return redirect(url_for('index'))

    @app.route('/delete/<int:task_id>')
    def delete_task(task_id):
        task_list_db.delete(task_id)
        return redirect(url_for('index'))