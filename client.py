import Pyro4

def main():
    uri = input("Cung cấp URI của đối tượng từ xa : ").strip()
    my_remote = Pyro4.Proxy(uri)
    response = my_remote.say_hello("Bạn tên là gì ? ")
    print(f"Kết quả: {response}")

if __name__ == "__main__":
    main()
