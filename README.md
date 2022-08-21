# sqlalchemy-sandbox
/dev/sqlalchemy-sandbox/markdown_assets ~/dev/sqlalchemy-sandbox
(sqlalchemy-sandbox) rshea@tana:~/dev/sqlalchemy-sandbox/markdown_assets$ ls -l
total 52
-rw-rw-r-- 1 rshea rshea 51945 Aug 21 19:45 sql_logo_truncated.png
(sqlalchemy-sandbox) rshea@tana:~/dev/sqlalchemy-sandbox/markdown_assets$ ll
total 60
drwxrwxr-x 2 rshea rshea  4096 Aug 21 19:47 ./
drwxrwxr-x 5 rshea rshea  4096 Aug 21 19:49 ../
-rw-rw-r-- 1 rshea rshea 51945 Aug 21 19:45 sql_logo_truncated.png
(sqlalchemy-sandbox) rshea@tana:~/dev/sqlalchemy-sandbox/markdown_assets$ popd
~/dev/sqlalchemy-sandbox
(sqlalchemy-sandbox) rshea@tana:~/dev/sqlalchemy-sandbox$ vim README.md 

[1]+  Stopped                 vim README.md
(sqlalchemy-sandbox) 148 rshea@tana:~/dev/sqlalchemy-sandbox$ fg
vim README.md
(sqlalchemy-sandbox) rshea@tana:~/dev/sqlalchemy-sandbox$ 

![SQLAlchemy logo](markdown_assets/sql_logo_truncated.png)

This project is used to experiment with the [sqlalchemy](https://sqlalchemy.org) ORM. 

At least initially it's based around the [SQLAlchemy 1.4 tutorial](https://docs.sqlalchemy.org/en/14/tutorial/engine.html).


## virtual environment

The virtual environment for this project is managed by [pipenv](https://pipenv.pypa.io).
