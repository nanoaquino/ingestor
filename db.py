from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('oracle://INSIS_PEOPLE_V10:people__v10@insis.cl5u1tcuiscl.us-east-1.rds.amazonaws.com/orcl')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()