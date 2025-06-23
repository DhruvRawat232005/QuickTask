from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_FILE = 'tasks.db'

# Initialize database
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task TEXT NOT NULL,
                tag TEXT,
                done INTEGER DEFAULT 0
            )
        ''')

@app.route('/')
def index():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    tag = request.form['tag']
    if task:
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute("INSERT INTO tasks (task, tag, done) VALUES (?, ?, 0)", (task, tag))
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle(task_id):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT done FROM tasks WHERE id = ?", (task_id,))
        current = cur.fetchone()[0]
        new_status = 0 if current else 1
        conn.execute("UPDATE tasks SET done = ? WHERE id = ?", (new_status, task_id))
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
