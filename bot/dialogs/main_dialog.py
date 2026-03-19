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
from dialogs.consultar_pedido_dialog import ConsultarPedidoDialog
from dialogs.consultar_produtos_dialog import ConsultarProdutoDialog
from dialogs.extrato_compra_dialog import ExtratoCompraDialog


class MainDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__("MainDialog")

        self.user_state = user_state

        #Prompt para escolha das opções
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(ConfirmPrompt(ConfirmPrompt.__name__))

        #Area de atendimento de consultar pedidos  
        self.add_dialog(ConsultarPedidoDialog())

        #Area de atendimento de consultar produtos
        self.add_dialog(ConsultarProdutoDialog())
        
        #Area de atendimento de extrato de compras
        self.add_dialog(ExtratoCompraDialog())

        # Prompt para escolha de opções
        # Tratamento das opções de escolha do usuário
        self.add_dialog(
            WaterfallDialog(
                "MainDialog",
                [
                    self.prompt_option_step,
                    self.process_option_step,
                ],
            )
        )


        self.initial_dialog_id = "MainDialog"

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
            return await step_context.begin_dialog("ConsultarPedidoDialog")
        elif choice == "Consultar Produtos":
            return await step_context.begin_dialog("ConsultarProdutoDialog")
        elif choice == "Extrato de Compras":
            return await step_context.begin_dialog("ExtratoCompraDialog")
        
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