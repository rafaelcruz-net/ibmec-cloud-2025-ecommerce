from botbuilder.dialogs import ComponentDialog, WaterfallDialog, WaterfallStepContext
from botbuilder.core import MessageFactory

class ConsultarPedidosDialog (ComponentDialog):
    def __init__(self):
        super(ConsultarPedidosDialog, self).__init__("ConsultarPedidosDialog")

        self.add_dialog(
            WaterfallDialog(
                "consultarPedidoWaterfall",
                [
                    self.product_name_step,
                ],
            )
        )


        self.initial_dialog_id = "consultarPedidoWaterfall"

    async def product_name_step(self, step_context: WaterfallStepContext):
        await step_context.context.send_activity(MessageFactory.text("Você escolheu a opção de Consultar Pedidos."))
        return await step_context.end_dialog()
        
