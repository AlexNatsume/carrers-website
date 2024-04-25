from sqlalchemy import create_engine, text
import os


db_connection = os.environ['DB_CONNECTION']
engine = create_engine(db_connection)


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs
  

