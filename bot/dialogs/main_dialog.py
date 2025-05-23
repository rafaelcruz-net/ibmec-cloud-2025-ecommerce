# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.dialogs.prompts import (
    TextPrompt,
    NumberPrompt,
    ChoicePrompt,
    ConfirmPrompt,
    AttachmentPrompt,
    PromptOptions,
    PromptValidatorContext,
)
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState

from data_models.user_profile import UserProfile
from api.product_api import ProductAPI
from botbuilder.schema import (
    ActionTypes,
    HeroCard,
    CardAction,
    CardImage,
)

from botbuilder.core import CardFactory
from dialogs.consultar_produtos_dialog import ConsultarProdutosDialog
from dialogs.consultar_pedidos_dialog import ConsultarPedidosDialog
from dialogs.extrato_compra_dialog import ExtratoCompraDialog


class MainDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.user_state = user_state

        #Area de atendimento de consultar produtos
        self.add_dialog(ConsultarProdutosDialog(user_state))

        #Area de atendimento de consultar pedidos
        self.add_dialog(ConsultarPedidosDialog())

        #Area de atendimento de extrato de compras
        self.add_dialog(ExtratoCompraDialog())

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.prompt_option_step,
                    self.process_option_step
                ],
            )
        )

        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))

        self.initial_dialog_id = WaterfallDialog.__name__

    async def prompt_option_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text("Escolha a opção desejada:"),
                choices=[Choice("Consultar Pedidos"), Choice("Consultar Produtos"), Choice("Extrato de Compras")],
            ),
        )

    async def process_option_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        
        option = step_context.result.value

        if option == "Consultar Pedidos":
            #Iniciando um novo dialog para consultar pedidos
            return await step_context.begin_dialog("ConsultarPedidosDialog")
        elif option == "Consultar Produtos":
            #Iniciando um novo dialog para consultar produtos
            return await step_context.begin_dialog("ConsultarProdutosDialog")
        elif option == "Extrato de Compras":
            #Iniciando um novo dialog para Extrato de Compras
            return await step_context.begin_dialog("ExtratoCompraDialog")

        return await step_context.end_dialog()
    

       