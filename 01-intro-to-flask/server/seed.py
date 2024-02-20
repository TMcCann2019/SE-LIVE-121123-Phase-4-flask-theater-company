#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
    # db and Production from models
from app import app
from models import db, Production

# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`

# 8.✅ Create a query to delete all existing records from Production    
def clear_database():
    print("Clearing the database...")
    Production.query.delete()

# 9.✅ Create some seeds for production and commit them to the database.
    
def create_productions():
    print("Creating productions...")
    productions = []

    p1 = Production(
        title = "Hamlet",
        genre= "Drama",
        budget = 10000,
        director = "Bill S. Peare",
        description = "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah",
        ongoing = True
    )

    productions.append(p1)

    p2 = Production(
        title = "Cats",
        genre= "Musical",
        budget = 20000,
        director = "Andrew Lloyd Webber",
        description = "blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah",
        ongoing = True
    )

    productions.append(p2)

    p3 = Production(
        title = "Carmen",
        genre= "Opera",
        budget = 20000,
        director = "Georges Bizet",
        description = "blah",
        ongoing = True
    )

    productions.append(p3)

    p4 = Production(
        title = "Hamilton",
        genre= "Musical",
        budget = 40000,
        director = "Lin-Manuel Miranda",
        description = "blah blah",
        ongoing = True
    )

    productions.append(p4)

    db.session.add_all(productions)
    db.session.commit()

# 10.✅ Run in terminal:
# `python seed.py`
# 11.✅ run `flask shell` in the terminal 
# from app import app
# from models import Production
# Check the seeds by querying Production
# 12.✅ Navigate back to app.py  

if __name__ == '__main__':
    # 7. ✅ Create application context `with app.app_context():`
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
    with app.app_context():
        clear_database()
        create_productions()