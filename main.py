from anime_web import create_app

app = create_app()

# only if this file is run, then this line is executed
# only runs web server if I run this file
if __name__ == '__main__':
    # auto rerun the web server when changes made
    app.run(debug=True)
