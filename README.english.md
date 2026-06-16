# Country Searcher

🇧🇷 [Português](README.pt-BR.md) | 🇺🇸 English

A web application that consumes an external geographic data API. The user types a country name and receives detailed information about it directly on the screen.

---

## Features

- Country search by name
- Display of API data (capital, population, region, flag, etc.)
- Error handling for invalid or not-found countries

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Flask | Web framework for routing and serving the app |
| Requests | Consuming the external REST API |
| HTML/CSS | User interface |

---

## Concepts Applied

- Python data structures
- Web application development with Flask
- Defining pages and endpoints
- HTML form handling
- REST API consumption
- HTTP response handling
- Exception handling
- JSON manipulation

---

## Prerequisites

- Python 3.x
- Internet connection (to access the external API)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/natapereirax-cmd/CountrySearcher.git
cd CountrySearcher
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Use

Run the main file inside the `web_page` folder:

```bash
cd web_page
python app.py
```

Open in your browser: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Type a country name in the search field and press Enter. The country's information will be displayed on the screen.

---

## Project Structure

```
CountrySearcher/
├── web_page/
│   └── app.py          # Main Flask application
├── requirements.txt    # Project dependencies
└── LEIAME.txt          # Plain text instructions (Portuguese)
```
