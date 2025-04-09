from data_fetcher import load_elevation_data
from analysis import analyze_interpolation, analyze_interpolation_chebyshev
import numpy as np

def main():
    # Przykładowe pliki CSV
    filenames = [
        #'data/GlebiaChallengera.csv',
        'data/MountEverest.csv',
        'data/SpacerniakGdansk.csv',
        'data/GlebiaChallengera.csv',
        'data/WielkiKanionKolorado.csv',
        'data/MountEverest.csv',
        'data/SpacerniakGdansk.csv',
        'data/WielkiKanionKolorado.csv'

    ]

    for filename in filenames:
        # Pobierz dane wysokościowe z pliku CSV
        x, y = load_elevation_data(filename)
        print(f"Dane z {filename}:")
        print("Odległości:", x)
        print("Wysokości:", y)

        analyze_interpolation_chebyshev(x, y, filename.split('/')[-1])
        # Analiza interpolacji Lagrange'a
        analyze_interpolation(x, y, 'Lagrange', filename.split('/')[-1])

        # Analiza interpolacji funkcjami sklejanymi
        analyze_interpolation(x, y, 'Spline', filename.split('/')[-1])

if __name__ == "__main__":
    main()
