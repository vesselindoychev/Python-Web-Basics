from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only from letters')


@deconstructible
class ImageMaxSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError('Max file size is %sMB' % str(self.max_size))


    # def validate_file_max_size_in_mb(self, max_size):
    #     def validate(value):
    #         filesize = value.file.size
    #         if filesize > max_size * 1024 * 1024:
    #             raise ValidationError('Max file size is %sMB' % str(max_size))
    #
    #     return validate
