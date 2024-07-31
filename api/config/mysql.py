from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://webmonitor:admin123!@192.168.0.25:3306/MonitorWeb_admin")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)
meta = MetaData()
Base = declarative_base()