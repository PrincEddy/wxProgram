from app_init import create_app

def server_run():
    app = create_app()
    app.run();

if __name__ == '__main__':
    server_run()
