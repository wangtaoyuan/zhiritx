# encoding=utf-8


from datebase import select_zrtx

if __name__ == '__main__':
    print(select_zrtx("select name from date_work where date=910"))
    name = select_zrtx("select name from date_work where date=%d" % 513)
    print(name)
    print(select_zrtx("select email from worker where name='王涛渊'"))
    print(select_zrtx("select email from worker where name='%s' " % name))

