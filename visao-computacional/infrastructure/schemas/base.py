from pydantic import BaseModel, Field


class InSchema(BaseModel):
    """Schema base para entrada de dados dos enpoints"""

    bucket: str = Field(description="Nome do bucket S3", examples=["bucket-1"])
    imageName: str = Field(
        description="Key da imagem armazenada no S3",
        examples=["picture.jpg"],
        pattern=r".*\.(jpg|jpeg|png|gif|bmp|tiff|webp)$",
    )

    class Config:
        extra = "forbid"
