import boto3
from boto3.resources.base import ServiceResource
from application.contrib.date import format_date
from application.contrib.exceptions import CannotGetObjectMetadataError


class S3:
    @staticmethod
    def client() -> ServiceResource:
        """Retorna o cliente S3."""
        return boto3.client("s3", region_name="us-east-1")

    @staticmethod
    def get_public_image_url(bucket_name: str, image_key: str) -> str:
        # Construção da URL pública
        return f"https://{bucket_name}.s3.amazonaws.com/{image_key.replace(' ', '+')}"

    @staticmethod
    def get_object_metadata(bucket_name: str, object_name: str) -> dict:
        """Obtém metadados de um objeto no S3."""
        try:
            return S3.client().head_object(Bucket=bucket_name, Key=object_name)
        except Exception as exc:
            raise CannotGetObjectMetadataError(
                message=f"Não foi possível obter os metadados do objeto S3: {str(exc)}"
            )

    @staticmethod
    def get_created_timestamp(bucket_name: str, object_name: str) -> str:
        """Retorna a data de criação do objeto no S3."""

        metadata = S3.get_object_metadata(bucket_name, object_name)
        # Retorna a data formatada
        return format_date(metadata["LastModified"])
