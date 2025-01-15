from typing import Any
import boto3
from boto3.resources.base import ServiceResource
from application.contrib.exceptions import (
    CannotPerformFaceAnalysisError,
    CannotPerformLabelDetectionError,
)
from infrastructure.aws.bedrock import Bedrock


class Rekognition:
    KEYWORDS = ["Mammal", "Canine", "Puppy", "Cat", "Animal", "Pet", "Dog"]

    @staticmethod
    def client() -> ServiceResource:
        """Retorna o cliente Rekognition."""
        return boto3.client("rekognition", region_name="us-east-1")

    @staticmethod
    def detect_labels(bucket: str, image_name: str) -> dict[str, Any]:
        """Retorna todas as labels detectadas na imagem."""
        try:
            return Rekognition.client().detect_labels(
                Image={"S3Object": {"Bucket": bucket, "Name": image_name}},
                MaxLabels=25,
                MinConfidence=75,
            )
        except Exception as exc:
            raise CannotPerformLabelDetectionError(
                message=f"Não foi possível detectar labels na imagem: {str(exc)}"
            )

    @staticmethod
    def detect_faces(bucket: str, photo: str) -> list[dict[str, str]]:
        """Detecta rostos em uma imagem no S3 e retorna uma lista de detalhes sobre."""

        try:
            # Usa o cliente Rekognition para detectar rostos
            response = Rekognition.client().detect_faces(
                Image={"S3Object": {"Bucket": bucket, "Name": photo}},
                Attributes=["DEFAULT", "EMOTIONS"],
            )
        except Exception as exc:
            raise CannotPerformFaceAnalysisError(
                message=f"Não foi possível analisar os rostos fornecidos: {str(exc)}"
            )

        # obtem o resultado
        face_details = response.get("FaceDetails", [])

        return face_details

    @staticmethod
    def get_pet_labels(labels: list) -> list[dict]:
        """Filtra os labels que pertencem à categoria 'Animals and Pets'."""

        def is_animal_and_pet(label) -> bool:
            """Retorna True se a label for da categoria 'Animals and Pets'."""
            categories = label.get("Categories", [])
            return any(
                category["Name"] == "Animals and Pets" for category in categories
            )

        return [
            {"Confidence": label["Confidence"], "Name": label["Name"]}
            for label in labels
            if label["Name"] not in Rekognition.KEYWORDS[:4]
            and is_animal_and_pet(label)
        ]

    @staticmethod
    def generate_pet_tips(labels: list) -> dict[str, Any]:
        """Gera a resposta com labels filtrados e dicas baseadas na raça do pet."""
        pet_labels = Rekognition.get_pet_labels(labels)

        # Encontra as raças com base nos labels
        breeds = [
            label["Name"]
            for label in pet_labels
            if label["Name"] not in Rekognition.KEYWORDS
        ]

        # Formata a resposta
        response = [{"labels": pet_labels, "Dicas": "Nenhuma raça encontrada."}]

        if breeds:
            pet_name = breeds[0]
            # Utiliza o Bedrock para gerar as dicas, caso exista uma raça detectada
            response[0]["Dicas"] = Bedrock.generate_pet_tips(breed=pet_name).strip()

        return response
