import cv2
import numpy as np
import matplotlib.pyplot as plt
import types

def messageToBinary (message) :
    if type(message) == str :
        return "".join([format(ord(i),"08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray :
        return [format(i,"08b") for i in message]    
    elif type(message) == int or type(message) == np.uint8 :
        return format(message,"08b")
    else :
        return TypeError("INPUT MESSAGE NOT SUPPORTED")

def hideData (image,secret_massage) :
    n_bytes = image.shape[0] * image.shape[1] * image.shape[2] / 8 
    print("Maximum num of byets :",n_bytes)
    
    if len(secret_massage) > n_bytes:
        raise ValueError("ERROR ENCOUNTERED INSUFFICIENT BYTES,NEED BIGGER IMAGE")

    secret_massage += "#"*5
    
    data_index = 0
    
    binary_secret_message = messageToBinary(secret_massage)
    data_len = len(binary_secret_message)
    
    for channel in image:
        for pixel in channel:
            r,g,b = messageToBinary(pixel)
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_secret_message[data_index], 2)
                data_index +=1

            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_secret_message[data_index], 2)
                data_index +=1                
    
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_secret_message[data_index], 2)
                data_index +=1
                
            if data_index >= data_len:
                break
    return image       
    
def showData(image):

  binary_data = ""
  for values in image:
      for pixel in values:
          r, g, b = messageToBinary(pixel) 
          binary_data += r[-1]
          binary_data += g[-1] 
          binary_data += b[-1] 

  all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]

  decoded_data = ""
  for byte in all_bytes:
      decoded_data += chr(int(byte, 2))
      if decoded_data[-5:] == "#"*5: 
          break
  #print(decoded_data)
  return decoded_data[:-5] 
    
def encodeText() :
    image_name = input('ENTER IMAGE NAME WITH ITS EXTENTION : ')
    image = cv2.imread(image_name)
    
    print('SHAPE OF IMAGE IS ',image.shape)
    max_LENGTH =image.shape[0] * image.shape[1] * 3 // 8 
    # print('MAX LENGTH OF ENCODED TEXT IS ',max_LENGTH )
    
    resized_image = cv2.resize(image,(500,500))
    
    print('ORIGINAL IMAGE')
    plt.imshow(cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB))
    plt.show()
    
    data = input("ENTER TEXT TO BE INCODED :")
    if len(data) == 0 :
        raise ValueError('DATA IS EMPTY')
        
    image_name = input('ENTER NEW IMAGE NAME WITH ITS EXTENTION : ')
    encoded_image = hideData(image,data)
    cv2.imwrite(image_name,encoded_image)              
          
def decodeText() :
    
    image_name = input('ENTER NAME OF THE STEGANOGAPHED IMAGE WITH PNG EXTENTION : ')
    image = cv2.imread(image_name)
    
    print('STEGANOGAPHED IMAGE') 
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.show()
    
    try :
            text = showData(image)
    except Exception as e:
       print("An exception occurred: ", e) 
       
    return text    
       
def stegmography() :
   for i in range (10) :
    a = input('IMAGE STEGMOGRAPHY \n1- ENCODE DATA \n2- DECODE DATA \n3- BREAK\nMY CHOICE IS : ')
    userinput = int(a)
    if userinput == 1 :
        print('\nENCODING....')
        encodeText()
    
        
    elif userinput == 2 :
        print('\nENCODING....')
        print('DECODED MESSAGE IS : \n' + decodeText())
    elif userinput == 3 :
       print('BREAK .. THANK YOU')
       break
    else :
        raise ValueError("ENTER CORRECT INPUT")
                
stegmography()    