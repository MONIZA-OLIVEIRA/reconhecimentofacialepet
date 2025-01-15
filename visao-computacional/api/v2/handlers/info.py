from application.contrib.build import build_http_response


def v2_description(event, context):
    body = {"message": "VISION api version 2."}

    return build_http_response(status_code=200, body=body)
