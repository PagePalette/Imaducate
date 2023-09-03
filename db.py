


class PageModel:

    def __init__(self, content: str, img: str | None = None):
        self.content = content
        self.img = img


class BookModel:

    def __init__(self, name: str, author: str, pages: list[PageModel]):
        self.name = name
        self.author = author
        self.pages = pages


class Repository:

    def __init__(self, book: list[BookModel]):
        self.book = book


GLOBAL_REPO: Repository = Repository([
    BookModel(
        "호두까기 인형", "차이코프스키", [
            PageModel("""
충실한 나의 부하 북치기 변정이여, 행진곡을 쳐라!"
호두까기 인형이 우렁차게 외치자 즉시 북치는 병정이 가장 기이한 방식으로 북을 둥둥 두드리기 시작해서
유리 장식장의 창문이 흔들리고 위윙거렸다. 그러더니 장식장 안에서 쿵쿵거리고 덜커덩거리는 비상한 소리가 났다.
마리는 이 소리를 듣고서 마침내 프리츠의 군대가 숙영 중이던 전체 상자들의 뚜껑이 힘차게 열렸고 병사들이
몰려나와 맨 아래 칸으로 뛰어내렸으며, 그곳에서도 뺵뺵하게 무리지어 깔끔하게 집합했다는 것 깨닫게 되었다.
            """),
            PageModel("""
호두까기 인형은 위아래로 뛰어다니며 부대원들에게 이러한 말을 하면서 감격시켰다.
"나팔수들의 개가 꼼짝도 하지 않잖아." 호두까기 인형이 몹시 화가 나서 소리를 질렀단다.
하지만 그런 다음에 약간 창백해지고, 긴 턱을 격렬하게 흔들고 있는 바람둥이 노인인 판탈로네에게 몸을 돌려서 엄숙하게 말했다.
            """)
        ]
    )
])
