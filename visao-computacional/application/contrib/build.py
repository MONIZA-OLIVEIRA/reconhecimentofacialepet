import json
from typing import Any


def build_http_response(
    status_code: int, body: dict, content_type: str = "application/json"
) -> dict[str, Any]:
    """Retorna uma resposta HTTP com status, corpo e cabeçalho."""
    return {
        "statusCode": status_code,
        "body": json.dumps(body, ensure_ascii=False, indent=4),
        "headers": {"Content-Type": content_type},
    }


def build_emotion_response(
    face_details: list[dict], url_to_image: str, created_image_timestamp: str
) -> dict[str, Any]:
    def format_face(face: dict) -> dict:
        """Retorna um dicionário com os dados do rosto detectado."""
        bbox = face.get("BoundingBox", {})
        emotion = max(face["Emotions"], key=lambda e: e["Confidence"])
        return {
            "position": {
                key: bbox.get(key) for key in ["Height", "Left", "Top", "Width"]
            },
            "classified_emotion": emotion["Type"],
            "classified_emotion_confidence": emotion["Confidence"],
        }

    def empty_face() -> dict[str, Any]:
        """Retorna um dicionário com dados nulaos se rostos não forem detectados."""
        return {
            "position": {key: None for key in ["Height", "Left", "Top", "Width"]},
            "classified_emotion": None,
            "classified_emotion_confidence": None,
        }

    # Constrói o item do retorno com base nos rostos detectados pelo Rekognition
    faces = (
        [format_face(face) for face in face_details] if face_details else [empty_face()]
    )
    return {
        "url_to_image": url_to_image,
        "created_image": created_image_timestamp,
        "faces": faces,
    }


def build_pet_and_emotion_response(
    url_to_image: str,
    created_image: str,
    pets: list[dict],
    face_details: list[dict] = None,
) -> dict[str, Any]:
    """Constrói o item do retorno com base nos pets e rostos detectados."""
    response = {
        "url_to_image": url_to_image,
        "created_image": created_image,
        "faces": face_details,
        "pets": pets,
    }
    if not face_details[0].get("classified_emotion"):
        del response["faces"]
        return response

    return response
