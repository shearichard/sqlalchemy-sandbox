from sqlalchemy import create_engine, text

def getting_a_connection_example(engine):
    starry_box("getting_a_connection_example")
    #The context manager provides a database connection and frames
    #the operation inside of a transaction. When the scope of the 
    #connection is released a ROLLBACK is done.
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())


def committing_changes_example(engine):
    #Example of 'commit as you go'
    starry_box("committing_changes_example - commit as you go")
    #Any commits are done explicitly
    with engine.connect() as conn:
        conn.execute(text("CREATE TABLE some_table (x int, y int)"))
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
        )
        conn.commit()

    #Example of 'begin once'
    starry_box("committing_changes_example - begin once")
    #Declare the connect to be a transaction block up front, updates
    #will be committed unless an exception is raised.
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
            [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
        )


def main():
    engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

    #"Getting a connection"
    getting_a_connection_example(engine)

    #Committing Changes
    committing_changes_example(engine)

def starry_box(s):
    print()
    print("*******************************************************************")
    print("** " + s)
    print("*******************************************************************")


if __name__ == "__main__":
    main()
