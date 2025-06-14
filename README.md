sledzenie-zdarzen-blockchain

Projekt dyplomowy: Zastosowanie mechanizmu łańcucha bloków do śledzenia newralgicznych zdarzeń produkcyjnych

Opis projektu

W tym repozytorium znajduje się symulator urządzenia generującego zdarzenia produkcyjne oraz konfiguracja Docker/Docker Compose do uruchomienia symulacji w kontenerach. Każde zdarzenie obejmuje:

event_id: unikalny identyfikator UUID4

timestamp: czas UTC (bez mikrosekund) w formacie ISO-8601

salt: losowe 8 bajtów (hex)

hash_value: SHA-256 hash z połączonych wartości powyżej

Dane te w docelowej wersji będą wysyłane do smart kontraktu na blockchainie Solana.

Struktura katalogów

sledzenie-zdarzen-blockchain/
├── device_sim/               # kod symulatora urządzenia
│   ├── simulate.py           # skrypt generuje zdarzenia i zapisuje do pliku
│   └── requirements.txt      # zależności Pythona 
├── data/                     # katalog na logi (montowany jako wolumen)
├── Dockerfile                # instrukcje budowy obrazu kontenera
├── docker-compose.yml        # konfiguracja usług i sieci Docker Compose
├── .gitignore                # pliki i katalogi ignorowane przez Git
└── README.md                 # ten plik

Szybki start
1. Budowa i uruchomienie -> docker compose up --build
2. 

