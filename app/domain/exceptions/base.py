from dataclasses import dataclass


@dataclass(eq=False)
class ApplicatedException(Exception):
    @property
    def message(self):
        return 'Произошла ошибка приложения.'
