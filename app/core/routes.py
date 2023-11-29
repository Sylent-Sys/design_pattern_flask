from app.controller.dashboard import Dashboard
class Routes:
    dashboardIndex = {
        "name":'/',
        "methods": ['GET', 'POST'],
        "fun": Dashboard.index
    }