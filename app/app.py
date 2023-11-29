from flask import Flask, request
from app.core.routes import Routes

def create_app():
    app = Flask(__name__)
    @app.route(Routes.dashboardIndex['name'], methods=Routes.dashboardIndex['methods'])
    def dashboard_index():
        """
        This function returns the result of calling the 'dashboardIndex' function from the 'Routes' dictionary with the 'request' parameter.

        Returns:
            The result of calling the 'dashboardIndex' function.
        """
        return Routes.dashboardIndex['fun'](request)
    app.run(debug=True)