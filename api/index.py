from . import create_app

app = create_app()

# This will allow Vercel to find the app
if __name__ == "__main__":
    app.run()