from marshmallow import Schema, fields, validate


class UserSchema(Schema):
    username = fields.String(
        required=True, 
        validate=[
            validate.Length(min=3, max=32, error='Username must be a string between 3 and 32 letters.')
        ],
    )
    password = fields.String(
        required=True, 
        validate=[
            validate.Length(min=8, max=32, error='Password must be a string between 8 and 32 letters.'),
            validate.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", error='Password must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number.')
        ],
    )
