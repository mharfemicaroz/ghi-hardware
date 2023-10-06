<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Customer List</h4>
      <h6>Manage your Customer</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/customeradd')"
        to="/index/customeradd"
      >
        <img src="/img/icons/plus.svg" class="me-1" alt="img" />Add Brand
      </router-link>
    </div>
  </div>
  <TableComponent
    :mainHeaders="headers"
    :mainItems="customers"
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
          <h4 class="modal-title" id="editModalLabel">Edit Customer Info</h4>
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
              <div class="col-lg-4 col-sm-6 col-12">
                <div class="form-group">
                  <label>Customer Name</label>
                  <input type="text" v-model="customer.name" required />
                </div>
              </div>
              <div class="col-lg-4 col-sm-6 col-12">
                <div class="form-group">
                  <label>Code</label>
                  <input type="text" v-model="customer.code" required />
                </div>
              </div>
              <div class="col-lg-4 col-sm-6 col-12">
                <div class="form-group">
                  <label>Email</label>
                  <input
                    type="email"
                    class="form-control"
                    v-model="customer.email"
                  />
                </div>
              </div>
              <div class="col-lg-4 col-12">
                <div class="form-group">
                  <label>Phone</label>
                  <input type="text" v-model="customer.phone" />
                </div>
              </div>
              <div class="col-lg-8 col-12">
                <div class="form-group">
                  <label>Address</label>
                  <input type="text" v-model="customer.address" />
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Description</label>
                  <textarea
                    class="form-control"
                    v-model="customer.desc"
                  ></textarea>
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
import { peopleCustomerApi } from "@/services/peopleServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      currentId: null,
      customer: {
        name: "",
        code: "",
        desc: "",
        email: "",
        phone: "",
        address: "",
      },
      headers: [
        {
          label: "Name",
          field: "name",
        },
        {
          label: "Code",
          field: "code",
        },
        {
          label: "Description",
          field: "desc",
        },
        {
          label: "Email",
          field: "email",
        },
        {
          label: "Phone",
          field: "phone",
        },
        {
          label: "Address",
          field: "address",
        },
        {
          label: "Created By",
          field: "author",
        },
        {
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      customers: [],
    };
  },
  async created() {
    this.loadData();
  },
  methods: {
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.go(0);
    },
    async loadData() {
      this.customers = await peopleCustomerApi.fetchAll();
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.currentId = id;
      const response = await peopleCustomerApi.fetchOne(id);
      this.customer = {
        name: response.name,
        desc: response.desc,
        code: response.code,
        email: response.email,
        phone: response.phone,
        address: response.address,
      };
    },
    async saveAction(id) {
      jQuery("#editModal").modal("toggle");
      await peopleCustomerApi.edit(this.currentId, this.customer);
      this.loadData();
    },
  },
};
</script>
<style></style>
