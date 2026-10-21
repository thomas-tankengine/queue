# Copyright 2025 Camptocamp SA (https://www.camptocamp.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.http import request

from odoo.addons.mail.controllers.webclient import WebclientController
from odoo.addons.mail.tools.store_handler import store_handler


class WebClient(WebclientController):
    @store_handler("systray_get_queue_job_batches")
    def store_get_queue_job_batches(self, store):
        # sudo: bus.bus: reading non-sensitive last id
        bus_last_id = request.env["bus.bus"].sudo()._bus_last_id()
        batches = request.env.user._get_queue_job_batches()
        store.add(batches, "_store_batch_fields")
        store.add_global_values(
            queueJobBatchCounter=len(batches),
            queueJobBatchCounterBusId=bus_last_id,
        )
