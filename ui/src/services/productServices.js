import * as APP from "../services/index";

const api = (resource) => {
  const URL = `product/${resource}/`;

  return {
    fetchAll: async () => APP.fetchAllItems(URL),
    fetchOne: async (id) => APP.fetchItem(URL, id),
    add: async (data) => APP.addItem(URL, data),
    edit: async (id, data) => APP.editItem(URL, id, data),
    delete: async (id) => APP.deleteItem(URL, id),
    filter: async (data) => APP.filterItems(URL, data),
  };
};

export const productItemApi = api("item");
export const productCategoryApi = api("category");
export const productBrandApi = api("brand");
export const productSubCategoryApi = api("category/sub");

export const saveImageProductCategory = async (data) => {
  return APP.saveImage(data);
};
