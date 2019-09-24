import Pyro4

def get_server():
    #ganti "localhost dengan ip yang akan anda gunakan sebagai server"
    uri = "PYRONAME:greetserver@localhost:7777"
    gserver = Pyro4.Proxy(uri)
    return gserver

if __name__=='__main__':
    server = get_server()
    if server == None:
        exit()
    connected = True
    while connected:
        test = input ("> ").lower()
        cek = test.split()
        if cek[0] == 'create':
            print(server.command_create(test))
        elif cek[0] == 'delete':
            print(server.command_delete(test))
        elif cek[0] == 'read':
            print(server.command_read(test))
        elif cek[0] == 'update':
            print(server.command_updater(test))
        elif cek[0] == 'list':
            print(server.get_list_dir(test))
        elif cek[0] == 'exit':
            print(server.bye())
            connected = False
        else:
            print(server.failed())