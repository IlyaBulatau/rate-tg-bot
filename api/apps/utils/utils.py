class AccesTokenFromHeaderService:
    """Мидлварь ограничивает доступ к ресурсу проверяя начилие токена"""
    BEARER_TOKEN_TYPE = "Bearer"

    def __init__(self, headers: dict[str]):
        self.headers = headers

    def is_access(self, access_token: str) -> bool:
        """Вызвыть для проверки токена"""
        authorization_header = self.headers.get("Authorization")
        if not authorization_header:
            return False

        token_type = self.get_token_type(authorization_header)
        if not self.is_bearer_token(token_type):
            return False

        return self.get_token(authorization_header) == access_token

    def get_token_type(self, auth_header: str) -> str:
        token_type = auth_header.split(" ", 1)[0]
        return token_type

    def is_bearer_token(self, token_type: str) -> bool:
        return token_type == self.BEARER_TOKEN_TYPE

    def get_token(self, auth_header: str) -> str:
        token = auth_header.split(" ", 1)[1]
        return token
