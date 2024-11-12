<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Add Voucher</h4>
      <h6>Create new product Voucher</h6>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <form @submit.prevent="addVoucher">
        <div class="row">
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Voucher Name</label>
              <input type="text" v-model="name" required />
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Mode</label>
              <select
                class="form-control"
                @change="toggleSelect"
                v-model="mode"
                required
              >
                <option value="0">Percentage-Based Discount</option>
                <option value="1">Fixed Amount Discount</option>
                <option value="2">Special Offer Price</option>
              </select>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>{{
                mode == 0
                  ? "Percentage"
                  : mode == 1
                  ? "Fixed Amount"
                  : "Special Price"
              }}</label>
              <input
                v-if="mode == 0"
                type="number"
                class="form-control"
                min="0"
                step="0.01"
                max="100"
                v-model="discountPercentage"
                required
              />
              <input
                v-else-if="mode == 1"
                type="number"
                class="form-control"
                min="0"
                step="0.01"
                v-model="discount"
                required
              />
              <input
                v-else-if="mode == 2"
                type="number"
                class="form-control"
                min="0"
                step="0.01"
                v-model="specialPrice"
                required
              />
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Start Date </label>
              <div class="input-groupicon">
                <input
                  type="date"
                  class="form-control"
                  v-model="startDate"
                  required
                />
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Expiration Date </label>
              <div class="input-groupicon">
                <input
                  type="date"
                  class="form-control"
                  v-model="expirationDate"
                  required
                />
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Description</label>
              <input type="text" v-model="desc" required />
            </div>
          </div>
          <div class="col-lg-12">
            <button type="submit" class="btn btn-submit me-2">Submit</button>
            <router-link
              class="btn btn-cancel"
              @click="navigateTo('/index/voucherlist')"
              to="/index/voucherlist"
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
import { productVoucherApi } from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      name: "",
      desc: "",
      mode: 0,
      discountPercentage: 0,
      discount: 0,
      specialPrice: 0,
      startDate: "",
      expirationDate: "",
    };
  },
  methods: {
    resetValues() {
      this.name = "";
      this.desc = "";
      this.discountPercentage = 0;
      this.percentage = 0;
      this.specialPrice = 0;
      this.expirationDate = "";
      this.startDate = "";
    },
    toggleSelect() {
      this.discountPercentage = 0;
      this.percentage = 0;
      this.specialPrice = 0;
    },
    async addVoucher() {
      await productVoucherApi
        .filter({
          columnName: "name",
          columnKey: this.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Product voucher with this name already exists."
            );
            this.resetValues();
          } else {
            if (new Date(this.expirationDate) < new Date(this.startDate)) {
              this.$refs.toast.showToast(
                "danger",
                "Expiration date must not be before the start date."
              );
              this.expirationDate = "";
              return false;
            }
            try {
              const response = await productVoucherApi.add({
                name: this.name,
                desc: this.desc,
                mode: this.mode,
                discountPercentage: this.discountPercentage,
                percentage: this.percentage,
                specialPrice: this.specialPrice,
                startDate: this.startDate,
                expirationDate: this.expirationDate,
              });

              localStorage.setItem("savedPath", "/index/voucherlist/");
              this.$router.push(`/index/voucherlist/`);
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
      this.$router.push(path);
    },
  },
};
</script>
<style></style>
