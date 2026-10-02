from flask import Flask, request, redirect, render_template
import psycopg2
import time

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host="database",
        database="madara_db",
        user="madara_user",
        password="madara_password"
    )


def init_database():
    while True:
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS quotes (
                    id SERIAL PRIMARY KEY,
                    quote TEXT NOT NULL
                )
            """)

            connection.commit()
            cursor.close()
            connection.close()

            print("Database connected successfully!")
            break

        except Exception as error:
            print("Waiting for database...")
            print(error)
            time.sleep(2)


@app.route("/")
def home():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, quote FROM quotes ORDER BY id DESC")
    quotes = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", quotes=quotes)


@app.route("/add", methods=["POST"])
def add_quote():
    quote = request.form["quote"]

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO quotes (quote) VALUES (%s)",
        (quote,)
    )

    connection.commit()

    cursor.close()
    connection.close()

    return redirect("/")


if __name__ == "__main__":
    init_database()
    app.run(host="0.0.0.0", port=8080, debug=True)