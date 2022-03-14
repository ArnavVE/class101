import dropbox
class TransferData():
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def uploadfile(self,filefrom,file2):
        dbx=dropbox.Dropbox(self.accessToken)
        f=open(filefrom,"rb")
        dbx.files_upload(f.read(),file2)
def main():
    accessToken="sl.BDxfYO1-kNf0BR1N2y0QgGEduX9prQDYoOU2Yir9eoSSa9D7ezXyDq-FowogDmD57nt35MowOa9X4pOHgMSf7NOMQAVydTXLP0B5H1NIJ-hfhlnWjZOXwEpeKkuIyDqG9JIytBM"
    transferData=TransferData(accessToken)
    filefrom=input("enter the file path to transfer")
    file2=input("enter the full path to dropbox")
    transferData.uploadfile(filefrom,file2)
main()