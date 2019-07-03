from flask import Flask, redirect, url_for, render_template,request
import os
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/')
def index():
    return render_template('index3.html')

@app.route('/index2', methods= ['POST','GET'])
def index2():


        import cv2

        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
                ret, frame = cam.read()
                cv2.imshow("test", frame)
                if not ret:
                        break
                k = cv2.waitKey(1)

                if k%256 == 27:
                        # ESC pressed
                        print("Escape hit, closing...")
                        break
                elif k%256 == 32:
                        # SPACE pressed
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        cv2.imwrite(img_name, frame)
                        print("{} written!".format(img_name))
                        img_counter += 1

        cam.release()

        cv2.destroyAllWindows()

        ## Main function
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\\Users\\Jeswin\\flasksite\\Hackhathon-65c2f11b3bbe.json"
        import google_vision_tag_getter as gvt
        import wikipedia_and_summarize as wiki 
        import test_wiki as info

        path="C:/Users/Jeswin/flasksite/opencv_frame_0.png"

        #master_list = []
        master_list = gvt.localize_objects(path)

        wiki_info = []
        '''
        for obj in master_list:
                wiki_info.append(wiki.wiki_ripoff(obj[0]))
        '''
        for obj in master_list:
                wiki_info.append(info.get_info(obj[0]))
        
        print(master_list)
        print(wiki_info)

        full_filename = os.path.join(app.config[''], 'opencv_frame_0.png')
        return render_template("index2.html", user_image = full_filename)

   
if __name__ == "__main__":
    app.run(host='0.0.0.0')

