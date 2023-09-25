<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Add Brand</h4>
      <h6>Create new product Brand</h6>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <form @submit.prevent="addBrand">
        <div class="row">
          <div class="col-lg-3 col-sm-6 col-12">
            <div class="form-group">
              <label>Brand Name</label>
              <input type="text" v-model="name" required />
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
              @click="navigateTo('/index/brandlist')"
              to="/index/brandlist"
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
import { productBrandApi } from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      name: "",
      desc: "",
    };
  },
  methods: {
    resetValues() {
      this.name = "";
      this.desc = "";
    },
    async addBrand() {
      await productBrandApi
        .filter({
          columnName: "name",
          columnKey: this.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Product brand with this name already exists."
            );
            this.resetValues();
          } else {
            try {
              const response = await productBrandApi.add({
                name: this.name,
                desc: this.desc,
              });

              localStorage.setItem("savedPath", "/index/brandlist/");
              this.$router.push(`/index/brandlist/`);
              setTimeout(() => {
                this.$router.go(0);
              }, 1);
            } catch (error) {
              console.error(error);
            }
          }
        });
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
};
</script>
<style></style>
