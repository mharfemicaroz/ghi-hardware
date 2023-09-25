<template>
  <div class="page-header">
    <div class="page-title">
      <h4>Product Edit Category</h4>
      <h6>Edit a product Category</h6>
    </div>
  </div>

  <div class="card">
    <div class="card-body">
      <div class="row">
        <div class="col-lg-6 col-sm-6 col-12">
          <div class="form-group">
            <label>Category Name</label>
            <input type="text" value="Computers" />
          </div>
        </div>
        <div class="col-lg-6 col-sm-6 col-12">
          <div class="form-group">
            <label>Category Code</label>
            <input type="text" value="CT001" />
          </div>
        </div>
        <div class="col-lg-12">
          <div class="form-group">
            <label>Description</label>
            <textarea class="form-control">Computers Description</textarea>
          </div>
        </div>
        <div class="col-lg-12">
          <a href="javascript:void(0);" class="btn btn-submit me-2">Submit</a>
          <router-link
            class="btn btn-cancel"
            @click="navigateTo('/index/categorylist')"
            to="/index/categorylist"
          >
            Cancel
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
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
