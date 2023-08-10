<template>
    <div class="page-header">
        <div class="page-title">
            <h4>Product Add sub Category</h4>
            <h6>Create new product Category</h6>
        </div> 
    </div>

    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-lg-4 col-sm-6 col-12">
                    <div class="form-group">
                        <label>Parent Category</label>
                        <select class="select">
                            <option>Choose Category</option>
                            <option>Category</option>
                        </select>
                    </div>
                </div>
                <div class="col-lg-4 col-sm-6 col-12">
                    <div class="form-group">
                        <label>Category Name</label>
                        <input type="text">
                    </div>
                </div>
                <div class="col-lg-4 col-sm-6 col-12">
                    <div class="form-group">
                        <label>Category Code</label>
                        <input type="text">
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="form-group">
                        <label>Description</label>
                        <textarea class="form-control"></textarea>
                    </div>
                </div>
                <div class="col-lg-12">
                    <a href="javascript:void(0);" class="btn btn-submit me-2">Submit</a>
                    <router-link class="btn btn-cancel" @click="navigateTo('/index/subcategorylist')" to="/index/subcategorylist">
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
            localStorage.setItem('savedPath', path);
            localStorage.setItem('propSidebar', isSidebar);
            this.$router.go(0);
        },
    }
}
</script>
<style></style>