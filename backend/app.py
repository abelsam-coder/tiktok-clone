from flask import Flask,redirect,url_for,render_template,request,session
from config import Config
from extensions import db,create_api,bcrypt
from flask_migrate import Migrate
from flask_socketio import SocketIO,emit
from routes.routes import routes
from models import Followers

app=Flask(__name__,template_folder="../frontend",static_folder='../upload', static_url_path='/upload')
app.config.from_object(Config)
db.init_app(app)
Migrate(app,db)
api = create_api(app)
bcrypt.init_app(app)

routes(api)

sock = SocketIO(app)

from flask_socketio import emit
from flask import session

@sock.on('follow')
def follow(data):
    username = session.get('username')  # logged in user
    follow_user = data.get('follow')    # user to follow
    print()
    if not username:
        emit('error', {'message': 'Not authenticated'})
        return

    get = Followers.query.filter_by(
        username=follow_user,
        follower=username
    ).first()

    if get:
        # Unfollow
        db.session.delete(get)
        db.session.commit()

        emit('follow_status', {
            'status': 'unfollowed',
            'user': follow_user
        })
    else:
        # Follow
        insert = Followers(
            username=follow_user,
            follower=username
        )
        db.session.add(insert)
        db.session.commit()

        emit('follow_status', {
            'status': 'followed',
            'user': follow_user
        })


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404





import models

if __name__ == '__main__':
       
       app.run(port=5000,debug=True)
