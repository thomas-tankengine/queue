/*
    Copyright 2025 Camptocamp SA (https://www.camptocamp.com).
    License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
*/
import {Store, pyToJsModels} from "@mail/core/common/store_service";
import {patch} from "@web/core/utils/patch";

pyToJsModels["queue.job.batch"] = "QueueJobBatch";

patch(Store.prototype, {
    setup() {
        super.setup(...arguments);
        this.hasQueueJobBatchUserGroup = false;
        this.queueJobBatchCounterBusId = 0;
        this.queueJobBatchCounter = 0;
    },

    /** @override */
    initialize() {
        super.initialize(...arguments);
        if (this.self_user?.share === false) {
            this.fetchStoreData("systray_get_queue_job_batches");
        }
    },
});
