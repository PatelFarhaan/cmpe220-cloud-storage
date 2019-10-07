import sys
sys.path.append('../../')


from project import db
from project.users.models import Users
from werkzeug.security import generate_password_hash



admin_obj = Users(email='patel.***REMOVED_EMAIL***',
                  hashed_password=generate_password_hash('***REMOVED_PASSWORD***'),
                  mobile_number='9962048121',
                  is_admin=True
                  )
db.session.add(admin_obj)
db.session.commit()
print("Admin Created Successfully!!!")