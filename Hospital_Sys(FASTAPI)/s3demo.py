import boto3

# Creating an S3 access object
obj = boto3.client("s3")
# Uploading a png file to S3 in 
# 'mygfgbucket' from local folder
obj.upload_file(
    Filename=r"C:\Users\Thinkbiz\OneDrive - VeBuIn\Desktop\Hospital_Sys\uploads\demo.jpg",
    Bucket="vb-python-intern-s3demo",
    Key="Devansh/firstgfgbucket.png"
)