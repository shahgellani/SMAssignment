from rest_framework.response import Response


def error_response(success, status_code, message):
    return Response({
        "success": success,
        "status_code": status_code,
        "message": message
    })
