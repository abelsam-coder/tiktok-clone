from flask_restful import Resource
from flask import request,render_template,make_response,session,redirect,flash
from models import User,Posts,Profile
from extensions import bcrypt,db
from sqlalchemy.exc import IntegrityError
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER='../upload/files'

class Upload(Resource):
       def post(self):
              username = session.get('username')
              if not username:
                     return redirect('/login')
              title = request.form['title']
              caption = request.form['caption']
              a = os.listdir(UPLOAD_FOLDER)
              file = request.files['file']
              filep = secure_filename(file.filename)
              join = os.path.join(UPLOAD_FOLDER,filep)
              file.save(join)
              path = f"/upload/files/{filep}"
              insert = Posts(username=username,title=title,caption=caption,post=path)
              db.session.add(insert)
              db.session.commit()
              flash('uploaded successfully')
              return redirect('/dashboard/upload') 
       def get(self):
              username = session.get('username')
              if not username:
                     return redirect('/login')
              html = render_template('post.html')
              return make_response(html, 200)


class Uploaded_data(Resource):
       def get(self):
              username = session.get('username')
              if not username:
                     return redirect('/login')
              get_email = User.query.filter_by(username=username).first()
              get_profile = Profile.query.filter_by(username=username).first()
              if get_profile:
                     posts = Posts.query.filter(Posts.username != username).all()
                     post_data = []
                     for post in posts:
                            user = post.username
                            if not user:
                                   continue
                            
                            # Assuming `post.user` exists and `Profile` is linked to User
                            profile_obj = Profile.query.filter_by(username=post.username).first()
                       
                            profile_img = profile_obj.profile if profile_obj else '/upload/profile/user1.png'
                            email = User.query.filter_by(username=username).first()
                            post_data.append({
                            'id': post.id,
                            'title': post.title,
                            'caption': post.caption,
                            'post_img': post.post,
                            'username': user,
                            'email': email.email,
                            'profile': profile_img
                            })


                     
                     html = render_template('main.html',posts=post_data,username=username,email=get_email.email,profile=get_profile.profile)
                     return make_response(html, 200)
              else:
                     posts = Posts.query.filter(Posts.username != username).all()
                     post_data = []
                     for post in posts:
                            user = post.username
                            if not user:
                                   continue
                            print(user)
                            # Assuming `post.user` exists and `Profile` is linked to User
                            profile_obj = Profile.query.filter_by(username=post.username).first()
                            
                            profile_img = profile_obj.profile if profile_obj else '/upload/profile/user1.png'
                            email = User.query.filter_by(username=user).first()
                                 
                           
                            post_data.append({
                            'id': post.id,
                            'title': post.title,
                            'caption': post.caption,
                            'post_img': post.post,
                            'username': post.username,
                            'email': email.email or '',
                            'profile': profile_img
                            })
                     let = Posts.query.all()
                     html = render_template('main.html',posts=post_data,username=username,email=get_email.email,profile='/upload/profile/user1.png')
                     return make_response(html, 200) 
              
              html = render_template('main.html')
              return make_response(html, 200)

class Search(Resource):
       def get(self):       
              username = session.get('username')
              search = request.args.get('search')  # GET parameter for search

              if not username:
                     return redirect('/login')

              # Get current user's email and profile
              get_email = User.query.filter_by(username=username).first()
              get_profile = Profile.query.filter_by(username=username).first()

              # Base query: all posts except current user's
              posts_query = Posts.query.filter(Posts.username != username)

              # Apply search filter if search term exists
              if search:
                     search_term = f"%{search}%"
                     posts_query = posts_query.filter(
                            (Posts.title.ilike(search_term)) |
                            (Posts.caption.ilike(search_term)) |
                            (Posts.username.ilike(search_term))
                     )

              posts = posts_query.all()
              post_data = []

              for post in posts:
                     user_username = post.username
                     if not user_username:
                            continue

                     # Get profile of the post's user
                     profile_obj = Profile.query.filter_by(username=user_username).first()
                     profile_img = profile_obj.profile if profile_obj else '/upload/profile/user1.png'

                     # Get email of the post's user
                     user_obj = User.query.filter_by(username=user_username).first()
                     email = user_obj.email if user_obj else ''

                     post_data.append({
                            'id': post.id,
                            'title': post.title,
                            'caption': post.caption,
                            'post_img': post.post,
                            'username': user_username,
                            'email': email,
                            'profile': profile_img
                     })

              # Render template with posts
              html = render_template(
              'main.html',
              posts=post_data,
              username=username,
              email=get_email.email if get_email else '',
              profile=get_profile.profile if get_profile else '/upload/profile/user1.png'
              )
              return make_response(html, 200)

                            