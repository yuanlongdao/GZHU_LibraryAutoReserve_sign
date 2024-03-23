infos = [
    {
        'sno': '32106100109',         # 学号
        'pwd': '@Yuan123456',         # 密码
        'devName': '101-130',   # 预约的座位号（不足3位数的要补零）
        'name': 'GG',        # 随便起个名字
        'periods': (            # 预约时间段（每段时间不能超过4小时）
            ('13:30:00', '17:30:00'),
            ('17:35:00', '21:00:00')
        ),
        'pushplus': 'c64029dab70a4991ad4c48dc8a070c9e',         # pushplus 的 token（用于推送消息到微信）
    },

    # 如果只是一个人预约座位，不需要帮别人预约签到，则可把下面三个字典注释/删除
    {
        'sno': '32106100109',  # 学号
        'pwd': '@Yuan123456',  # 密码
        'devName': '101-131',  # 预约的座位号（不足3位数的要补零）
        'name': 'GG',  # 随便起个名字
        'periods': (  # 预约时间段（每段时间不能超过4小时）
            ('13:30:00', '17:30:00'),
            ('17:35:00', '21:00:00')
        ),
        'pushplus': 'c64029dab70a4991ad4c48dc8a070c9e',  # pushplus 的 token（用于推送消息到微信）
    },
    {
        'sno': '32106100109',  # 学号
        'pwd': '@Yuan123456',  # 密码
        'devName': '101-132',  # 预约的座位号（不足3位数的要补零）
        'name': 'GG',  # 随便起个名字
        'periods': (  # 预约时间段（每段时间不能超过4小时）
            ('13:30:00', '17:30:00'),
            ('17:35:00', '21:00:00')
        ),
        'pushplus': 'c64029dab70a4991ad4c48dc8a070c9e',  # pushplus 的 token（用于推送消息到微信）
    },
    # {
    #     'sno': '******',
    #     'pwd': '******',
    #     'devName': 'M301-001',
    #     'name': '小白',
    #     'periods': (
    #         ('8:30:00', '12:30:00'),
    #         ('12:30:00', '16:30:00'),
    #         ('16:30:00', '20:30:00'),
    #         ('20:30:00', '21:45:00')
    #     ),
    #     'pushplus': '',
    # },
]
