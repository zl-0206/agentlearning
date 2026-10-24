class Phone:
    __current__=None#私有成员

    def __keep_single_core(self):
        print(3442)

    def call(self):
        if self.__current__>1:
            print('open')
        else:
            self.__keep_single_core()
            print('fail')

phone=Phone()
phone.__current__=2
phone.call()

print('==========')

class Phone:
    __is_5g_able=True

    def __check(self):
        if self.__is_5g_able:
            print('success')
        else:
            print('fail')

    def call_by_5g(self):
        self.__check()
        print('calling now')


phone=Phone()
#外部无法调用私有部分 phone.__check(self)
phone.call_by_5g()




