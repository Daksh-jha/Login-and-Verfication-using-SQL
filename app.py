from email import message
from string import digits
from flask import *
import sqlite3
from random import choices
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)


def add_user(name, email, password):
    conn = sqlite3.connect("user.sqlite3")
    cursor = conn.cursor()

    cursor.execute(
        """
            create table if not exists user_database
             (id integer primary key autoincrement,
             name varchar(30),
             email varchar(30),
             password varchar(30))
            """
    )

    cursor.execute(
        """
                insert into user_database
                 (name,email,password)
                 values(?,?,?)

            """, [name, email, password]
    )

    conn.commit()
    conn.close()


def get_username(email, password):
    conn = sqlite3.connect("user.sqlite3")
    cursor = conn.cursor()
    list = cursor.execute(
        """
                 select name from user_database
                 where email==? and password==?                
                """, [email, password]
    ).fetchall()
    conn.commit()
    conn.close()

    return list[0][0]


def check_user(email, password):
    conn = sqlite3.connect("user.sqlite3")
    cursor = conn.cursor()
    list = cursor.execute(
        """
            select * from user_database
            where email==? and password==?


            """, [email, password]
    ).fetchall()
    conn.commit()
    conn.close()
    if list == []:
        return False
    else:
        return True


def generate_otp(k=5):
    return "".join(choices(digits, k=k))


otp = generate_otp()


def send_otp(email):
    from_ = '{Email}'
    to = email
    msg = MIMEMultipart()
    msg['From'] = from_
    msg['To'] = email
    msg['Subject'] = 'New Mail Generated'
    pwd = '{App Generated Password}'
    text = f'''
         This is your One Time Password {otp}
    '''
    text_mime = MIMEText(text, 'plain')
    msg.attach(text_mime)
    print("[+] Connecting to server...")
    conn = smtplib.SMTP("smtp.gmail.com", 587)
    print("[+] Making Connection Secure...")
    conn.starttls()
    print("[+] Logging to the Server...")
    conn.login(from_, pwd)
    print("[+] Send mail...")
    conn.sendmail(from_, to, msg.as_string())
    print('[+] Closing the Connection...')
    conn.close()


def email_check(email):
    conn = sqlite3.connect("user.sqlite3")
    cursor = conn.cursor()
    em = cursor.execute(
        """ 
        select * from user_database
            where email=?
        """, [email]
    ).fetchall()
    conn.commit()
    conn.close()
    if em == []:
        return False
    else:
        return True


admin_code = "python1admin@flask"


@app.route("/")
def home_page():
    return render_template("index.html", data=None)


@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        email = request.form.get("email")
        t_pass = request.form.get("secret")
        if check_user(email, t_pass):
            name = get_username(email, t_pass)

            return render_template("index.html", data=name)
        elif email == "" or t_pass == "":
            message = ["fields are empty"]
            return render_template("signin.html", data=message)
        elif email == "admin@123" and t_pass == admin_code:
            return redirect(url_for("admin_page"))
        else:
            message = ["email and password don't match"]
            return render_template("signin.html", data=message)
    return render_template("signin.html")


@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        pass_n = request.form.get("secret")
        c_pass = request.form.get("c_secret")
        email = request.form.get("email")
        if pass_n != c_pass:
            message = ["password dont match"]
            return render_template("signup.html", data=message)
        elif username == "" or pass_n == "" or c_pass == "" or email == "":
            message = ["fields are empty"]
            return render_template("signup.html", data=message)
        elif email_check(email):
            message = ["email already registred"]
            return render_template("signup.html", data=message)
        else:
            add_user(username, email, pass_n)
            send_otp(email)
            return redirect(url_for("otp_verification"))
        # else:
        #     return redirect(url_for("sign_up"))
    return render_template("signup.html")


@app.route("/otp-verification", methods=["GET", "POST"])
def otp_verification():
    if request.method == "POST":
        c_otp = request.form.get("otp")
        if c_otp != otp:
            return redirect(url_for("otp_verification"))

        return redirect(url_for("home_page"))
    return render_template("otp.html")


@app.route("/admin")
def admin_page():
    conn = sqlite3.connect("user.sqlite3")
    cursor = conn.cursor()
    list = cursor.execute(
        """ 
            select * from user_database
            """
    ).fetchall()
    conn.commit()
    conn.close()
    return render_template("admin.html", data=list)


app.run(debug=True)
