from resources import user
from resources import upload,home,profile


def routes(api):
       api.add_resource(user.Users_register,'/register')
       api.add_resource(user.Users_login,'/login')
       api.add_resource(upload.Upload,'/dashboard/upload')
       api.add_resource(home.home,'/')
       api.add_resource(upload.Uploaded_data,'/dashboard/home')
       api.add_resource(upload.Search,'/search')
       api.add_resource(user.Get_user,'/user/<search>')
       api.add_resource(user.Logout,'/dashboard/logout')
       api.add_resource(profile.Profile_edit,'/dashboard/profile/edit')
       api.add_resource(profile.Profile_info,'/dashboard/profile')