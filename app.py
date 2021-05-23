from flask import request, Flask, jsonify
from routes import routes
import config

app = Flask(__name__)

# Start Routing
routes(app)

if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
