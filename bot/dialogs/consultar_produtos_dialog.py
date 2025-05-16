from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions

class ConsultarProdutosDialog (ComponentDialog):
    def __init__(self):
        super(ConsultarProdutosDialog, self).__init__("ConsultarProdutosDialog")

        self.add_dialog(TextPrompt(TextPrompt.__name__))

        self.add_dialog(
            WaterfallDialog(
                "consultarProdutoWaterfall",
                [
                    self.product_name_step,
                    self.product_name_search_step,
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

        # Aqui você pode adicionar a lógica para buscar o produto pelo nome
        await step_context.context.send_activity(MessageFactory.text(f"Você está buscando o produto: {product_name}"))

        return await step_context.end_dialog()
