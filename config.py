import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    # DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    ARTICLES_PER_PAGE = 10
    COMMENTS_PER_PAGE = 8
    SECRET_KEY = 'secret_key_to_protect_from_csrf'
    
    # for csrf protection
    WTF_CSRF_SECRET_KEY = 'random_key_for_form' 

    # Take good care of 'SECRET_KEY' and 'WTF_CSRF_SECRET_KEY', 
    # if you use the bootstrap extension to create a form, 
    # it is Ok to use 'SECRET_KEY',
    # but when you use tha style like '{{ form.name.labey }}:{{ form.name() }}',
    # you must do this for yourself to use the wtf, more about this, you can
    # take a reference to the book <<Flask Framework Cookbook>>.

    @staticmethod
    def init_app(app):
        pass
