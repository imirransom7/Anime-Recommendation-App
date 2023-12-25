from anime_web import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

# only if this file is run, then this line is executed
# only runs web server if I run this file
if __name__ == '__main__':
    # auto rerun the web server when changes made
    app.run(debug=True)
