from flask import Request, render_template


class Dashboard:
    @staticmethod
    def index(request: Request):
        if request.method == 'POST':
            return {
                'msg': 'Hello World!'
            }
        return render_template('dashboard/index.html', user={
            'username': 'John Doe'
        })