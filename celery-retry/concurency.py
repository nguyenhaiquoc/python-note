from sqlalchemy import Column, Integer, String, create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy engine
engine = create_engine(
    "postgresql://username:password@localhost:5432/database"
)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create the base class for declarative models
Base = declarative_base()


# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(Integer)


# Create the table if it doesn't exist
Base.metadata.create_all(engine)

# Create a new session
session = Session()

# Perform an update with optimistic concurrency control
user_id = 1
new_name = "New Name"
new_version = 1

stmt = update(User).where(User.id == user_id, User.version == new_version)
stmt = stmt.values(name=new_name, version=User.version + 1)
result = session.execute(stmt)
if result.rowcount == 0:
    # The update failed due to concurrency conflict
    print("Concurrency conflict detected. Please try again.")

# Commit the changes
session.commit()

# Close the session
session.close()
