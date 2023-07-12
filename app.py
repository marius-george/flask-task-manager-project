import os
from flask import Flask, render_template
from pymongo import MongoClient

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    mongo_uri = app.config["MONGO_URI"]
    database_name = "task_manager"

    client = MongoClient(mongo_uri)
    db = client[database_name]
    tasks = db.tasks.find()

    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"), port=int(
        os.environ.get("PORT")), debug=True)
