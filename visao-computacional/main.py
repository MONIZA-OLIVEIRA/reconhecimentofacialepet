from typing import Any
from application.contrib.exceptions import (
    CannotDetectEmotionError,
    CannotDetectPetAndEmotionError,
    CannotGeneratePetTipsError,
    CannotGetObjectMetadataError,
    CannotPerformFaceAnalysisError,
    CannotPerformLabelDetectionError,
)
from infrastructure.aws.s3 import S3
from infrastructure.aws.rekognition import Rekognition
from application.contrib.build import (
    build_emotion_response,
    build_pet_and_emotion_response,
)


class Emotion:
    @staticmethod
    def detect_emotion(bucket: str, image_name: str) -> dict[str, Any]:
        """
        Analisa uma imagem e retorna dados sobre a emoção presente se houver um rosto
        """
        try:
            # Obtenção da data de criação da imagem no S3
            created_image_timestamp = S3.get_created_timestamp(
                bucket_name=bucket, object_name=image_name
            )
            # Retorna a URL da imagem
            url_to_image = S3.get_public_image_url(
                bucket_name=bucket, image_key=image_name
            )
            # Análise da imagem pelo Rekognition
            detected_faces = Rekognition.detect_faces(bucket=bucket, photo=image_name)

        except (CannotGetObjectMetadataError, CannotPerformFaceAnalysisError) as exc:
            raise CannotDetectEmotionError(message=exc.message)

        return build_emotion_response(
            face_details=detected_faces,
            url_to_image=url_to_image,
            created_image_timestamp=created_image_timestamp,
        )


class PetAndEmotion:
    @staticmethod
    def detect_pet_and_emotion(bucket: str, image_name: str):
        """
        Analisa uma imagem e retorna dados sobre a raça de
        um cachoro e a emoção presentes se houver um rosto e um pet.
        """
        try:
            # Detectar labels da imagem com Rekognition
            labels = Rekognition.detect_labels(bucket=bucket, image_name=image_name)
            pet_labels = Rekognition.generate_pet_tips(labels=labels["Labels"])
            detected_emotion = Emotion.detect_emotion(
                bucket=bucket, image_name=image_name
            )

            # Retorna a URL da imagem
            url_to_image = S3.get_public_image_url(
                bucket_name=bucket, image_key=image_name
            )

            # Obtenção da data de criação da imagem no S3
            created_image_timestamp = S3.get_created_timestamp(
                bucket_name=bucket, object_name=image_name
            )
        except (
            CannotDetectEmotionError,
            CannotGeneratePetTipsError,
            CannotGetObjectMetadataError,
            CannotPerformLabelDetectionError,
        ) as exc:
            raise CannotDetectPetAndEmotionError(message=exc.message)

        return build_pet_and_emotion_response(
            url_to_image=url_to_image,
            created_image=created_image_timestamp,
            face_details=detected_emotion["faces"],
            pets=pet_labels,
        )
