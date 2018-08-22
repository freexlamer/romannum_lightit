from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from romarabconv import RumanArabicConverter

@api_view(['POST'])
def convert(request):
    conv = RumanArabicConverter()
    if request.method == 'POST':
        if 'input' in request.data:
            return Response(json.dumps({'output':conv.convert_multi(request.data['input'])}), 
                            status=status.HTTP_201_CREATED)
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)
        
