#import numpy as np
#import json
#import cv2
from flask import Flask, request, render_template, redirect, jsonify
# import io
# import base64
#from imageio import imread
# import face_recognition




app = Flask(__name__)

@app.route('/api')
def index():
    msg={}
    #?task= upload or find &&
    # step-1
    # token = request.args['token']
    # task=request.args['task']
    #rading base64 in the form of string
    # image_b64_string=str(request.args['image'])
    # image_b64_string='/9j/4AAQSkZJRgABAQAAAQABAAD/4QAqRXhpZgAASUkqAAgAAAABADEBAgAHAAAAGgAAAAAAAABHb29nbGUAAP/bAIQAAwICCQkJCAoJCQgKCgoICQgJCQgJBwkJCQkJBgcGBgYGBgYHBwgIBQgIBwcHCgcHBwgJCQkHBwsNCggNBwgJCAEDBAQGBQYKBgYKCAcKCw4ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgI/8AAEQgBcQE4AwERAAIRAQMRAf/EAB0AAAAHAQEBAAAAAAAAAAAAAAECAwQFBgcACAn/xABPEAABAgMEBgYHBQUGBAUFAQABAhEAAyEEBRIxBgdBUWHwEyJxgZGhCDJCUrHB0SNicuHxFDM0c6IJFSRDgrI1Y3TCJVOSs9IWtMPi8qP/xAAcAQABBQEBAQAAAAAAAAAAAAAAAQIDBAUGBwj/xABIEQACAQMCAwQGBgcHAgUFAAAAAQIDBBEFEiExQQYTIlEyQlJhcbIjYnKBosIUMzQ1gpGSJKGxwdHS8BVDJeHi8fJERWODw//aAAwDAQACEQMRAD8A9WyVc/PZGsimxwkPz3w4bgOowjHh0c+ENA5H5QAKAcIABaAA7QC4DIBgEBSIABCefhAAdXygACTKbn4QAKtAAJMAHQDog8/SkAjQL5QCAvAAEAHK5+r8IAOUYABBgAOT4cuTAAXDlDWsgATCYYq4BkjODDEZyB4c5Q0XDBxZeEAi5hlJ5/KHJ4HNHYIVtCgYRCJ4AUQgctCtgCkDloYAZA7Ic3kRI7BCp8BGgVEbc/jDUshgRKRD+g5Evc6WfnhFSXMRoz1Cagjf8mi6iLIuD8M/lC8hy4ij8n5QmRyRwMIIwUZQr4DW8CnO3nFCDkGIPPz+9AAoRAOTOxQCMUSrsgEDc/SAAUc/nT1YADGAAQqvPjAAYnn6wAcrugFTwGJgBsKTAICDxgAB+flAAYAc/HthG8ACBlzshUAKR2b/AIw'
    #decoding the string to image which gives result as gray scale image
    # image_grayScale= imread(io.BytesIO(base64.b64decode(image_b64_string)))

    #converting the gray scale image to colored image
    # cv2_img = cv2.cvtColor(image_grayScale, cv2.COLOR_RGB2BGR)

    #resizing the image
    # image = cv2.resize(cv2_img, (300, 500))

    # Face encoding
    # result,encode_image=face_encoding(image)

    #testing till face_encoding
    msg['msg']='face_encoding'
    # msg['token']=token
    # msg['task']=task
    # msg['encode']=str(encode_image)
    return jsonify(msg)

    # if(result!=True):
    #     if(task=='upload'):
    #         upload_result=upload_details(token,encode_image)
    #         if(upload_result==True):
    #             msg['msg']="Image uploaded Succcessfully..!"
    #         else:
    #             msg['msg']="Network Inconvenience, Please Try again..!"
    #     elif(task=='find'):
    #         status,key=find(encode_image)
    #         if (status != False and key != False):
    #             msg['token']=key
    #
    # else:
    #     msg['msg']=result

    # return jsonify(msg)


# @app.route('/Face_Encoding')
# def face_encoding(image):
#         # read the image
#         img = image
#         faceLoc = face_recognition.face_locations(img)
#
#         # checking if there are multiple faces
#         if (len(faceLoc) == 1):#if the image consists of single face
#             encode_img=face_recognition.face_encodings(img)
#             return True,encode_img
#         else:
#             return False,"Image consists of multiple faces...!"


# @app.route('/Upload')
# def upload_details(token,encode_img):
#
#     # save the encoding to json
#     json_file = open("json.json",)
#     json_decoded = json.load(json_file)
#
#     # check if the image already exists, if not exists then store the encoding
#     status,key= find(encode_img)
#
#     if (status != False and key != False):
#         return False
#
#     # storing the encoded value
#     json_decoded[token] = str(encode_img)
#     json.dump(json_decoded, open("json.json", 'w'))
#
#     return True


# @app.route('/Find')
# def find(encode_img):
#     json_file=open("json.json")
#     json_decoded=json.load(json_file)
#
#     for k, v in dict(json_decoded).items():
#         a = np.array(list(map(float, v[1:-1].split())))
#         # print(encode_img)
#         # print(a)
#         if(face_recognition.compare_faces([a], encode_img)[0]):
#             return True,k
#
#     return False,False


if __name__ == '__main__':
    app.run(debug=True)
