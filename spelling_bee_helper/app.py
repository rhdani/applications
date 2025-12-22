# app.py
from flask import Flask, flash, render_template, request, redirect, url_for
from solver import load_words, solve

app = Flask(__name__)
app.secret_key = "dev-secret-key"
WORD_FILE = "words.txt"
WORDS = sorted(load_words())

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        center = request.form["center"].lower()
        others = request.form["others"].lower()
        result = solve(center, others, WORDS)

    return render_template("index.html", result=result)

@app.route("/add-word", methods=["POST"])
def add_word():
    global WORDS

    raw_input = request.form["new_word"].strip().lower()

    # split on whitespace
    candidates = raw_input.split()

    added = []
    skipped = []

    with open(WORD_FILE, "a") as f:
        for word in candidates:
            # basic validation
            if len(word) >= 4 and word.isalpha() and word not in WORDS and not word.endswith("s"):
                f.write(word + "\n")
                WORDS.append(word)
                added.append(word)
            else:
                skipped.append(word)
    if added:
        flash(f"Added {len(added)} word(s): {', '.join(added)}")
    if skipped:
        flash(f"Skipped {len(skipped)} word(s): {', '.join(skipped)}")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

