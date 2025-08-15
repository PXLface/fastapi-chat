from dataclasses import dataclass

from domain.exceptions.base import ApplicatedException


@dataclass(eq=False)
class TextTooLongException(ApplicatedException):
    text: str

    @property
    def message(self):
        return f'Слишком длинный текст сообщения "{self.text[:255]}..."'
