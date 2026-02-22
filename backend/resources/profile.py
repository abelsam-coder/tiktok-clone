from flask_restful import Resource
from flask import session,redirect,make_response,render_template,request
from models import Followers,Posts,Profile,User
from werkzeug.utils import secure_filename
import os
from extensions import db

class Profile_info(Resource):
       def get(self):
              username = session.get('username')
              if not username:
                     return redirect('/')
              
              email = User.query.filter_by(username=username).first()
              get_info = Followers.query.filter_by(username=username).count()
              profile_obj = Profile.query.filter_by(username=username).first()
              profile_img = profile_obj.profile if profile_obj else '/upload/profile/user1.png'
              get_following = Followers.query.filter_by(follower=username).count()
              posts = Posts.query.filter_by(username=username).all()
              bio_a = Profile.query.filter_by(username=username).first()
              bio = bio_a.bio if bio_a else 'none'
              post = Posts.query.filter_by(username=username).count()
              response = render_template('profile.html',posts=posts,followers=get_info,following=get_following,post=post,username=username,email=email.email,profile=profile_img,bio=bio)
                     
              
              return make_response(response)
       
class Profile_edit(Resource):
       def post(self):
              username = session.get('username')
              if not username:
                     return redirect('/')
              bio = request.form['bio']
              profile = request.files['file']
              insert = Profile.query.filter_by(username=username).first()
              
              if insert:
                     insert.bio = bio
                     UPLOAD_FILE = '../upload/profile'
                     filep = secure_filename(profile.filename)
                     pat = os.path.join(UPLOAD_FILE,filep)
                     profile.save(pat)
                     insert.profile = f'/upload/profile/{filep}'
                     insert.save()
              else:
                     UPLOAD_FILE = '../upload/profile'
                     filep = secure_filename(profile.filename)
                     pat = os.path.join(UPLOAD_FILE,filep)
                     profile.save(pat)
                     lo = f'/upload/profile/{filep}'
                     insert = Profile(bio=bio,profile=lo,username=username)
                     db.session.add(insert)
                     db.session.commit()
              return redirect('/dashboard/profile')       
       def get(self):
              username = session.get('username')
              if not username:
                     return redirect('/')
              insert = Profile.query.filter_by(username=username).first()
              if insert:
                     let = render_template('edit.html',bio=insert.bio,profile=insert.profile)
                     return make_response(let)
              else:
                     let = render_template('edit.html',bio='none',profile='/upload/profile/user1.png')
                     return make_response(let)
              




              
              