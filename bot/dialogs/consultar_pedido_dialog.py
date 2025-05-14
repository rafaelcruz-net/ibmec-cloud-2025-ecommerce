from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class ConsultarPedidoDialog(ComponentDialog):
    def __init__(self):
        super(ConsultarPedidoDialog, self).__init__("ConsultarPedidoDialog")

        self.add_dialog(
            WaterfallDialog(
                "ConsultarPedidoWaterfallDialog",
                [
                    self.prompt_option_step,
                ],
            )
        )

        self.initial_dialog_id = "ConsultarPedidoWaterfallDialog"

    async def prompt_option_step(self, step_context: WaterfallStepContext) :
        await step_context.context.send_activity("Você está consultando o pedido.")
        return await step_context.end_dialog()

