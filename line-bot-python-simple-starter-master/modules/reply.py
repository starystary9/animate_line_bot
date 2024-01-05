from linebot.models import (
    MessageEvent, TextMessage, StickerMessage, TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, MessageAction, URIAction, CarouselTemplate, CarouselColumn, QuickReply, QuickReplyButton
)

# 官方文件
# https://github.com/line/line-bot-sdk-python

# 常見問答表
faq = {
    '貼圖': StickerSendMessage(
        package_id='1',
        sticker_id='1'
    ),
   
    '交通': TextSendMessage(text='請問您想使用何種方式前往？',
                          quick_reply=QuickReply(items=[
                              QuickReplyButton(action=MessageAction(
                                  label="搭乘捷運", text="捷運")
                              ),
                              QuickReplyButton(action=MessageAction(
                                  label="搭乘公車", text="公車")
                              )
                          ])
                          ),
    '營業時間':TextSendMessage(
        text="10:00 - 22:00"
    ),
    '捷運': TextSendMessage(
        text="搭乘捷運至板南線西門站步行5分鐘即可抵達。"
    ),
    '營業地址': LocationSendMessage(
        title='location',
        address='Taipei',
        latitude=25.0452725,
        longitude=121.5069142
    ),
    '查詢更新': TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    # 選單一圖片網址
                    title='選單一',
                    text='點選下方按鈕查詢即時更新',
                    actions=[
                        MessageAction(
                            label='查詢芙莉蓮',
                            text='芙莉蓮'
                        ),
                        MessageAction(
                            label='查詢夜櫻家',
                            text='夜櫻家'
                        ),
                        MessageAction(
                            label='查詢躍動青春',
                            text='躍動青春'
                        )
                    ]
                ),
                CarouselColumn(
                    # 選單二圖片網址
                    title='選單二',
                    text='點選下方按鈕查詢即時匯率',
                    actions=[
                        MessageAction(
                            label='查詢舞妓家的料理人',
                            text='舞妓家的料理人'
                        ),
                        MessageAction(
                            label='查詢天國大魔鏡',
                            text='天國大魔鏡'
                        ),
                        MessageAction(
                            label='查詢小林家的龍女僕',
                            text='小林家的龍女僕'
                        )
                    ]
                ),
            ]
        )
    )
}

# 主選單
menu = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                title='主選單一',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='查詢更新',
                        text='查詢更新'
                    ),
                    MessageAction(
                        label='營業時間',
                        text='營業時間'
                    ),
                    MessageAction(
                        label='營業地址',
                        text='營業地址'
                    )
                ]
            ),
            CarouselColumn(
                title='主選單二',
                text='點選下方按鈕開始互動',
                actions=[
                    MessageAction(
                        label='交通資訊',
                        text='交通'
                    ),
                    MessageAction(
                        label='門市照片',
                        text='門市照片'
                    ),
                    URIAction(
                        label='官方網站',
                        uri='http://www.animate.tw/'
                    )
                ]
            )
        ]
    )
)
