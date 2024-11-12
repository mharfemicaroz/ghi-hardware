<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Add sub Category</h4>
      <h6>Create new product Category</h6>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <form @submit.prevent="addSubCategory">
        <div class="row">
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Parent Category</label>
              <select class="form-select" v-model="category" required>
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
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Subcategory Name</label>
              <input type="text" required v-model="name" />
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Subcategory Code</label>
              <input type="text" required v-model="code" />
            </div>
          </div>
          <div class="col-lg-12">
            <div class="form-group">
              <label>Description</label>
              <textarea class="form-control" v-model="desc"></textarea>
            </div>
          </div>
          <div class="col-lg-12">
            <button type="submit" class="btn btn-submit me-2">Submit</button>
            <router-link
              class="btn btn-cancel"
              @click="navigateTo('/index/subcategorylist')"
              to="/index/subcategorylist"
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
} from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      categories: [],
      category: null,
      name: "",
      code: "",
      desc: "",
    };
  },
  methods: {
    resetValues() {
      this.category = null;
      this.name = "";
      this.code = "";
      this.desc = "";
    },
    async addSubCategory() {
      await productSubCategoryApi
        .filter({
          columnName: "name",
          columnKey: this.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Product subcategory with this name already exists."
            );
            this.resetValues();
          } else {
            await productSubCategoryApi
              .filter({
                columnName: "code",
                columnKey: this.code,
              })
              .then(async (result) => {
                if (result.length > 0) {
                  this.$refs.toast.showToast(
                    "danger",
                    "Product subcategory with this code already exists."
                  );
                  this.resetValues();
                } else {
                  try {
                    const response = await productSubCategoryApi.add({
                      category: this.category,
                      name: this.name,
                      code: this.code,
                      desc: this.desc,
                    });

                    localStorage.setItem(
                      "savedPath",
                      "/index/subcategorylist/"
                    );
                    this.$router.push(`/index/subcategorylist/`);
                  } catch (error) {
                    console.error(error);
                  }
                }
              });
          }
        });
    },
    async loaddata() {
      await productCategoryApi.fetchAll().then(async (result) => {
        this.categories = result;
      });
    },
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.push(path);
    },
  },
  mounted() {
    this.loaddata();
  },
};
</script>
<style></style>
