import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))



class LoggableList(list, Loggable):

    def append(self, obj):
        super(LoggableList, self).append(obj)
        self.log(obj)

z = LoggableList()
y = Loggable()
y.log('Kitty')
z.append('Hello')



