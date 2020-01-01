# secret key, sql, mail_username, mail_password lebih baik dimasukkan kedalam env. Cek video
class Config:
    SECRET_KEY = '31d71669beb9d0a7a8bbb34cca079d8c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'ngobar.ci.login@gmail.com'
    MAIL_PASSWORD = 'ngobarcilogin'
