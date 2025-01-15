import json
from application.contrib.build import build_http_response
from main import Emotion
from aws_lambda_powertools.utilities.parser import parse, ValidationError
from aws_lambda_powertools.utilities.parser.exceptions import InvalidModelTypeError
from infrastructure.schemas.emotion import EmotionIn
from aws_lambda_powertools.utilities.typing import LambdaContext
from application.contrib.exceptions import CannotDetectEmotionError


def lambda_handler(event: dict, context: LambdaContext):
    """Processa a imagem. Detecta emoções e retorna seus dados."""
    try:
        # faz o parse do body para objeto EmotionIn
        parsed_body = parse(event=json.loads(event.get("body")), model=EmotionIn)
    except InvalidModelTypeError as exc:
        # extrai a causa original quando é == ValidationError
        if isinstance(exc.__cause__, ValidationError):
            return build_http_response(
                status_code=500,
                body={"ValidationError": exc.__cause__.errors(include_url=False)},
            )
        # retorna qualquer mensagem de erro encapsulada em InvalidModelTypeError
        return build_http_response(status_code=500, body={"ValidationError": str(exc)})

    bucket = parsed_body.bucket
    image_name = parsed_body.imageName

    try:
        body = Emotion.detect_emotion(bucket=bucket, image_name=image_name)
        print(json.dumps(body))
    except CannotDetectEmotionError as exc:
        print(f"ERROR: {exc.message}")
        return build_http_response(status_code=500, body={"detail": exc.message})

    return build_http_response(status_code=200, body=body)
