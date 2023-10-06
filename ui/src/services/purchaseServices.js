import * as APP from "./index";

export const purchaseOrderApi = APP.api("purchase", "order");
export const purchaseItemApi = APP.api("purchase", "items");
export const purchaseTransactionApi = APP.api("purchase", "transact");
