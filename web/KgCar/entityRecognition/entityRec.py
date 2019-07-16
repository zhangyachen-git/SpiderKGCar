from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
# 中文词法分析工具包
import thulac


@csrf_exempt
# 中文分词+词性标注+命名实体识别
def ner_post(request):
    ctx = {}
    if request.POST:
        # 获取输入文本
        key = request.POST['user_text']
        print("key:", key)
        get_ner(key)
        # return render(request, "entityRecognition.html")
    return render_to_response("entityRecognition.html")


# 获取中文分词
def get_ner(text):
    thuFactory = thulac.thulac()
    taglist = thuFactory.cut(text, text=False)
    # taglist.append(['===', None])
    i = 0
    for taglist_part in taglist:
        print(taglist_part)
        # 当前词性筛选
        word_pro = curword(taglist_part[1])


# 当前词的词性筛选
def curword(s):
    '''
    n/名词 np/人名 ns/地名 ni/机构名 nz/其它专名
    m/数词 q/量词 mq/数量词 t/时间词 f/方位词 s/处所词
    v/动词 a/形容词 d/副词 h/前接成分 k/后接成分 i/习语
    j/简称 r/代词 c/连词 p/介词 u/助词 y/语气助词
    e/叹词 o/拟声词 g/语素 w/标点 x/其它
    '''
    if s == "n":
        print("名词")
    if s == "np":
        print("人名")
    if s == "ns":
        print("地名")
    if s == "ni":
        print("机构名")
    if s == "nz":
        print("其他专名")

    if s == "m":
        print("数词")
    if s == "q":
        print("量词")
    if s == "mq":
        print("数量词")
    if s == "t":
        print("时间词")
    if s == "f":
        print("方位词")
    if s == "s":
        print("处所词")
    if s == "v":
        print("动词")
    if s == "a":
        print("形容词")
    if s == "d":
        print("副词")
    if s == "h":
        print("前接成分")
    if s == "k":
        print("后接成分")
    if s == "i":
        print("习语")
    if s == "j":
        print("简称")
    if s == "r":
        print("代词")
    if s == "c":
        print("连词")
    if s == "p":
        print("介词")
    if s == "u":
        print("助词")
    if s == "y":
        print("语气助词")
    if s == "e":
        print("叹词")
    if s == "o":
        print("拟声词")
    if s == "g":
        print("语素")
    if s == "w":
        print("标点")
    if s == "x":
        print("其它")


if __name__ == '__main__':
    text = "德国老牌豪华品牌Borgward在日内瓦车展现场宣布品牌复兴，" \
           "发布会上Borgward也公布了其今后在中国市场的中文名称宝沃，其中宝同BORG，寓意珍贵和地位，" \
           "沃同WARD寓意为丰盛、润泽和富饶，合二为一，取物华天宝，沃壤千里之意。" \
           "这是继1949年Hansa 1500在日内瓦车展亮相以来，这一德国汽车品牌首次重返日内瓦车展舞台。"
    get_ner(text)