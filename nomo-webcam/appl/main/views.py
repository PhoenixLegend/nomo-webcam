#主蓝本中定义的应用路由
from datetime import datetime
from flask import render_template,session,redirect,url_for,request,make_response,jsonify
from . import main
import os
from  PIL import Image
import math
import cv2
from werkzeug.utils import secure_filename


    
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def cut_img(img, x, y):
    """
    函数功能：进行图片裁剪（从中心点出发）
    :param img: 要裁剪的图片
    :param x: 需要裁剪的宽度
    :param y: 需要裁剪的高
    :return: 返回裁剪后的图片
    """
    x_center = img.size[0] / 2
    y_center = img.size[1] / 2
    new_x1 = x_center - x//2
    new_y1 = y_center - y//2
    new_x2 = x_center + x//2
    new_y2 = y_center + y//2
    new_img = img.crop((new_x1, new_y1, new_x2, new_y2))
    return new_img

def double_exposure():
    basepath = os.path.dirname(__file__)  # 当前文件所在路径
    rootpath = basepath[:basepath.find("back_code\\")+len("back_code\\")]
    directory_name =  "image\origin_images"
    #directory_name = "f:\\学习\\研究生\\课程设计\\APP\\back_code\\image\\origin_images"
    arr_of_img = []
    for filename in os.listdir(directory_name):
        img = cv2.imread(directory_name + "/" + filename)
        arr_of_img.append(img)
        #print(img)
        
    
    img1 = Image.fromarray(arr_of_img[0])
    img2 = Image.fromarray(arr_of_img[1])
    new_x = min(img1.size, img2.size)[0]  
    new_y = min(img1.size, img2.size)[1]
    new_img1 = cut_img(img1, new_x, new_y)
    new_img2 = cut_img(img2, new_x, new_y)
    fixed_img = Image.blend(new_img1, new_img2, (math.sqrt(5)-1)/2)
    for filename in os.listdir(directory_name):
        os.remove(directory_name + "/" + filename)
    return fixed_img


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@main.route('/gallery',methods=['GET','POST'])
def gallery():
    if request.method == 'POST':
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        rootpath = basepath[:basepath.find("back_code\\")+len("back_code\\")]
        for file in request.files.getlist('file'): # 这里改动以存储多份文件
             if file and allowed_file(file.filename):
                 filename = secure_filename(file.filename)
                 upload_path = os.path.join(rootpath, 'image/origin_images/',filename)
                 file.save(upload_path)
    return render_template("gallery.html")

@main.route('/show_2', methods=['POST', 'GET'])
def show_double():
    basepath = os.path.dirname(__file__)  # 当前文件所在路径
    rootpath = basepath[:basepath.find("back_code\\")+len("back_code\\")]
    img = double_exposure()
    img.save(rootpath + "image/fixed_images/3.jpg")
    image_data = open(rootpath+"image/fixed_images/3.jpg", "rb").read()
    response = make_response(image_data)
    response.headers['Content-Type'] = 'image/png'
    return response