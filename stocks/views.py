from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# Create your views here.

def home(request):
    #ticker = request.GET['ticker'] # 요청 데이터 중 ticker라는 이름의 값을 GET방식으로 가져온다.
    # 그러나 위처럼 해버리면, 홈 화면 자체가 안들어가진다. ticker 자체가 없는 상태이기 때문이다.
    # 이럴때는 파이썬의 예외처리를 적용해준다.
    try:
        ticker = request.GET['ticker']
        stock_api = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=")
        stock = json.loads(stock_api.content)  # json 데이터가 parsing까지 끝내고 파이썬의 딕셔너리 형태로 된다.

    except Exception as e: # 빈 데이터를 보여줄 때의 경우; 에러나는 이유
        stock = ""

    #stock_api = requests.get("https://cloud.iexapis.com/stable/stock/AMZN/quote?token=")
    # 위의 주소는 하드코딩된 티커값의 주소이기 때문에, 정규표현식으로 바꿔줄 필요가 있다.

    content = {'stock':stock} # home.html에서 템플릿 태그 안에 stock으로 써줄 수 있다.

    return render(request, 'stocks/home.html', content)
    # 웹을 부를 때 자동으로 templates 폴더를 탐색하기 때문에
    # templates/stocks/home.html을 하지 않아도 된다.

    # 다른 앱의 home.html에 접근하지 않도록 하기 위해서
    # 명시적으로 앱이름/home.html 처럼 구성해주는 것이다.

    # view에서 home이 실행되면,
    # home.html에서 content값을 사용할 수 있다.