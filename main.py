from server import app, celery


if __name__  == "__main__":
    app.run(debug=False)
