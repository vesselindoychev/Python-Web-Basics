from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = 'Ensure this value contains only letters.'


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__mb_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __mb_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'
