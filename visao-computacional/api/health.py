from application.contrib.build import build_http_response


def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return build_http_response(status_code=200, body=body)
