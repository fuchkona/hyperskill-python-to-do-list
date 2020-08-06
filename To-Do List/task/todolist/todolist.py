# Write your code here
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()


class TaskTable(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def print_today_tasks():
    today = datetime.today()

    print(f"Today {today.day} {today.strftime('%b')}:")
    rows = session \
        .query(TaskTable) \
        .filter(TaskTable.deadline == today.date()) \
        .all()
    if len(rows) == 0:
        print("Nothing to do!")
        print()
    else:
        for i in range(len(rows)):
            print(f"{i + 1}. {rows[i]}")
            print()


def print_missed_tasks():
    print("Missed tasks:")
    rows = session \
        .query(TaskTable) \
        .filter(TaskTable.deadline < datetime.today().date()) \
        .order_by(TaskTable.deadline) \
        .all()
    if len(rows) == 0:
        print("Nothing is missed!")
    else:
        for i in range(len(rows)):
            deadline = rows[i].deadline
            print(f"{i + 1}. {rows[i].task}. {deadline.day} {deadline.strftime('%b')}")
    print()


def print_all_tasks():
    print("All tasks:")
    rows = session \
        .query(TaskTable) \
        .order_by(TaskTable.deadline) \
        .all()
    print_tasks(rows)


def print_tasks(rows):
    if len(rows) == 0:
        print("Nothing to do!")
        print()
    else:
        for i in range(len(rows)):
            deadline = rows[i].deadline
            print(f"{i + 1}. {rows[i].task}. {deadline.day} {deadline.strftime('%b')}")
            print()


def print_week_tasks():
    for day in range(7):
        today = datetime.today() + timedelta(days=day)
        rows = session \
            .query(TaskTable) \
            .filter(TaskTable.deadline == today.date()) \
            .all()
        print(today.strftime('%A %d %b'))
        if len(rows) == 0:
            print("Nothing to do!")
            print()
        else:
            for i in range(len(rows)):
                print(f"{i + 1}. {rows[i]}")
                print()


def add_task():
    print("Enter task")
    task_name = input()
    print("Enter deadline")
    input_date = input().split('-')
    task_deadline = datetime(
        int(input_date[0]),
        int(input_date[1]),
        int(input_date[2])
    )

    new_row = TaskTable(task=task_name, deadline=task_deadline)
    session.add(new_row)
    session.commit()

    print("The task has been added!")


def delete_task():
    print("Choose the number of the task you want to delete:")
    rows = session \
        .query(TaskTable) \
        .order_by(TaskTable.deadline) \
        .all()

    if len(rows) == 0:
        print("Nothing to delete")
        print()
    else:
        print_tasks(rows)
        task_to_delete = int(input()) - 1
        session.delete(rows[task_to_delete])
        session.commit()


def print_menu():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")


while True:
    print_menu()
    option = int(input())
    if option == 1:
        print_today_tasks()
    elif option == 2:
        print_week_tasks()
    elif option == 3:
        print_all_tasks()
    elif option == 4:
        print_missed_tasks()
    elif option == 5:
        add_task()
    elif option == 6:
        delete_task()
    else:
        print("Bye!")
        break
