<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Brand List</h4>
      <h6>Manage your Brand</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/addbrand')"
        to="/index/addbrand"
      >
        <img src="/img/icons/plus.svg" class="me-1" alt="img" />Add Brand
      </router-link>
    </div>
  </div>
  <TableComponent
    :mainHeaders="headers"
    :mainItems="brands"
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
          <h4 class="modal-title" id="editModalLabel">Edit Brand</h4>
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
            <div class="col-lg-6 col-sm-6 col-12">
              <div class="form-group">
                <label>Name</label>
                <input type="text" v-model="brand.name" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group">
                <label>Description</label>
                <textarea class="form-control" v-model="brand.desc"></textarea>
              </div>
            </div>
            <div class="col-lg-12">
              <a
                href="javascript:void(0);"
                @click="saveAction"
                class="btn btn-submit me-2"
                >Submit</a
              >
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
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ToasterComponent from "../../common/ToasterComponent.vue";
import TableComponent from "../../common/TableComponent.vue";
import { productBrandApi } from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      currentId: null,
      brand: {
        name: "",
        desc: "",
      },
      headers: [
        {
          label: "Brand Name",
          field: "name",
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
          label: "",
          field: "action",
          sortable: false,
        },
      ],
      brands: [],
    };
  },
  methods: {
    navigateTo(path, propSidebar = true) {
      // Adding a unique timestamp as a query parameter to force reload

      // Saving path to localStorage
      const isSidebar = propSidebar || true;
      localStorage.setItem("savedPath", path);
      localStorage.setItem("propSidebar", isSidebar);
      this.$router.push(path);
    },
    async loadData() {
      const response = await productBrandApi.fetchAll();
      this.brands = response;
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.currentId = id;
      const response = await productBrandApi.fetchOne(id);
      this.brand = {
        name: response.name,
        desc: response.desc,
      };
    },
    async saveAction(id) {
      jQuery("#editModal").modal("toggle");
      await productBrandApi.edit(this.currentId, this.brand);
      this.loadData();
    },
  },
  async created() {
    this.loadData();
  },
};
</script>
<style></style>
