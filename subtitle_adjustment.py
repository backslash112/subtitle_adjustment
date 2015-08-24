#with open('subtitle.txt') as subtitle:
#    for line in subtitle:
#        timer = float(line[6:])+0.01
#        with open('subtitle_result.txt', 'a') as result_file:
#            result_file.write(line[0:6]+"%.2f"%timer+'\n')


class SubtitleAdjustment(object):
    def __init__(self):
        print("myclass init")

    @classmethod
    def test(self):
        print("test")
    
    def test2(self):
        print("test2")

    def run(self):
        print("SubtitleAdjustment - run")
        with open('subtitle.txt') as subtitle:
            for line in subtitle:
                timer = float(line[6:])+0.01
                with open('subtitle_result.txt', 'a') as result_file:
                    result_file.write(line[0:6]+"%.2f"%timer+'\n')