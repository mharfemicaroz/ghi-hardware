<template>
    <div class="page-header">
        <div class="page-title">
            <h4>Group Permissions</h4>
            <h6>Manage Group Permissions</h6>
        </div>
        <div class="page-btn">
            <a class="btn btn-added" href="createpermission.html"><img src="/img/icons/plus.svg" alt="img" class="me-1">Add
                Group Permission</a>
        </div>
    </div>

    <div class="card">
        <div class="card-body">
            <div class="table-top">
                <div class="search-set">
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
            <div class="table-responsive">
                <table class="table  datanew">
                    <thead>
                        <tr>
                            <th>
                                <label class="checkboxs">
                                    <input type="checkbox">
                                    <span class="checkmarks"></span>
                                </label>
                            </th>
                            <th>Role</th>
                            <th>description</th>
                            <th>Status</th>
                            <th class="text-end">Action</th>
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
                            <td>Admin</td>
                            <td>Owner</td>
                            <td>
                                <span class="badges bg-lightgreen">Active</span>
                            </td>
                            <td class="text-end">
                                <router-link class="me-3" @click="navigateTo('/index/editpermission')"
                                    to="/index/editpermission">
                                    <img src="/img/icons/edit.svg" alt="img">
                                </router-link>
                                <a class="me-3 confirm-text" href="javascript:void(0);">
                                    <img src="/img/icons/delete.svg" alt="img">
                                </a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label class="checkboxs">
                                    <input type="checkbox">
                                    <span class="checkmarks"></span>
                                </label>
                            </td>
                            <td>Purchase</td>
                            <td>Purchase Permission</td>
                            <td>
                                <span class="badges bg-lightgreen">Active</span>
                            </td>
                            <td class="text-end">
                                <router-link class="me-3" @click="navigateTo('/index/editpermission')"
                                    to="/index/editpermission">
                                    <img src="/img/icons/edit.svg" alt="img">
                                </router-link>
                                <a class="me-3 confirm-text" href="javascript:void(0);">
                                    <img src="/img/icons/delete.svg" alt="img">
                                </a>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <label class="checkboxs">
                                    <input type="checkbox">
                                    <span class="checkmarks"></span>
                                </label>
                            </td>
                            <td>Sales</td>
                            <td>Sales Permission</td>
                            <td>
                                <span class="badges bg-lightgreen">Active</span>
                            </td>
                            <td class="text-end">
                                <router-link class="me-3" @click="navigateTo('/index/editpermission')"
                                    to="/index/editpermission">
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