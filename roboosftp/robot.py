import pysftp


class Roboot:
    def __init__(self, host, username, password, port=22):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        self.srv = pysftp.Connection(host=host, username=username,
                                     password=password, port=port,
                                     cnopts=cnopts)

    def ls(self:str):
        return self.srv.listdir()

    def cd(self, path:str):
        self.srv.cd(path)

    def download(self, path:str) -> bytes:
        r = b''
        with self.srv.open(path, 'rb') as file:
            r = file.read()
        return r

    def _close(self, *o):
        self.srv.close()
