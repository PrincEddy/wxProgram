from app_init import create_app

def run():
    app = create_app()
    app.run();

if __name__ == '__main__':
    run()
