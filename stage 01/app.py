from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(
        slackUsername="daily_tee",
        backend=True,
        age=20,
        bio="I am a Backend Developer"
    )


if __name__ == '__main__':
    app.run(debug=True)