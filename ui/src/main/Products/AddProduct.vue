<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Add</h4>
      <h6>Create new product</h6>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <form @submit.prevent="addProduct">
        <div class="row">
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Product Name</label>
              <input type="text" v-model="name" required />
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Category</label>
              <select
                class="form-select"
                v-model="category"
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
                v-model="subcategory"
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
              <select class="form-select" v-model="brand">
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
              <select class="form-select" v-model="unit" required>
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
              <input type="text" v-model="sku" required />
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
                v-model="minqty"
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
                v-model="qty"
              />
            </div>
          </div>
          <div class="col-lg-12">
            <div class="form-group">
              <label>Description</label>
              <textarea class="form-control" v-model="desc"></textarea>
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
                v-model="tax"
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
                v-model="discount"
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
                v-model="price"
              />
            </div>
          </div>
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label> Status</label>
              <select class="form-select" v-model="status" required>
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
            <button type="submit" class="btn btn-submit me-2">Submit</button>
            <router-link
              class="btn btn-cancel"
              @click="navigateTo('/index/productlist')"
              to="/index/productlist"
            >
              Cancel
            </router-link>
          </div>
        </div>
      </form>
    </div>
  </div>
  <ToasterComponent ref="toast" />
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import {
  productSubCategoryApi,
  productCategoryApi,
  productBrandApi,
  productItemApi,
} from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      categories: [],
      subcategories: [],
      brands: [],
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
      imageFile: null,
      imageFileName: "",
    };
  },
  computed: {
    filteredSubcategories() {
      return this.subcategories.filter((item) => {
        return item.category === this.category;
      });
    },
  },
  methods: {
    toggleSelect() {
      if (this.filteredSubcategories.length === 0) {
        this.subcategory = null;
      }
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
    async addProduct() {
      await productItemApi
        .filter({
          columnName: "name",
          columnKey: this.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Product item with this name already exists."
            );
            this.resetValues();
          } else {
            await productItemApi
              .filter({
                columnName: "sku",
                columnKey: this.sku,
              })
              .then(async (result) => {
                if (result.length > 0) {
                  this.$refs.toast.showToast(
                    "danger",
                    "Product item with this sku code already exists."
                  );
                  this.resetValues();
                } else {
                  try {
                    const response = await productItemApi.add({
                      category: this.category,
                      subcategory: this.subcategory,
                      brand: this.brand,
                      name: this.name,
                      desc: this.desc,
                      unit: this.unit,
                      sku: this.sku,
                      minqty: this.minqty,
                      qty: this.qty,
                      tax: this.tax,
                      discount: this.discount,
                      price: this.price,
                      status: this.status,
                    });

                    localStorage.setItem("savedPath", "/index/productlist/");
                    this.$router.push(`/index/productlist/`);
                    setTimeout(() => {
                      this.$router.go(0);
                    }, 1);
                  } catch (error) {
                    console.error(error);
                  }
                }
              });
          }
        });
    },
    async loaddata() {
      this.categories = await productCategoryApi.fetchAll();
      this.subcategories = await productSubCategoryApi.fetchAll();
      this.brands = await productBrandApi.fetchAll();
    },
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.go(0);
    },
  },
  mounted() {
    this.loaddata();
  },
};
</script>
<style></style>
