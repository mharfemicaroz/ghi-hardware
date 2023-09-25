<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product List</h4>
      <h6>Manage your products</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/addproduct')"
        to="/index/addproduct"
      >
        <img src="/img/icons/plus.svg" alt="img" class="me-1" />Add New Product
      </router-link>
    </div>
  </div>
  <TableComponent
    :mainHeaders="headers"
    :mainItems="products"
    :editable="true"
    @edit-action="editAction"
  />
  <ToasterComponent ref="toast" />
  <div
    class="modal fade show"
    id="editModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="editModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-lg" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="editModalLabel">Edit Product</h4>
          <button
            type="button"
            class="close"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="saveAction">
            <div class="row">
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Product Name</label>
                  <input type="text" v-model="product.name" required />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Category</label>
                  <select
                    class="form-select"
                    v-model="product.category"
                    @change="toggleSelect"
                    required
                  >
                    <option
                      v-for="(item, index) in categories"
                      :key="index"
                      :value="item.id"
                    >
                      {{ item.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Sub Category</label>
                  <select
                    v-if="filteredSubcategories.length > 0"
                    class="form-select"
                    v-model="product.subcategory"
                    required
                  >
                    <option
                      v-for="(item, index) in filteredSubcategories"
                      :key="index"
                      :value="item.id"
                    >
                      {{ item.name }}
                    </option>
                  </select>
                  <input
                    v-else
                    type="text"
                    value="Not Available"
                    class="form-control"
                    readonly
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Brand</label>
                  <select class="form-select" v-model="product.brand">
                    <option value="">No Brand</option>
                    <option
                      v-for="(item, index) in brands"
                      :key="index"
                      :value="item.id"
                    >
                      {{ item.name }}
                    </option>
                  </select>
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Unit</label>
                  <select class="form-select" v-model="product.unit" required>
                    <option value="pc">Piece</option>
                    <option value="kg">Kilogram</option>
                    <option value="m">Meter</option>
                    <option value="sqm">Square Meter</option>
                    <option value="cum">Cubic Meter</option>
                    <option value="qty">Quantity</option>
                  </select>
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>SKU</label>
                  <input type="text" v-model="product.sku" required />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Minimum Qty</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    step="1"
                    required
                    v-model="product.minqty"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Quantity</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    required
                    step="1"
                    v-model="product.qty"
                  />
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Description</label>
                  <textarea
                    class="form-control"
                    v-model="product.desc"
                  ></textarea>
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Tax</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    required
                    step="0.01"
                    v-model="product.tax"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Discount</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    required
                    step="0.01"
                    v-model="product.discount"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label>Price</label>
                  <input
                    type="number"
                    class="form-control"
                    min="0"
                    required
                    step="0.01"
                    v-model="product.price"
                  />
                </div>
              </div>
              <div class="col-lg-3 col-sm-6 col-12">
                <div class="form-group">
                  <label> Status</label>
                  <select class="form-select" v-model="product.status" required>
                    <option value="closed">Closed</option>
                    <option value="open">Open</option>
                  </select>
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label> {{ imageFileName }}</label>
                  <div class="image-upload">
                    <input type="file" id="image" @change="handleImageUpload" />
                    <div class="image-uploads">
                      <img src="/img/icons/upload.svg" alt="img" />
                      <h4>Drag and drop a file to upload</h4>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-12">
                <button type="submit" class="btn btn-submit me-2">
                  Submit
                </button>
                <a
                  href="javascript:void(0);"
                  class="btn btn-cancel"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                >
                  Cancel
                </a>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import TableComponent from "../../common/TableComponent.vue";
import {
  productSubCategoryApi,
  productCategoryApi,
  productBrandApi,
  productItemApi,
} from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      productId: null,
      product: {
        category: "",
        subcategory: "",
        brand: "",
        name: "",
        desc: "",
        unit: "",
        sku: "",
        minqty: 0,
        qty: 0,
        tax: 0,
        discount: 0,
        price: 0,
        status: "",
      },
      headers: [
        {
          label: "Item",
          field: "name",
        },
        {
          label: "Category",
          field: "category_data",
          identifier: "name",
        },
        {
          label: "Sub-category",
          field: "subcategory_data",
          identifier: "name",
        },
        {
          label: "Brand",
          field: "brand_data",
          identifier: "name",
        },
        {
          label: "SKU",
          field: "sku",
        },
        {
          label: "Qty",
          field: "qty",
        },
        {
          label: "Price",
          field: "price",
        },
        {
          label: "Description",
          field: "desc",
        },
        {
          label: "Created By",
          field: "author",
        },
        {
          label: "Status",
          field: "status",
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      categories: [],
      subcategories: [],
      brands: [],
      products: [],
      imageFile: null,
      imageFileName: "",
    };
  },
  computed: {
    filteredSubcategories() {
      return this.subcategories.filter((item) => {
        return item.category === this.product.category;
      });
    },
  },
  methods: {
    toggleSelect() {
      if (this.filteredSubcategories.length === 0) {
        this.subcategory = null;
      }
    },
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.go(0);
    },
    resetValues() {
      this.category = "";
      this.subcategory = "";
      this.brand = "";
      this.name = "";
      this.desc = "";
      this.unit = "";
      this.sku = "";
      this.minqty = 0;
      this.qty = 0;
      this.tax = 0;
      this.discount = 0;
      this.price = 0;
      this.status = "";
      this.imageFile = null;
      this.imageFileName = "";
    },
    async saveAction() {
      jQuery("#editModal").modal("toggle");
      await productItemApi.edit(this.productId, this.product);
      this.loadData();
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.productId = id;
      const response = await productItemApi.fetchOne(id);
      this.product = {
        name: response.name,
        desc: response.desc,
        unit: response.unit,
        sku: response.sku,
        minqty: response.minqty,
        qty: response.qty,
        tax: response.tax,
        discount: response.discount,
        price: response.price,
        status: response.status,
        category: response.category,
        subcategory: response.subcategory || "",
        brand: response.brand || "",
      };
    },
    async loadData() {
      this.products = await productItemApi.fetchAll();
    },
  },
  async mounted() {
    this.categories = await productCategoryApi.fetchAll();
    this.subcategories = await productSubCategoryApi.fetchAll();
    this.brands = await productBrandApi.fetchAll();
    this.loadData();
  },
};
</script>
<style></style>
