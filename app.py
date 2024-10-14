# from iebank_api import app
# from flask_cors import CORS  

# # Enable CORS for all routes
# CORS(app)

# if __name__ == '__main__':
#     app.run(debug=True)

# app.config.from_object('config.LocalConfig')

from iebank_api import app
import os

# Check if the application is running in a testing environment
if os.getenv('FLASK_ENV') == 'testing':
    app.config.from_object('config.TestConfig')
else:
    app.config.from_object('config.LocalConfig')

if __name__ == '__main__':
    app.run(debug=True)
