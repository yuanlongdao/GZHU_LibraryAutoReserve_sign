infos = [
    {
        'sno': '32106100110',         # 学号
        'pwd': 'XLB021208.',         # 密码
        'devName': '101-244',   # 预约的座位号（不足3位数的要补零）
        'name': 'GG',        # 随便起个名字
        'periods': (            # 预约时间段（每段时间不能超过4小时）
            ('13:30:00', '17:30:00'),
            ('17:35:00', '21:00:00')
        ),
        'pushplus': '653749a946d142e581b00bc9a49469b8',         # pushplus 的 token（用于推送消息到微信）
    },

    # 如果只是一个人预约座位，不需要帮别人预约签到，则可把下面三个字典注释/删除
    # {
    #     'sno': '32106100110',  # 学号
    #     'pwd': 'XLB021208.',  # 密码
    #     'devName': '101-342',  # 预约的座位号（不足3位数的要补零）
    #     'name': 'GG',  # 随便起个名字
    #     'periods': (  # 预约时间段（每段时间不能超过4小时）
    #         ('14:30:00', '18:30:00'),
    #         ('18:35:00', '21:00:00')
    #     ),
    #     'pushplus': '653749a946d142e581b00bc9a49469b8',  # pushplus 的 token（用于推送消息到微信）
    # },
    # {
    #     'sno': '32106100110',  # 学号
    #     'pwd': 'XLB021208.',  # 密码
    #     'devName': '101-245',  # 预约的座位号（不足3位数的要补零）
    #     'name': 'GG',  # 随便起个名字
    #     'periods': (  # 预约时间段（每段时间不能超过4小时）
    #         ('14:30:00', '18:30:00'),
    #         ('18:35:00', '21:00:00')
    #     ),
    #     'pushplus': '653749a946d142e581b00bc9a49469b8',  # pushplus 的 token（用于推送消息到微信）
    # },
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
