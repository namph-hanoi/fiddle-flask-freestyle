import signal
from app.bootstrap import create_app
from app.config import Config

if __name__ == '__main__':
    print('alo')
    app = create_app()
    app.run(host=Config.APP_HOST, port=Config.APP_PORT, debug=Config.DEBUG)
