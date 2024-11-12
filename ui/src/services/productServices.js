import * as APP from "../services/index";

export const productItemApi = APP.api("product", "item");
export const productCategoryApi = APP.api("product", "category");
export const productBrandApi = APP.api("product", "brand");
export const productVoucherApi = APP.api("product", "voucher");
export const productVoucherItemApi = APP.api("product", "voucher/item");
export const productSubCategoryApi = APP.api("product", "category/sub");
