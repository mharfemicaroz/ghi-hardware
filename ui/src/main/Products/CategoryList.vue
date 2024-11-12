<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Category list</h4>
      <h6>View/Search product Category</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/addcategory')"
        to="/index/addcategory"
      >
        <img src="/img/icons/plus.svg" class="me-1" alt="img" />Add Category
      </router-link>
    </div>
  </div>
  <TableComponent
    :mainHeaders="headers"
    :mainItems="categories"
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
          <h4 class="modal-title" id="editModalLabel">Edit Category</h4>
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
                <label>Category Name</label>
                <input type="text" v-model="category.name" />
              </div>
            </div>
            <div class="col-lg-6 col-sm-6 col-12">
              <div class="form-group">
                <label>Category Code</label>
                <input type="text" v-model="category.code" />
              </div>
            </div>
            <div class="col-lg-12">
              <div class="form-group">
                <label>Description</label>
                <textarea
                  class="form-control"
                  v-model="category.desc"
                ></textarea>
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
import { productCategoryApi } from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      currentId: null,
      category: {
        name: "",
        code: "",
        desc: "",
      },
      headers: [
        {
          label: "Category Name",
          field: "name",
        },
        {
          label: "Category Code",
          field: "code",
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
      categories: [],
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
      const response = await productCategoryApi.fetchAll();
      this.categories = response;
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.currentId = id;
      const response = await productCategoryApi.fetchOne(id);
      this.category = {
        name: response.name,
        code: response.code,
        desc: response.desc,
      };
    },
    async saveAction() {
      jQuery("#editModal").modal("toggle");
      await productCategoryApi.edit(this.currentId, this.category);
      this.loadData();
    },
  },
  async created() {
    this.loadData();
  },
};
</script>
<style></style>
