<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Sub Category list</h4>
      <h6>View/Search product Category</h6>
    </div>
    <div class="page-btn">
      <router-link
        class="btn btn-added"
        @click="navigateTo('/index/addsubcategory')"
        to="/index/addsubcategory"
      >
        <img src="/img/icons/plus.svg" class="me-2" alt="img" />
        Add Sub Category
      </router-link>
    </div>
  </div>
  <TableComponent
    :mainHeaders="headers"
    :mainItems="subcategories"
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
          <form @submit.prevent="saveAction">
            <div class="row">
              <div class="col-lg-4 col-sm-6 col-12">
                <div class="form-group">
                  <label>Parent Category</label>
                  <select
                    class="form-select"
                    v-model="subcategory.category"
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
              <div class="col-lg-4 col-sm-6 col-12">
                <div class="form-group">
                  <label>Name</label>
                  <input type="text" v-model="subcategory.name" />
                </div>
              </div>
              <div class="col-lg-4 col-sm-6 col-12">
                <div class="form-group">
                  <label>Code</label>
                  <input type="text" v-model="subcategory.code" />
                </div>
              </div>
              <div class="col-lg-12">
                <div class="form-group">
                  <label>Description</label>
                  <textarea
                    class="form-control"
                    v-model="subcategory.desc"
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
} from "@/services/productServices";
export default {
  components: {
    ToasterComponent,
    TableComponent,
  },
  data() {
    return {
      currentId: null,
      subcategory: {
        category: "",
        name: "",
        code: "",
        desc: "",
      },
      headers: [
        {
          label: "Subcategory",
          field: "name",
        },
        {
          label: "Parent Category",
          field: "category_data",
          identifier: "name",
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
      subcategories: [],
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
    async saveAction() {
      jQuery("#editModal").modal("toggle");
      await productSubCategoryApi.edit(this.currentId, this.subcategory);
      this.loadData();
    },
    async editAction(id) {
      jQuery("#editModal").modal("toggle");
      this.currentId = id;
      const response = await productSubCategoryApi.fetchOne(id);
      this.subcategory = {
        category: response.category,
        name: response.name,
        code: response.code,
        desc: response.desc,
      };
    },
    async loadData() {
      this.subcategories = await productSubCategoryApi.fetchAll();
    },
  },
  async mounted() {
    this.categories = await productCategoryApi.fetchAll();
    this.loadData();
  },
};
</script>
<style></style>
