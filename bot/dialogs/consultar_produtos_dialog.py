from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class ConsultarProdutoDialog(ComponentDialog):
    def __init__(self):
        super(ConsultarProdutoDialog, self).__init__("ConsultarProdutoDialog")

        self.add_dialog(
            WaterfallDialog(
                "ConsultarProdutoWaterfallDialog",
                [
                    self.prompt_option_step,
                ],
            )
        )

        self.initial_dialog_id = "ConsultarProdutoWaterfallDialog"

    async def prompt_option_step(self, step_context: WaterfallStepContext) :
        await step_context.context.send_activity("Você está no consultar produtos.")
        return await step_context.end_dialog()

