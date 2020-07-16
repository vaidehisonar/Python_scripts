import pandas as pd
import os
import requests # to get image from the web
import shutil # to save it locally


df = pd.read_csv("phone_dataset.csv",encoding= 'unicode_escape') #you could add index_col=0 if there's an index
#print(df.shape)
#print(df)
url_List=[]
test_url=[]
names=[]
new_df = df.dropna()
url_List.append(new_df['Product_img'])
names.append(new_df['Product_name'])
#print(url_List)
test_url = url_List[0]
#print(test_url)
img_names = names[0]
#print(img_names)

for each_url,f_name in zip(test_url,img_names):
    #if len(f_name)>50:
    name = f_name.split('(' or "\|" or '\\' or '\*' or '\/')[0]
    #print(name)
    filename = name+'{}'.format(".jpg")
    #print(filename)
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(each_url, stream = True)

# Check if the image was retrieved successfully
    if r.status_code == 200:    
    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        dest = os.path.join("E:\self exercises\Mobile Phones", filename)
    # Open a local file with wb ( write binary ) permission.
        if not os.path.isfile(dest):
            try:
                with open(dest,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
            except:
                print("dest",dest)
        
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Image Couldn\'t be retreived')




