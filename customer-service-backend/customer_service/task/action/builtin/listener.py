from typing import Any

from customer_service.domain.state import DialogueState
from customer_service.task.action.base import Action, ActionResult


class ActionListener(Action):
    name = "action_listen"

    async def run(self, state: DialogueState, action_kwargs: dict[str, Any]) -> ActionResult:
        """
        不会实现（哨兵）
        :param state:
        :param action_kwargs:
        :return:
        """





