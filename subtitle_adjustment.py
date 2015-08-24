#with open('subtitle.txt') as subtitle:
#    for line in subtitle:
#        timer = float(line[6:])+0.01
#        with open('subtitle_result.txt', 'a') as result_file:
#            result_file.write(line[0:6]+"%.2f"%timer+'\n')


class MyClass(object):
    def __init__(self):
        print("myclass init")

    def test(self):
        print("test")


def adjustment_subtitle():
    print("adjustment_subtitle")
    with open('subtitle.txt') as subtitle:
        for line in subtitle:
            timer = float(line[6:])+0.01
            with open('subtitle_result.txt', 'a') as result_file:
                result_file.write(line[0:6]+"%.2f"%timer+'\n')

def main():
    print("starting")
    adjustment_subtitle()

if __name__ == "__main__":
    main()
    myClass = MyClass()
    myClass.test()