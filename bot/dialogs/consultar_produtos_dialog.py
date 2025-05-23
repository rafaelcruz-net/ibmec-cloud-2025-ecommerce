from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions
from botbuilder.dialogs import DialogTurnStatus, DialogTurnResult
from botbuilder.schema import (
    ActionTypes,
    HeroCard,
    CardAction,
    CardImage,
)
from botbuilder.core import CardFactory
from api.product_api import ProductAPI
from dialogs.comprar_produto_dialog import ComprarProdutoDialog
from botbuilder.core import UserState

class ConsultarProdutosDialog (ComponentDialog):
    def __init__(self, user_state: UserState):
        super(ConsultarProdutosDialog, self).__init__("ConsultarProdutosDialog")

        self.add_dialog(TextPrompt(TextPrompt.__name__))

        self.add_dialog(TextPrompt("comprarProduto"))

         #Area de atendimento de consultar pedidos
        self.add_dialog(ComprarProdutoDialog(user_state))

        self.add_dialog(
            WaterfallDialog(
                "consultarProdutoWaterfall",
                [
                    self.product_name_step,
                    self.product_name_search_step,
                    self.buy_product_step
                ],
            )
        )

        self.initial_dialog_id = "consultarProdutoWaterfall"
    
    async def product_name_step(self, step_context: WaterfallStepContext):
        
        prompt_message = MessageFactory.text("Por favor, digite o nome do produto que você deseja consultar.")

        prompt_options = PromptOptions(
            prompt=prompt_message,
            retry_prompt=MessageFactory.text("Desculpe, não consegui entender. Por favor, digite o nome do produto novamente."),
        )
        
        return await step_context.prompt(TextPrompt.__name__, prompt_options)
    
    async def product_name_search_step(self, step_context: WaterfallStepContext):

        product_name = step_context.result

        await self.show_card_results(product_name, step_context)

        return DialogTurnResult(
            status=DialogTurnStatus.Waiting,
            result=step_context.result,
        )


    async def buy_product_step(self, step_context: WaterfallStepContext):

        result_action = step_context.context.activity.value

        if (result_action is None):
            return await step_context.end_dialog()
        
        if result_action["acao"] == "comprar":

            product_id = result_action["productId"]

            return await step_context.begin_dialog("ComprarProdutoDialog", {"productId": product_id})

            #Direcionar para outro dialog de compras
        
        return await step_context.end_dialog()

    async def show_card_results(self, productName, step_context: WaterfallStepContext):
        produto_api = ProductAPI()

        response = produto_api.search_product(productName)

        for produto in response:
            #Montando o card
            card = CardFactory.hero_card(
                HeroCard(
                    title=produto["productName"],
                    text=f"Preço: R$ {produto['price']}",
                    subtitle=produto["productDescription"],
                    images=[CardImage(url=imagem) for imagem in produto["imageUrl"]],
                    buttons=[
                        CardAction(
                            type=ActionTypes.post_back,
                            title=f"Comprar {produto["productName"]}",
                            value={"acao": "comprar", "productId": produto["id"]},

                        )
                    ],
                )
            )

            await step_context.context.send_activity(MessageFactory.attachment(card))    
