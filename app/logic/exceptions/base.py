from dataclasses import dataclass

from domain.exceptions.base import ApplicatedException


@dataclass(eq=False)
class LogicException(ApplicatedException):
    @property
    def message(self):
        return 'В обработке запроса возникла ошибка'
