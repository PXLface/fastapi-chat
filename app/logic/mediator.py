from collections import defaultdict
from dataclasses import dataclass, field
from typing import Dict, Iterable, Type

from domain.events.base import BaseEvent
from logic.commands.base import CR, CT, BaseCommand, CommandHandler
from logic.events.base import ER, ET, EventHandler
from logic.exceptions.mediator import CommandHandlersNotRegisterException, EventHandlersNotRegisterException

@dataclass(eq=False)
class Mediator:
    events_map: dict[ET, EventHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    commands_map: dict[CT, CommandHandler] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    def register_event(self, event: ET, event_handler: EventHandler[ET, ER]) -> None:
        self.events_map[event].append(event_handler)

    def register_command(self, command: CT, command_handler: CommandHandler[CT, CR]) -> None:
        self.commands_map[command].append(command_handler)

    async def handle_event(self, events: BaseEvent) -> ER:
        event_type = events.__class__
        handlers = self.events_map.get(event_type)
        
        if not handlers:
            raise EventHandlersNotRegisterException(event_type=event_type)

        result = []

        for event in events:
            result.extend([await handler.handle(event) for handler in handlers])

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map.get(command_type)

        if not handlers:
            raise CommandHandlersNotRegisterException(command_type=command_type)

        return [await handler.handle(command) for handler in handlers]
