from aiogram.filters.state import StatesGroup, State
from aiogram.types import Message

from aiogram_dialog import Dialog, DialogManager, DialogProtocol, Window
from aiogram_dialog.tools import render_transitions
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Back, Next
from aiogram_dialog.widgets.text import Const


class RenderSG(StatesGroup):
    first = State()
    second = State()
    last = State()


async def on_input(
        message: Message, dialog: DialogProtocol, manager: DialogManager,
):
    manager.dialog_data["name"] = message.text
    await manager.next()


dialog = Dialog(
    Window(
        Const("1. First"),
        Next(),
        state=RenderSG.first,
    ),
    Window(
        Const("2. Second"),
        Back(),
        MessageInput(on_input),
        state=RenderSG.second,
    ),
    Window(
        Const("3. Last"),
        Back(),
        state=RenderSG.last,
    ),
)

# this is diagram rendering
render_transitions([dialog])
