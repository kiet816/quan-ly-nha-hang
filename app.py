# app.py - Đã sửa lỗi văng session (chỉ thêm 1 tham số)

from flask import Flask, render_template
from datetime import timedelta

from blueprints.login import login_bp
from blueprints.register import register_bp
from blueprints.admin import admin_bp
from blueprints.nhanvien import nhanvien_bp
from blueprints.menu import menu_bp
from blueprints.pos import pos_bp
from blueprints.addtable import addtable_bp
from blueprints.kitchen import kitchen_bp
from blueprints.customer import customer_bp
from extensions import db

app = Flask(__name__)
app.secret_key = "super_secret_key_nha_hang_2025"
app.permanent_session_lifetime = timedelta(hours=1)

# ĐĂNG KÝ BLUEPRINT
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(nhanvien_bp)
app.register_blueprint(menu_bp)
app.register_blueprint(pos_bp)
app.register_blueprint(addtable_bp)
app.register_blueprint(kitchen_bp)
app.register_blueprint(customer_bp, url_prefix="/")

@app.route("/")
def home():
    return render_template("login.html")

if __name__ == "__main__":
    # ĐÃ SỬA: Thêm use_reloader=False để tắt tự động restart server
    # Đây chính là nguyên nhân gây mất session đột ngột dù bạn đang thao tác liên tục
    app.run(debug=True, use_reloader=False, port=5000)