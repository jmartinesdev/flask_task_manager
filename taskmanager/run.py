import os
from taskmanager import app

if __name__ == "__main__":
    app.run(
        host=os.eviron.get("IP")
        port=os.eviron.get("PORT")
        debug=os.eviron.get("DEBUG")
    )