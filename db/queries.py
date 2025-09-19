CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL
    )
"""


INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"


SELECT_TASKS = "SELECT id, task FROM tasks"


DELETE_TASK = "DELETE FROM tasks WHERE id = ?"


UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"