from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory
from botbuilder.core import MessageFactory, UserState
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions

from models.product_buy import ProductBuyModel

class ComprarProdutoDialog (ComponentDialog):
    def __init__(self, user_state: UserState):
        super(ComprarProdutoDialog, self).__init__("ComprarProdutoDialog")

        self.add_dialog(TextPrompt("numeroCartaoCreditoPrompt"))
        self.add_dialog(TextPrompt("dataExpiracaoPrompt"))
        self.add_dialog(TextPrompt("cvvPrompt"))

        self.add_dialog(
            WaterfallDialog(
                "comprarProdutoWaterfall",
                [
                    self.numero_cartao_step,
                    self.data_expiracao_step,
                    self.cvv_step,
                    self.final_step
                ],
            )
        )


        self.initial_dialog_id = "comprarProdutoWaterfall"

    async def numero_cartao_step(self, step_context: WaterfallStepContext):
        
        product_id = step_context.options.get("productId")

        #Grava na memoria o id do produto
        step_context.values["productId"] = product_id
        
        prompt_message = MessageFactory.text("Por favor, digite o numero de seu cartão de crédito.")

        prompt_options = PromptOptions(
            prompt=prompt_message,
            retry_prompt=MessageFactory.text("Desculpe, não consegui entender. Por favor, digite o nome do produto novamente."),
        )
        
        return await step_context.prompt("numeroCartaoCreditoPrompt", prompt_options)
    async def data_expiracao_step(self, step_context: WaterfallStepContext):
        
        #Grava na memoria o numero do cartao
        step_context.values["numero_cartao"] = step_context.result
        
        prompt_message = MessageFactory.text("Por favor, digite a data de expiração.")

        prompt_options = PromptOptions(
            prompt=prompt_message,
            retry_prompt=MessageFactory.text("Desculpe, não consegui entender. Por favor, digite o nome do produto novamente."),
        )

        return await step_context.prompt("dataExpiracaoPrompt", prompt_options)
    async def cvv_step(self, step_context: WaterfallStepContext):
        
        #Grava na memoria a data de expiração
        step_context.values["data_expiracao"] = step_context.result

          
        prompt_message = MessageFactory.text("Por favor, digite a o cvv do cartão.")

        prompt_options = PromptOptions(
            prompt=prompt_message,
            retry_prompt=MessageFactory.text("Desculpe, não consegui entender. Por favor, digite o nome do produto novamente."),
        )

        return await step_context.prompt("cvvPrompt", prompt_options)
    async def final_step(self, step_context: WaterfallStepContext):
        
        #Grava na memoria o cvv
        step_context.values["cvv"] = step_context.result

        product_id = step_context.values["productId"]
        numero_cartao = step_context.values["numero_cartao"]
        data_expiracao = step_context.values["data_expiracao"]
        cvv = step_context.values["cvv"]

        product_buy_model = ProductBuyModel(product_id, numero_cartao, data_expiracao, cvv)

        # Aqui você pode adicionar a lógica para processar a compra com os dados do product_buy_model
        # Por exemplo, chamar uma API ou fazer alguma operação de banco de dados.
        print(product_buy_model)

        await step_context.context.send_activity(f"Compra realizada com sucesso para o produto {product_id}!")

        return await step_context.end_dialog()



