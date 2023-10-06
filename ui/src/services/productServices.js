import * as APP from "../services/index";

export const productItemApi = APP.api("product", "item");
export const productCategoryApi = APP.api("product", "category");
export const productBrandApi = APP.api("product", "brand");
export const productSubCategoryApi = APP.api("product", "category/sub");
