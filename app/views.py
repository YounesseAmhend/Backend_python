from app.models.http import HttpRequest, HttpResponse

def home_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(status_code=200)

def echo_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status_code=200,
        body=request.path.value,
    )

def get_user_agent(request: HttpRequest) -> HttpResponse:
    print(f"Headers {request.headers.user_agent}")
    return HttpResponse(
        status_code=200,
        body=request.headers.user_agent,        
    )

def hello(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        status_code=200,
        body='Hello World!'
    )