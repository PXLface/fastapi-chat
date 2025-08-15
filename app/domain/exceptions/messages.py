from dataclasses import dataclass

from domain.exceptions.base import ApplicatedException


@dataclass(eq=False)
class TitleToolongException(ApplicatedException):
    text: str

    @property
    def message(self):
        return f'Слишком длинный текст сообщения "{self.text[:255]}..."'


@dataclass(eq=False)
class EmptyTextException(ApplicatedException):
    @property
    def message(self):
        return 'Текст не может быть пустым'
