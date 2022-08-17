#  coding: utf-8
from logging import getLogger

from flask import Flask
from flask_cors import CORS

from app.configs.logs import init_logging
from app.twitterBot.routes import twitter
from app.configs.caching import init_cache

init_logging()
logger = getLogger("twitter")

app = Flask(__name__)
init_cache(app)

app.config['TESTING'] = True

logger.debug("INIT_ROUTINE Habilitando CORS")
CORS(app)

logger.debug("INIT_ROUTINE Registrando rotas do twitter")
app.register_blueprint(blueprint=twitter, url_prefix="/twitter")

if __name__ == "__main__":
    app.run(threaded=True)
