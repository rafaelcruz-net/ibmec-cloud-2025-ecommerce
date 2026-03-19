from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class ExtratoCompraDialog(ComponentDialog):
    def __init__(self):
        super(ExtratoCompraDialog, self).__init__("ExtratoCompraDialog")

        self.add_dialog(
            WaterfallDialog(
                "ExtratoCompraWaterfallDialog",
                [
                    self.prompt_option_step,
                ],
            )
        )

        self.initial_dialog_id = "ExtratoCompraWaterfallDialog"

    async def prompt_option_step(self, step_context: WaterfallStepContext) :
        await step_context.context.send_activity("Você está consultando o extrato de compras.")
        return await step_context.end_dialog()

