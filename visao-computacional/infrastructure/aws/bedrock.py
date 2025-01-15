import boto3
from application.contrib.exceptions import CannotGeneratePetTipsError
from application.core.config import settings


class Bedrock:
    @staticmethod
    def client():
        """Cria um cliente Bedrock Runtime na região especificada."""
        return boto3.client("bedrock-runtime", region_name="us-east-1")

    @staticmethod
    def generate_pet_tips(breed: str):
        """Gera dicas sobre cuidados com o pet usando o cliente Bedrock."""
        user_message = (
            f"Forneça dicas práticas para cuidar de um cachorro da raça {breed}.\n"
            "Seja o mais direto possível, não me cumprimente, certifique-se de que as "
            "informações sejam práticas, bem curtas e aplicáveis.\n"
            "Estruture a resposta em seções, abordando o seguinte:\n"
            "1. Nível de energia: Descreva se a raça é mais ativa ou tranquila e "
            "dê exemplos de atividades que combinam com o nível de energia.\n"
            "2. Necessidades diárias de exercício físico: Especifique quanto tempo de "
            "atividade física e mental, sugerindo tipos de exercícios "
            "e jogos.\n"
            "3. Temperamento: Explique como essa raça se comporta em relação a humanos "
            "e outros animais, com crianças e dicas sobre socialização.\n"
            "4. Necessidades especiais de cuidados: Inclua informações sobre higiene, "
            "alimentação, destacando práticas recomendadas e produtos úteis.\n"
            "5. Problemas de saúde comuns: condições frequentes nessa raça e forneça "
            "dicas sobre como preveni-las ou gerenciá-las, incluindo recomendações de "
            "exames veterinários.\n"
        )

        try:
            # Enviar a mensagem ao modelo
            response = Bedrock.client().converse(
                modelId=settings.MODEL_ID,
                messages=[{"role": "user", "content": [{"text": user_message}]}],
                inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
            )

            # Extrair o conteúdo da resposta
            tips = response["output"]["message"]["content"][0]["text"]

            tips = tips.replace("\n", " ")  # Remove as quebras de linha

            return tips.strip()  # Retorna as dicas sem quebras de linha

        except Exception as exc:
            raise CannotGeneratePetTipsError(
                message=f"Não foi possível gerar as dicas para o pet: {str(exc)}"
            )
