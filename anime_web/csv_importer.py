from .models import AnimeDataset, db
import csv


def import_csv_to_anime_dataset(csv_path):
    with open(csv_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row if it exists

        for row in csv_reader:
            anime_entry = AnimeDataset(
                anime_id=row[0],
                name=row[1],
                score=float(row[2]),
                genre=row[3],
                english_name=row[4],
                japanese_name=row[5],
                synopsis=row[6],
                type=row[7],
                episodes=row[8],
                aired=row[9],
                premiered=row[10],
                producers=row[11],
                licensors=row[12],
                studios=row[13],
                source=row[14],
                duration=row[15],
                rating=row[16],
                ranked=row[17],
                popularity=row[18],
                members=row[19],
                favorites=row[20],
                watching=row[21],
                completed=row[22],
                on_hold=row[23],
                dropped=row[24]


            )

            db.session.add(anime_entry)

    db.session.commit()
