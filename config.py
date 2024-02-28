import urllib.parse

mysql_username = 'root'

# used to encode the password since the password has a '@' symbol in it
mysql_password = urllib.parse.quote_plus('Stephanie@7')

secret_key = 'THIS IS THE SECRET KEY'

# path for the connection to the database in my MySQL
mysql_path = f'mysql://root:{mysql_password}@localhost/anime_data'

DB_NAME = 'database.db'

sql_lite_connection = f'sqlite:///{DB_NAME}'
