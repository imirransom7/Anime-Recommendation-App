from anime_web import create_app


app = create_app()

# with app.app_context():
#     with open('anime-filtered.csv', 'r') as file:
#         csv_reader = csv.reader(file)
#         next(csv_reader)  # Skip header if needed
#         for row in csv_reader:
#             entry = AnimeDataset(column1=row[0], column2=row[1])
#             db.session.add(entry)
#
#     db.session.commit()


# only if this file is run, then this line is executed
# only runs web server if I run this file
if __name__ == '__main__':
    # auto rerun the web server when changes made
    app.run(debug=True)
