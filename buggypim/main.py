from pony import orm
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QLineEdit

db=orm.Database()

class TodoItem(db.Entity):
    id = orm.PrimaryKey(int, auto=True)
    text = orm.Required(str)
    important = orm.Required(bool, default=False)


def entry():
    '''Entry point'''
    try:
        db.bind(provider='sqlite', filename='buggypim.sqlite', create_db=True)
        db.generate_mapping(create_tables=True)
        orm.set_sql_debug(True)
        create_item()
        app = QApplication([])
        window = QWidget()
        layout = QVBoxLayout()
        todotable = QTableWidget()
        newitem = QLineEdit()
        layout.addWidget(todotable)
        layout.addWidget(newitem)
        layout.addWidget(QPushButton('Add item'))
        window.setLayout(layout)
        window.show()
        app.exec()
    except KeyboardInterrupt:
        print("Script interrupted by user.\n", file=sys.stderr)

@orm.db_session
def create_item():
       t=TodoItem(text="Write BuggyPIM!", important=True)

