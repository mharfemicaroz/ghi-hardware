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
  <div class="tabs-set">
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button
          class="nav-link active"
          id="tab1-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab1"
          type="button"
          role="tab"
          aria-controls="tab1"
          aria-selected="true"
        >
          Available
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="tab2-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab2"
          type="button"
          role="tab"
          aria-controls="tab2"
          aria-selected="false"
        >
          For Pricing
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="tab3-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab3"
          type="button"
          role="tab"
          aria-controls="tab3"
          aria-selected="false"
        >
          Expiring
        </button>
      </li>
      <li class="nav-item" role="presentation">
        <button
          class="nav-link"
          id="tab4-tab"
          data-bs-toggle="tab"
          data-bs-target="#tab4"
          type="button"
          role="tab"
          aria-controls="tab4"
          aria-selected="false"
        >
          Unavailable
        </button>
      </li>
    </ul>
    <div class="tab-content" id="myTabContent">
      <div
        class="tab-pane fade show active"
        id="tab1"
        role="tabpanel"
        aria-labelledby="tab1-tab"
      >
        <TableComponent
          :mainHeaders="headers"
          :mainItems="filteredproducts"
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
        />
      </div>
      <div
        class="tab-pane fade"
        id="tab2"
        role="tabpanel"
        aria-labelledby="tab2-tab"
      >
        <TableComponent
          :mainHeaders="headers"
          :mainItems="
            filteredproducts.filter(
              (o) => o.status === 'open' && o.isRecentPurchased
            )
          "
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
        />
      </div>
      <div
        class="tab-pane fade"
        id="tab3"
        role="tabpanel"
        aria-labelledby="tab3-tab"
      >
        <TableComponent
          :mainHeaders="headers"
          :mainItems="filteredproducts.filter((o) => o.status === 'open')"
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
        />
      </div>
      <div
        class="tab-pane fade"
        id="tab4"
        role="tabpanel"
        aria-labelledby="tab4-tab"
      >
        <TableComponent
          :mainHeaders="headers"
          :mainItems="filteredproducts.filter((o) => o.status !== 'open')"
          :editable="false"
          :moreAction="true"
          :actionBtns="['Edit Product', 'View/Set Price']"
          @btn-action1="editAction"
          @btn-action2="viewPrice"
        />
      </div>
    </div>
  </div>
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
                    :min="product.minqty"
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
                    :min="product.sellingPrice"
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
  <div
    class="modal fade show"
    id="priceModal"
    tabindex="-1"
    role="dialog"
    aria-labelledby="priceModalLabel"
    style="display: none; padding-right: 17px"
    aria-modal="true"
  >
    <div class="modal-dialog modal-xl" role="document">
      <div class="modal-content" style="">
        <div class="modal-header">
          <h4 class="modal-title" id="priceModalLabel">Price Module</h4>
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
          <div class="row">
            <div class="col-lg-9 col-sm-6 col-12">
              <div
                class="table-responsive"
                style="
                  height: fit-content;
                  max-height: 300px;
                  overflow-y: auto;
                  overflow-x: hidden;
                "
              >
                <table class="table">
                  <thead>
                    <tr>
                      <th>Last Date Purchased</th>
                      <th>Price</th>
                      <th>Selling Price</th>
                      <th>Profit</th>
                      <th>Markup %</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="item of pricehistory">
                      <td>{{ item.created }}</td>
                      <td>{{ item.price }}</td>
                      <td>{{ item.sellingPrice }}</td>
                      <td>{{ item.difference }}</td>
                      <td>{{ item.percentage }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="col-lg-3 col-sm-6 col-12">
              <form id="priceForm" @submit.prevent="setPrice">
                <div class="row">
                  <div class="col-lg-12 float-md-right mb-0">
                    <div class="total-order mb-0 mt-0">
                      <ul>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.05).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 5%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.05).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.1).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 10%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.1).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.2).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 20%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.2).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.3).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 30%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.3).toFixed(2) }}
                          </h5>
                        </li>
                        <li
                          class="markup"
                          @click="
                            newprice = parseFloat(
                              (product.purchasePrice * 1.5).toFixed(2)
                            )
                          "
                        >
                          <h4>Markup @ 50%</h4>
                          <h5>
                            ₱{{ (product.purchasePrice * 1.5).toFixed(2) }}
                          </h5>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="row">
                  <div class="form-group">
                    <label>Price</label>
                    <input
                      type="number"
                      class="form-control"
                      :min="product.purchasePrice"
                      step="0.01"
                      v-model="newprice"
                      required
                    />
                  </div>
                </div>
                <div class="col-lg-12">
                  <button type="submit" class="btn btn-submit me-2">Set</button>
                  <a
                    href="javascript:void(0);"
                    class="btn btn-cancel"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  >
                    Cancel
                  </a>
                </div>
              </form>
            </div>
          </div>
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
import { purchaseItemApi } from "@/services/purchaseServices";
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
        latestPrice: 0,
      },
      headers: [
        {
          label: "",
          field: "checkbox",
          sortable: false,
        },
        {
          label: "Item",
          field: "name",
          sortable: true,
        },
        {
          label: "Category",
          field: "categoryName",
          sortable: true,
        },
        {
          label: "Sub-category",
          field: "subcategoryName",
          sortable: true,
        },
        {
          label: "Brand",
          field: "brandName",
          sortable: true,
        },
        {
          label: "SKU",
          field: "sku",
          sortable: true,
        },
        {
          label: "Qty",
          field: "qty",
          sortable: true,
        },
        {
          label: "Price",
          field: "price",
          sortable: true,
        },
        {
          label: "Description",
          field: "desc",
          sortable: true,
        },
        {
          label: "Created By",
          field: "author",
          sortable: true,
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      pricehistory: [],
      categories: [],
      subcategories: [],
      brands: [],
      products: [],
      imageFile: null,
      imageFileName: "",
      newprice: 0,
    };
  },
  computed: {
    filteredSubcategories() {
      return this.subcategories.filter((item) => {
        return item.category === this.product.category;
      });
    },
    filteredproducts() {
      return this.products
        .map((o) => {
          const categoryName = o.category_data.name;
          const subcategoryName = o.subcategory_data.name;
          const brandName =
            o.brand_data !== null ? o.brand_data.name : "No Brand";
          return {
            ...o,
            categoryName: categoryName,
            subcategoryName: subcategoryName,
            brandName: brandName,
          };
        })
        .sort((a, b) => {
          return b.isRecentPurchased - a.isRecentPurchased;
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
    getBadgeClass(status) {
      return {
        "bg-lightgreen": status === true || status === "open",
        "bg-lightred": status === false || status === "close",
      };
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
      this.latestPrice = 0;
    },
    async setPrice() {
      jQuery("#priceModal").modal("toggle");
      this.product.price = this.newprice;
      this.product.isRecentPurchased = false;
      await productItemApi.edit(this.productId, this.product);
      const data = await purchaseItemApi.filter({
        columnName: "product_id",
        columnKey: this.productId,
      });
      const purchasedata = data.sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      })[0];
      const purchaseItemID = purchasedata.id;
      await purchaseItemApi.edit(purchaseItemID, {
        ...purchasedata,
        sellingPrice: this.newprice,
      });
      this.loadData();
    },
    async viewPrice(id) {
      const response = await productItemApi.fetchOne(id);
      this.product = {
        id: response.id,
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
      const purchasedata = (
        await purchaseItemApi.filter({
          columnName: "product_id",
          columnKey: id,
        })
      ).sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      });
      if (purchasedata.length > 0) {
        jQuery("#priceModal").modal("toggle");
        this.newprice = parseFloat(this.product.price);
        this.productId = id;
        this.product.purchasePrice = purchasedata[0].price;
        this.pricehistory = purchasedata.map((o) => {
          const difference = parseFloat(o.sellingPrice) - parseFloat(o.price);
          const percentage =
            Math.round(
              ((parseFloat(o.sellingPrice) - parseFloat(o.price)) /
                parseFloat(o.price)) *
                10000
            ) / 100;
          return {
            ...o,
            difference: difference < 0 ? "-" : difference,
            percentage: isNaN(percentage)
              ? "-"
              : percentage < 0
              ? "-"
              : percentage,
          };
        });
      } else {
        this.pricehistory = [];
        this.$refs.toast.showToast(
          "warning",
          "This product has no recent purchases."
        );
      }
    },
    async saveAction() {
      jQuery("#editModal").modal("toggle");
      await productItemApi.edit(this.productId, this.product);
      this.loadData();
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.productId = id;
      const result = (
        await purchaseItemApi.filter({
          columnName: "product_id",
          columnKey: id,
        })
      ).sort((a, b) => {
        return new Date(b.created) - new Date(a.created);
      });
      const latestPrice = result.length > 0 ? result[0].sellingPrice : 0;
      const response = await productItemApi.fetchOne(id);
      this.product = {
        id: response.id,
        name: response.name,
        desc: response.desc,
        unit: response.unit,
        sku: response.sku,
        minqty: response.minqty,
        qty: response.qty,
        tax: response.tax,
        discount: response.discount,
        price: response.price,
        sellingPrice: latestPrice,
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
<style scoped>
.markup {
  cursor: pointer;
}
</style>
