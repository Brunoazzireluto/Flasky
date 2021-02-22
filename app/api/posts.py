from flask import jsonify, request, g, url_for, current_app

@api.route('/posts/')
@auth.login_required
def get_posts():
    pass