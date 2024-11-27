"""pylintの動作を理解してもらうだけの非常に単純なプログラムです。"""

def sayhello():
    """挨拶をする関数です。
    """
    print("Hello")

def main():
    """挨拶をして、変数aとbの値を表示し、a+bとa*b-bの値を表示します。
    """
    a = 2
    b = 4

    sayhello()
    print(f"{a=}")
    print(f"{b=}")
    print(f"{a+b=}")
    print(f"{a*b-b=}")


if __name__ == "__main__":
    main()
