class FileTypeError(Exception):
    def __init__(self, err="仅支持 jpg/png/bmp 格式"):
        super().__init__(err)


file_name = input("请输入上传图片的名称(包含格式):")
try:
    if file_name.split(".")[-1] in ["jpg", "png", "bmp"]:
        print("上传成功")
    else:
        raise FileTypeError
except Exception as error:
    print(error)
