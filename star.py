# 根据月日返回星座 元组
star_month = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
              u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
month = ((1, 20), (2, 20), (3, 20), (4, 20), (5, 20), (6, 20), (7, 20), (8, 20),
         (9, 20), (10, 20), (11, 20), (12, 20))
birthday = (12, 18)
index = len(list(filter(lambda x: x < birthday, month)))
print(star_month[index % 12])
