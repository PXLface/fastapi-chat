from dataclasses import dataclass, field

from domain.entities.base import BaseEntity
from domain.events.messages import NewChatCreated, NewMessageReceivedEvent
from domain.values.messages import Text, Title


@dataclass(frozen=True)
class Message(BaseEntity):
    text: Text


@dataclass(frozen=True)
class Chat(BaseEntity):
    title: Title
    messages: set[Message] = field(
        default_factory=set,
        kw_only=True,
    )

    @classmethod
    def create_chat(cls, title: Title) -> 'Chat':
        new_chat = cls(title=title)
        new_chat.register_event(NewChatCreated(chat_oid=new_chat.oid, title=new_chat.title.as_generic_type()))

    def add_message(self, message: Message):
        self.messages.add(message)
        self.register_event(NewMessageReceivedEvent(
            message_text=message.text.as_generic_type(),
            chat_oid=self.oid,
            message_oid=message.oid
        ))
