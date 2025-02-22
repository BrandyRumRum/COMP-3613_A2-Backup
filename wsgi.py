import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Staff, Course, CourseStaff, CourseAdmin
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, create_staff, create_course, assign_staff, view_course_staff )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("name", default="Rob")
def create_user_command(username, password, name):
    create_user(username, password, name)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)

'''
Staff Commands
'''

staff_cli = AppGroup('staff', help='Staff object commands')

@staff_cli.command('create-staff')
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_staff_command(username, password):
    roles = {1: "Lecturer", 
             2: "TA", 
             3: "Tutor"}
    role_id = 0
    
    name = input("Enter staff member's name: ")
    while role_id not in (1,2,3):
        role_id = int(input("Enter role {Lecturer: 1, TA: 2, Tutor: 3}: "))
    role = roles.get(role_id)
    create_staff(username, password, name, role)

app.cli.add_command(staff_cli)

'''
Course Admin Commands
'''

course_admin_cli = AppGroup('admin', help='Staff object commands')

@course_admin_cli.command('create-course')
def create_course_command():
    name = input("Enter course name: ")
    description = input("Enter course description: ")
    create_course(name, description)

@course_admin_cli.command('assign-staff')
def assign_staff_command():
    course_name = input("Enter course name: ")
    staff_name = input("Enter staff member's name: ")
    assign_staff(course_name, staff_name)

@course_admin_cli.command('view-course-staff')
def view_course_staff_command():
    course_name = input("Enter course name: ")
    view_course_staff(course_name)

app.cli.add_command(course_admin_cli)