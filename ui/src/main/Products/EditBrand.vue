<template>
    <div class="page-header">
        <div class="page-title">
            <h4>Brand Edit</h4>
            <h6>Update your Brand</h6>
        </div>
    </div>

    <div class="card">
        <div class="card-body">
            <div class="row">
                <div class="col-lg-3 col-sm-6 col-12">
                    <div class="form-group">
                        <label>Brand Name</label>
                        <input type="text" value="samsung">
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="form-group">
                        <label>Description</label>
                        <textarea
                            class="form-control">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,</textarea>
                    </div>
                </div>
                <div class="col-lg-12">
                    <div class="form-group">
                        <label> Product Image</label>
                        <div class="image-upload">
                            <input type="file">
                            <div class="image-uploads">
                                <img src="/img/icons/upload.svg" alt="img">
                                <h4>Drag and drop a file to upload</h4>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12">
                    <div class="product-list">
                        <ul class="row">
                            <li>
                                <div class="productviews">
                                    <div class="productviewsimg">
                                        <img src="/img/brand/samsung.png" alt="img">
                                    </div>
                                    <div class="productviewscontent">
                                        <div class="productviewsname">
                                            <h2>samsung</h2>
                                            <h3>581kb</h3>
                                        </div>
                                        <a href="javascript:void(0);">x</a>
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-12">
                    <a href="javascript:void(0);" class="btn btn-submit me-2">Submit</a>
                    <router-link class="btn btn-cancel" @click="navigateTo('/index/brandlist')" to="/index/brandlist">
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