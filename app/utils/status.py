class CodeDefinition:
    def __init__(self, code, message):
        self.code = code
        self.__message = message

    @property
    def message(self):
        return self.__message

    def format_message(self, **kwargs):
        if kwargs:
            return self.__message.format(**kwargs)
        return self.__message


SUCCESS = CodeDefinition(200, 'The action perform successfully.')
LOGIN_SUCEESS = CodeDefinition(200, 'Login success.')
CREATE_SUCCESS = CodeDefinition(201, 'Account was created successfully.')
UNEXPECTED_ERROR = CodeDefinition(500, 'An unexpected error has occurred.')
BAD_REQUEST = CodeDefinition(400, 'Bad request.')
UNAUTHORIZED = CodeDefinition(401, 'Unauthorized.')
FORBIDDEN = CodeDefinition(403, 'Forbidden.')
USER_NOT_FOUND = CodeDefinition(404, 'User not found.')
PASSWORD_ERROR = CodeDefinition(404, 'Password not correct.')
CONFLICT = CodeDefinition(409, 'Username is existed.')
UNSUPPORTED_MEDIA_TYPE = CodeDefinition(415, 'Unsupported media type.')
PARAMETER_ERROR = CodeDefinition(422, 'Parameter error.')
