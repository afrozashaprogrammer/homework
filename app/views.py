from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def index(request):
    person1 = {
        "name": "Raisha",
        "age": 22,
        "ia_married": "Flase"
    }
    person2 = {
        "name": "Ayesha",
        "age": 10,
        "is_married": "Flase"
    }
    person_list = [person1, person2]
    return Response(person_list)