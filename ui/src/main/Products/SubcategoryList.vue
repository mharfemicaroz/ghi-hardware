<template>
    <div class="page-header">
        <div class="page-title">
            <h4>Product Sub Category list</h4>
            <h6>View/Search product Category</h6>
        </div>
        <div class="page-btn">
            <router-link class="btn btn-added" @click="navigateTo('/index/addsubcategory')" to="/index/addsubcategory">
                <img src="/img/icons/plus.svg" class="me-2" alt="img">
                Add Sub Category
            </router-link>
        </div>
    </div>

    <div class="card">
        <div class="card-body">
            <div class="table-top"> 
                <div class="search-set">
                    <div class="search-path">
                        <a class="btn btn-filter" id="filter_search">
                            <img src="/img/icons/filter.svg" alt="img">
                            <span><img src="/img/icons/closes.svg" alt="img"></span>
                        </a>
                    </div>
                    <div class="search-input">
                        <a class="btn btn-searchset"><img src="/img/icons/search-white.svg" alt="img"></a>
                    </div>
                </div>
                <div class="wordset">
                    <ul>
                        <li>
                            <a data-bs-toggle="tooltip" data-bs-placement="top" title="pdf"><img src="/img/icons/pdf.svg"
                                    alt="img"></a>
                        </li>
                        <li>
                            <a data-bs-toggle="tooltip" data-bs-placement="top" title="excel"><img
                                    src="/img/icons/excel.svg" alt="img"></a>
                        </li>
                        <li>
                            <a data-bs-toggle="tooltip" data-bs-placement="top" title="print"><img
                                    src="/img/icons/printer.svg" alt="img"></a>
                        </li>
                    </ul>
                </div>
            </div>

            <div class="card" id="filter_inputs">
                <div class="card-body pb-0">
                    <div class="row">
                        <div class="col-lg-2 col-sm-6 col-12">
                            <div class="form-group">
                                <label>Category</label>
                                <select class="select">
                                    <option>Choose Category</option>
                                    <option>Computers</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-lg-2 col-sm-6 col-12">
                            <div class="form-group">
                                <label>Sub Category</label>
                                <select class="select">
                                    <option>Choose Sub Category</option>
                                    <option>Fruits</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-lg-2 col-sm-6 col-12">
                            <div class="form-group">
                                <label>Category Code</label>
                                <select class="select">
                                    <option>CT001</option>
                                    <option>CT002</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-lg-1 col-sm-6 col-12 ms-auto">
                            <div class="form-group">
                                <label>&nbsp;</label>
                                <a class="btn btn-filters ms-auto"><img src="/img/icons/search-whites.svg" alt="img"></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="table-responsive">
                <table class="table  datanew">
                    <thead>
                        <tr>
                            <th>
                                <label class="checkboxs">
                                    <input type="checkbox" id="select-all">
                                    <span class="checkmarks"></span>
                                </label>
                            </th>
                            <th>Image</th>
                            <th>Category</th>
                            <th>Parent category</th>
                            <th>Category Code</th>
                            <th>Description</th>
                            <th>Created By</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <label class="checkboxs">
                                    <input type="checkbox">
                                    <span class="checkmarks"></span>
                                </label>
                            </td>
                            <td>
                                <a class="product-img">
                                    <img src="/img/product/product10.jpg" alt="product">
                                </a>
                            </td>
                            <td>Health Care </td>
                            <td>Health Care </td>
                            <td>CT0010</td>
                            <td>Health Care Description</td>
                            <td>Admin</td>
                            <td>
                                <router-link class="me-3" @click="navigateTo('/index/editsubcategory')" to="/index/editsubcategory">
                                    <img src="/img/icons/edit.svg" alt="img">
                                </router-link>
                                <a class="me-3 confirm-text" href="javascript:void(0);">
                                    <img src="/img/icons/delete.svg" alt="img">
                                </a>
                            </td>
                        </tr>
                    </tbody>
                </table>
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