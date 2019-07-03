#VIVEKS DONT TOUCH
##IGNORE

def localize_objects(path):
        from PIL import Image
        from PIL import ImageFont
        from PIL import ImageDraw
        font = ImageFont.truetype("Aaargh.ttf", 30)

        img = Image.open(path)
        draw = ImageDraw.Draw(img)
        master_list = []

        
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()

        with open(path, 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content=content)

        objects = client.object_localization(image=image).localized_object_annotations

        #print('Number of objects found: {}'.format(len(objects)))
        for object_ in objects:
            object_list = []
            object_list.append(object_.name) # Adding object name in the list
            object_list.append(object_.score) # Adding confidence in the list
            vertices = [] # List to store all the vertices

            for vertex in object_.bounding_poly.normalized_vertices:
                vertices.append(vertex.x)
                vertices.append(vertex.y)

            #print(vertices)

            object_list.append(vertices) # Adding the list of vertices to the object list

            master_list.append(object_list) # Adding the object data into the master list
            k=0
            for i in master_list:
                flag=0
                draw.rectangle((i[2][0]*640,i[2][1]*480,i[2][4]*640,i[2][5]*480), outline='red')
                k=k+1
                length=0
                for j in range(0,k-1):
                    if i[2][0]==master_list[j][2][0]:
                        flag=1
                        length=len(i[0])

                if(flag==0):
                    draw.text(((i[2][0]*640),(i[2][1]*480)-30),i[0],(0,255,0),font=font)

                else:
                    draw.text((i[2][0]*640,(i[2][1]*480)+5),i[0],(0,255,0),font=font)

            img.save('./static/img/sample-out.jpg')
            return master_list





