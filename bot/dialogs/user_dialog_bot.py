# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import CardFactory

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
from botbuilder.schema import (
    ActionTypes,
    HeroCard,
    CardAction,
    CardImage,
)
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState
from api.product_api import ProductAPI


class UserProfileDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(UserProfileDialog, self).__init__(UserProfileDialog.__name__)

        self.user_profile_accessor = user_state.create_property("UserProfile")

        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.prompt_option_step,
                    self.process_option_step,
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

    async def process_option_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        
        choice = step_context.result.value
        
        if choice == "Consultar Pedidos":
            await step_context.context.send_activity(f"Voce escolheu pedido.")
        elif choice == "Consultar Produtos":
            await self.show_card_produto(step_context.context)
        elif choice == "Extrato de Compras":
            await step_context.context.send_activity("Voce escolheu extrato de compras")
        
        return await step_context.end_dialog()
    
    async def show_card_produto(self ,turn_context):
        
        produto_api = ProductAPI()

        response = produto_api.consultar_api()
        print(response)

        #Chamada de API para obter os produtos
        card = CardFactory.hero_card(
            HeroCard(
                title=response["productName"],
                text=f"Preço: R$ {response['price']}",
                subtitle=response["productDescription"],
                images=[CardImage(url=response["imageUrl"][0])],
                buttons=[
                    CardAction(
                        type=ActionTypes.im_back,
                        title="Comprar Produto",
                        value=response["id"],
                    ),
                ],
            )
        )
        await turn_context.send_activity(MessageFactory.attachment(card))