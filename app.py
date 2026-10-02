from flask import Flask

app = Flask(__name__)

dialogue = """
WAKE UP TO REALITY

Nothing ever goes as planned in this accursed world.

The longer you live, the more you realize that the only things
that truly exist in this reality are pain, suffering and futility.

Wherever there is light, there are also shadows.

As long as there are winners, there must also be losers.

Peace and conflict are connected in this world.
"""

@app.route("/")
def home():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Madara Uchiha</title>

        <style>
            body {{
                background: #111;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }}

            h1 {{
                color: #b30000;
                font-size: 50px;
                margin-bottom: 10px;
            }}

            h2 {{
                font-style: italic;
                color: #ccc;
            }}

            .dialogue {{
                max-width: 800px;
                margin: 40px auto;
                padding: 30px;
                background: #222;
                border-radius: 10px;
                font-size: 20px;
                line-height: 1.8;
                white-space: pre-line;
                text-align: left;
            }}
        </style>
    </head>

    <body>

        <h1>MADARA UCHIHA</h1>

        <h2>"Wake up to reality..."</h2>

        <div class="dialogue">
            {dialogue}
        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)