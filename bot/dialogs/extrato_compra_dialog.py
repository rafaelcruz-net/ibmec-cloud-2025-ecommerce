from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class ExtratoCompraDialog (ComponentDialog):
    def __init__(self):
        super(ExtratoCompraDialog, self).__init__("ExtratoCompraDialog")

        self.add_dialog(
            WaterfallDialog(
                "extratoCompraWaterfall",
                [
                    self.product_name_step,
                ],
            )
        )


        self.initial_dialog_id = "extratoCompraWaterfall"

    async def product_name_step(self, step_context: WaterfallStepContext):
        await step_context.context.send_activity(MessageFactory.text("Você escolheu a opção de Extrato de Compras."))
        return await step_context.end_dialog()
        
