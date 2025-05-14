from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory
from botbuilder.dialogs.prompts import TextPrompt, PromptOptions


class ConsultarProdutoDialog(ComponentDialog):
    def __init__(self):
        super(ConsultarProdutoDialog, self).__init__("ConsultarProdutoDialog")

        self.add_dialog(TextPrompt("namePrompt"))

        self.add_dialog(
            WaterfallDialog(
                "ConsultarProdutoWaterfallDialog",
                [
                    self.product_name_step,
                    self.prompt_process_product_name_step,
                ],
            )
        )


        self.initial_dialog_id = "ConsultarProdutoWaterfallDialog"

    async def product_name_step(self, step_context: WaterfallStepContext) :
                
        prompt_message = MessageFactory.text("Por favor, digite o nome do produto que você deseja consultar.")
        
        return await step_context.prompt(
            "namePrompt",
            PromptOptions(prompt=MessageFactory.text("Digite seu nome:"))
        )
    
    async def prompt_process_product_name_step(self, step_context: WaterfallStepContext) :
        product_name = step_context.result
        # Aqui você pode adicionar a lógica para consultar o produto usando o nome fornecido
        return await step_context.end_dialog()
    


