from database import engine, Base
import models

print("Building database tables...")

# This single line looks at everything inheriting from 'Base' 
# and creates the tables in the SQLite file.
Base.metadata.create_all(bind=engine)

print("Success! Check your folder for focus_logger.db")