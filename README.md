# DataAnalysis Web App Tutorial

## Setup & Installtion

Make sure you have the 3.9.9 or more version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements\devrequirements.txt
```

## Change Postgres SQL connection string 
``` File "__init__.py"
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:123mrp.NET@localhost/{DB_NAME}'

## Running The App

```bash
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`
