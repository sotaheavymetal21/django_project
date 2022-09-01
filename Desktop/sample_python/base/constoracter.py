# コンストラクタ,デストラクタ


class SampleClass:

    def __init__(self, msg, name=None):  # コンストラクタ
        print("コンストラクタが呼ばれました")
        self.msg = msg  # インスタンス変数
        self.name = name  # インスタンス変数
        print(self)  # <__main__.SampleClass object at 0x7f97394d6fd0>
        print(name)

    def __del__(self):
        print("デストラクタが実行されました")
        print("name = {}".format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)


var_1 = SampleClass("Hello", "Sota")
var_1.print_msg()  # Hello
var_1.print_name()  # Sota
del var_1  # インスタンスが削除される
