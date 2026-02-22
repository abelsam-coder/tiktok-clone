from flask_restful import Resource
from flask import request,render_template,make_response,flash,redirect,session
from models import User,Profile,Posts,Followers
from extensions import bcrypt,db
from sqlalchemy.exc import IntegrityError
import os
from werkzeug.utils import secure_filename



class Users_register(Resource):
       
       def post(self):
              get_username = session.get('username')
              if get_username:
                     return redirect('/dashboard/home')
              username = request.form['username']
              email = request.form['email']
              password = request.form['password']
              try:
                     hashed_password = bcrypt.generate_password_hash(password).decode()
                     user = User(username=username,email=email,password=hashed_password)
                     db.session.add(user)
                     db.session.commit()
                     response = {
                            'status':'success'
                     }

                     session['username'] = username
                     flash(f'Welcome user {username}','success')
                     return redirect('/dashboard/home')
              except IntegrityError:
                     flash('please use another username','error')
                     return redirect('/register')  
             
       def get(self):
              html = render_template('register.html')
              return make_response(html, 200)
       
class Users_login(Resource):
       def post(self):
              get_username = session.get('username')
              if get_username:
                     return redirect('/dashboard/home')
              username = request.form['username']
              password = request.form['password']
              try:
                     user = User.query.filter(User.username==username).first()
                     if user:
                            if bcrypt.check_password_hash(user.password,password):
                                   session['username'] = username
                                   flash('Welcome back user {username}')
                                   return redirect('/dashboard/home')
                            else:
                                   flash('Incorrect Password','error')
                                   return redirect('/login')
                     else:
                            flash('No username found','error')
                            return redirect('/login')  
                         
              except Exception as e:
                     return str(e) 
       def get(self):
              html = render_template('login.html')
              return make_response(html, 200)  
       
class Get_user(Resource):
       def get(self,search):
              username = session.get('username')
              search = search 
             

              if not username:
                     return redirect('/login')

              # Get current logged-in user's email and profile
              current_user = User.query.filter_by(username=username).first()
              current_profile = Profile.query.filter_by(username=username).first()

              # Initialize variables
              searched_user_data = None
              searched_posts = []

              if search:
              # Find the searched user
                     searched_user = User.query.filter_by(username=search).first()
                     if searched_user:
                            # Get their profile
                            profile_obj = Profile.query.filter_by(username=searched_user.username).first()
                            profile_img = profile_obj.profile if profile_obj else '/upload/profile/user1.png'
                           
                            searched_user_data = {
                            'username': searched_user.username,
                            'email': searched_user.email,
                            'profile': profile_img
                            }
                            is_followed = Followers.query.filter_by(username=search,follower=username).first()
                            followed = 'unfollow' if is_followed else 'follow'
                            # Optionally, get posts by this searched user
                            searched_posts_objs = Posts.query.filter_by(username=searched_user.username).all()
                            get_following = Followers.query.filter_by(follower=search).count()
                            get_info = Followers.query.filter_by(username=search).count()
                            postt = Posts.query.filter_by(username=search).count()
                            for post in searched_posts_objs:
                                   searched_posts.append({
                                   'id': post.id,
                                   'title': post.title,
                                   'caption': post.caption,
                                   'post_img': post.post,
                                   'username': post.username,
                                   'profile': profile_img,
                                   'email': searched_user.email,
                                 
                            })
                           

              # Render template with searched user and posts
              html = render_template(
              'userprofile.html',
              username=username,
              email=current_user.email if current_user else '',
              profile=current_profile.profile if current_profile else '/upload/profile/user1.png',
              searched_user=searched_user_data,
              followers=get_info,
              following=get_following,
              posts=postt,
              follow=followed,
              user_post=searched_posts
              )
              return make_response(html, 200)
                            

class Logout(Resource):
       def get(self):
              session.pop('username')
              return redirect('/')
