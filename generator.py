from PIL import Image 
import os
import json
import cv2

# Download BanglaWriting Dataset and place unzipped 'raw' folder in the current path.

file_arr = os.listdir('raw/.')
# print(file_arr[101%2])
# counter = 0
failed_to_save = 0

for file_number in range(len(file_arr)):
    if file_number%2 == 0:
        print(file_arr[file_number])
        # counter += 1

        img_name = file_arr[file_number]
        img_json = file_arr[file_number+1]

        with open("raw/" + img_json, "r", encoding="utf-8") as read_it: 
            data = json.load(read_it) 

        # printing all labels (bangla words) from data.json
        # for item in range(len(data['shapes'])):
        #     print(    data['shapes'][item]['label'] )

        # printing all labels (bangla words) from data.json
        # for item in range(len(data['shapes'])):
        #     print(    data['shapes'][item]['points'] )

        try:
            for item in range(len(data['shapes'])):
                word_number = item

                x = data['shapes'][word_number]['points'][0][0]
                x1 = data['shapes'][word_number]['points'][1][0]
                y = data['shapes'][word_number]['points'][0][1]
                y1 = data['shapes'][word_number]['points'][1][1]

                # print(x, x1, y, y1)
                # print(    data['shapes'][word_number]['label'] )
                img_label = data['shapes'][word_number]['label']

                
                
                # Opens a image in RGB mode 
                im = Image.open("raw/" + img_name) 

                # croped image 
                im1 = im.crop((x, y, x1, y1)) 
                
                # Shows the image in image viewer 
                # im1.show() 
                # im1.save("img\\" + img_label + ".jpg")

                # Using OTSU Threshold to convert the images to BNW and remove noise
                temp = "temp.jpg"
                im1.save(temp)
                img = cv2.imread(temp, 0)
                ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                im1 = Image.fromarray(imgf)

		
                try:
                    im1.save("img\\" + img_label + " " + str(word_number) + "__" + file_arr[file_number])
                    # "img" folder should be created beforehand on the current path. Will add code to create file dynamically if not exists.
                except:
                    if img_label == '*':
                        im1.save("img\\" + "--- " + str(word_number) + "__" + file_arr[file_number])
                    elif img_label.find('*') != -1:
                        im1.save("img\\" + "----- " + str(word_number) + "__" + file_arr[file_number])
                    else:
                        # print(word_number, img_label)
                        failed_to_save += 1
                        pass
        except:
            pass
	    # maybe corrupted image, handle this
        else:
            pass

print(failed_to_save)