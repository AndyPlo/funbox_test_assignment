import re
import time

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

PATTERN = r'^(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n\?\=]+)'


# Валидатор. В процессе создания.
def is_valid(data):
    return True


def domain_clearing(data, timestamp):
    clear_data = {}
    clear_data[timestamp] = set()
    for link in data['links']:
        clear_data[timestamp].add(re.match(PATTERN, link).group())
    return clear_data


@api_view(['POST'])
def visited_links(request):
    if request.method == 'POST':
        data = request.data
        timestamp = time.time()
        if is_valid(data):
            clear_data = domain_clearing(data, timestamp)
            return Response(
                {
                    'clear_data': clear_data,
                    'status': 'ok'
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'status': 'validation_error'
            },
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def visited_domains(request):
    return Response(
        'ok',
        status=status.HTTP_200_OK
    )
