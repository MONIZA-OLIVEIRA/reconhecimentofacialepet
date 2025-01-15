from typing import Optional


class BaseException(Exception):
    """Classe base para todas as exceções personalizadas."""

    def __init__(self, *args: object, message: Optional[str] = None) -> None:
        super().__init__(*args)

        if message:
            self.message = message


class CannotDetectEmotionError(BaseException):
    """Não foi possível concluir a detecção de emoções."""

    def __init__(self, *args: object, message: Optional[str] = None) -> None:
        super().__init__(*args, message=message)


class CannotDetectPetAndEmotionError(BaseException):
    """Não foi possível gerar as dicas para o pet."""

    def __init__(self, *args: object, message: Optional[str] = None) -> None:
        super().__init__(*args, message=message)


class CannotGetObjectMetadataError(BaseException):
    """Não foi possível obter os metadados do objeto."""

    def __init__(self, *args: object, message: Optional[str] = None) -> None:
        super().__init__(*args, message=message)


class CannotGeneratePetTipsError(BaseException):
    """Não foi possível gerar as dicas para o pet."""

    def __init__(self, *args: object, message: Optional[str] = None) -> None:
        super().__init__(*args, message=message)


class CannotPerformFaceAnalysisError(BaseException):
    """Não foi possível fazer a análise do rosto fornecido."""

    def __init__(self, *args: object, message: Optional[str] = None) -> None:
        super().__init__(*args, message=message)


class CannotPerformLabelDetectionError(BaseException):
    """Não foi possível detectar labels na imagem."""

    def __init__(self, *args: object, message: Optional[str] = None) -> None:
        super().__init__(*args, message=message)
