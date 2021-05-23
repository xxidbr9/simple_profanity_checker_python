from .bad_word_routes import init_bad_word_routes

# routing all service
def routes(app):
    init_bad_word_routes(app)
