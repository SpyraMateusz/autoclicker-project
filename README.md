AUTCLICKER API

Autor: Mateusz Spyra
Numer indeksu: 54179
Kod kursu: Nowatorski Projekt - DevOps

OPIS PROJEKTU
Projekt przedstawia prosty API autoclickera korzystajacy z bazy danych PostgreSQL.
API posiada dwa endpointy:
- POST /click – zwieksza licznik klikniec o 1
- GET /status – zwraca aktualna liczbe klikniec

TECHNOLOGIE
- Python 3.11 + FastAPI
- PostgreSQL (kontener)
- Docker (multi-stage build)
- Docker Compose (uruchamianie dwoch kontenerow)
- GitHub Actions (CI: oddzielne workflow dla main i pull requestow)

URUCHOMIENIE PROJEKTU
1. Sklonuj repozytorium:
   git clone <repo-url>
   cd autoclicker-project
2. Uruchom aplikacje z Docker Compose:
   docker-compose up --build
3. API dostepne pod adresem: http://localhost:8000
4. Testy mozna uruchomic lokalnie:
   pytest app/test_main.py