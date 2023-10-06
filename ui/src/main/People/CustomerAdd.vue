<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Customer Management</h4>
      <h6>Add/Update Customer</h6>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <form @submit.prevent="addCustomer">
        <div class="row">
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Customer Name</label>
              <input type="text" v-model="name" required />
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Code</label>
              <input type="text" v-model="code" required />
            </div>
          </div>
          <div class="col-lg-4 col-sm-6 col-12">
            <div class="form-group">
              <label>Email</label>
              <input type="email" class="form-control" v-model="email" />
            </div>
          </div>
          <div class="col-lg-4 col-12">
            <div class="form-group">
              <label>Phone</label>
              <input type="text" v-model="phone" />
            </div>
          </div>
          <div class="col-lg-8 col-12">
            <div class="form-group">
              <label>Address</label>
              <input type="text" v-model="address" />
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
              @click="navigateTo('/index/customerlist')"
              to="/index/customerlist"
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
import { peopleCustomerApi } from "@/services/peopleServices";
export default {
  components: {
    ToasterComponent,
  },
  data() {
    return {
      name: "",
      code: "",
      desc: "",
      email: "",
      phone: "",
      address: "",
    };
  },
  methods: {
    resetValues() {
      this.name = "";
      this.code = "";
      this.desc = "";
      this.email = "";
      this.phone = "";
      this.address = "";
    },
    async addCustomer() {
      await peopleCustomerApi
        .filter({
          columnName: "name",
          columnKey: this.name,
        })
        .then(async (result) => {
          if (result.length > 0) {
            this.$refs.toast.showToast(
              "danger",
              "Customer with this name already exists."
            );
            this.resetValues();
          } else {
            await peopleCustomerApi
              .filter({
                columnName: "code",
                columnKey: this.code,
              })
              .then(async (result) => {
                if (result.length > 0) {
                  this.$refs.toast.showToast(
                    "danger",
                    "Customer with this code already exists."
                  );
                  this.resetValues();
                } else {
                  try {
                    const response = await peopleCustomerApi.add({
                      name: this.name,
                      code: this.code,
                      desc: this.desc,
                      email: this.email,
                      phone: this.phone,
                      address: this.address,
                    });

                    localStorage.setItem("savedPath", "/index/customerlist/");
                    this.$router.push(`/index/customerlist/`);
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
