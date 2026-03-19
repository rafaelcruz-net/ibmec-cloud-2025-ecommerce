from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions


class ConsultarProdutoDialog(ComponentDialog):
    def __init__(self):
        super(ConsultarProdutoDialog, self).__init__("ConsultarProdutoDialog")

        self.add_dialog(TextPrompt(TextPrompt.__name__))

        self.add_dialog(
            WaterfallDialog(
                "consultarProdutoWaterfallDialog",
                [
                    self.product_name_step,
                    self.prompt_process_product_name_step,
                ],
            )
        )


        self.initial_dialog_id = "consultarProdutoWaterfallDialog"

    async def product_name_step(self, step_context: WaterfallStepContext) :
                
        prompt_message = MessageFactory.text("Por favor, digite o nome do produto que você deseja consultar.")
        
        prompt_option = PromptOptions(
            prompt=prompt_message,
            retry_prompt=MessageFactory.text("Desculpe, não consegui entender. Por favor, digite o nome do produto novamente."),
        )

        return await step_context.prompt(TextPrompt.__name__, prompt_option)
    
    async def prompt_process_product_name_step(self, step_context: WaterfallStepContext) :
        product_name = step_context.result
        # Aqui você pode adicionar a lógica para consultar o produto usando o nome fornecido
        return await step_context.end_dialog()
    


