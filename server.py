import Pyro4

@Pyro4.expose
class MyRemote:
    def say_hello(self, name):
        return f"Xin chào, {name}!"

    def say_name(self, anh):
        return f"Tôi tên là {anh}!"

def main():
    # Khởi tạo daemon Pyro4
    daemon = Pyro4.Daemon()
    # Đăng ký lớp MyRemote với Pyro4
    uri = daemon.register(MyRemote)
    print(f"Uri = {uri}")
    # Chờ yêu cầu từ client
    daemon.requestLoop()

if __name__ == "__main__":
    main()
