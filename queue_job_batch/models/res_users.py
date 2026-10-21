# Copyright 2025 Camptocamp SA (https://www.camptocamp.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class Users(models.Model):
    _name = "res.users"
    _inherit = ["res.users"]

    def _store_init_global_fields(self, res):
        super()._store_init_global_fields(res)
        res.attr(
            "hasQueueJobBatchUserGroup",
            lambda u: u.has_group("queue_job_batch.group_queue_job_batch_user"),
        )

    def _get_queue_job_batches(self):
        # See :meth:`controllers.webclient.WebClient.store_get_queue_job_batches`
        self.ensure_one()
        return self.env["queue.job.batch"].search(
            [
                ("user_id", "=", self.id),
                ("is_read", "=", False),
            ]
        )
