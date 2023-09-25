<template>
  <div class="sidebar" id="sidebar">
    <div class="sidebar-inner slimscroll">
      <div id="sidebar-menu" class="sidebar-menu">
        <ul>
          <li :class="getActiveMenu('/index/dashboard')">
            <router-link
              @click="navigateTo('/index/dashboard')"
              to="/index/dashboard"
            >
              <a href="#"
                ><img src="/img/icons/dashboard.svg" alt="img" /><span>
                  Dashboard</span
                >
              </a>
            </router-link>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/product.svg" alt="img" /><span>
                Product</span
              >
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/productlist')"
                  @click="navigateTo('/index/productlist')"
                  to="/index/productlist"
                >
                  <span>Product List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addproduct')"
                  @click="navigateTo('/index/addproduct')"
                  to="/index/addproduct"
                >
                  <span>Add Product</span>
                </router-link>
              </li>
              <!-- <li> <router-link :class="getActiveMenu('/index/editproduct')"
                                    @click="navigateTo('/index/editproduct')" to="/index/editproduct">
                                    <span>Edit Product</span>
                                </router-link></li> -->
              <!-- <li>
                <router-link
                  :class="getActiveMenu('/index/productdetails')"
                  @click="navigateTo('/index/productdetails')"
                  to="/index/productdetails"
                >
                  <span>Product Details</span>
                </router-link>
              </li> -->
              <li>
                <router-link
                  :class="getActiveMenu('/index/categorylist')"
                  @click="navigateTo('/index/categorylist')"
                  to="/index/categorylist"
                >
                  <span>Category List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addcategory')"
                  @click="navigateTo('/index/addcategory')"
                  to="/index/addcategory"
                >
                  <span>Add Category</span>
                </router-link>
              </li>
              <!-- <li> <router-link :class="getActiveMenu('/index/editcategory')"
                                    @click="navigateTo('/index/editcategory')" to="/index/editcategory">
                                    <span>Edit Category</span>
                                </router-link></li> -->
              <li>
                <router-link
                  :class="getActiveMenu('/index/subcategorylist')"
                  @click="navigateTo('/index/subcategorylist')"
                  to="/index/subcategorylist"
                >
                  <span>Sub Category List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addsubcategory')"
                  @click="navigateTo('/index/addsubcategory')"
                  to="/index/addsubcategory"
                >
                  <span>Add Sub Category</span>
                </router-link>
              </li>
              <!-- <li> <router-link :class="getActiveMenu('/index/editsubcategory')"
                                    @click="navigateTo('/index/editsubcategory')" to="/index/editsubcategory">
                                    <span>Edit Sub Category</span>
                                </router-link></li> -->
              <li>
                <router-link
                  :class="getActiveMenu('/index/brandlist')"
                  @click="navigateTo('/index/brandlist')"
                  to="/index/brandlist"
                >
                  <span>Brand List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addbrand')"
                  @click="navigateTo('/index/addbrand')"
                  to="/index/addbrand"
                >
                  <span>Add Brand</span>
                </router-link>
              </li>
              <!-- <li> <router-link :class="getActiveMenu('/index/editbrand')"
                                    @click="navigateTo('/index/editbrand')" to="/index/editbrand">
                                    <span>Edit Brand</span>
                                </router-link></li> -->
              <!-- <li>
                <router-link
                  :class="getActiveMenu('/index/importproduct')"
                  @click="navigateTo('/index/importproduct')"
                  to="/index/importproduct"
                >
                  <span>Import Products</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/printbarcode')"
                  @click="navigateTo('/index/printbarcode')"
                  to="/index/printbarcode"
                >
                  <span>Print Barcode</span>
                </router-link>
              </li> -->
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/sales1.svg" alt="img" /><span> Sales</span>
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/saleslist')"
                  @click="navigateTo('/index/saleslist')"
                  to="/index/saleslist"
                >
                  <span>Sales List</span>
                </router-link>
              </li>
              <li>
                <a href="#" @click="openNewTab" to="/pos">
                  <span>POS</span>
                </a>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/salesreturnlist')"
                  @click="navigateTo('/index/salesreturnlist')"
                  to="/index/salesreturnlist"
                >
                  <span>Sales Return List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/newsalesreturnlist')"
                  @click="navigateTo('/index/newsalesreturnlist')"
                  to="/index/newsalesreturnlist"
                >
                  <span>New Sales Return</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/purchase1.svg" alt="img" /><span>
                Purchase</span
              >
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/purchaselist')"
                  @click="navigateTo('/index/purchaselist')"
                  to="/index/purchaselist"
                >
                  <span>Purchase List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addpurchase')"
                  @click="navigateTo('/index/addpurchase')"
                  to="/index/addpurchase"
                >
                  <span>Add Purchase</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/importpurchase')"
                  @click="navigateTo('/index/importpurchase')"
                  to="/index/importpurchase"
                >
                  <span>Import Purchase</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/expense1.svg" alt="img" /><span>
                Expense</span
              >
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/expenselist')"
                  @click="navigateTo('/index/expenselist')"
                  to="/index/expenselist"
                >
                  <span>Expense List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/createexpense')"
                  @click="navigateTo('/index/createexpense')"
                  to="/index/createexpense"
                >
                  <span>Add Expense</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/expensecategorylist')"
                  @click="navigateTo('/index/expensecategorylist')"
                  to="/index/expensecategorylist"
                >
                  <span>Expense Category List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addexpensecategory')"
                  @click="navigateTo('/index/addexpensecategory')"
                  to="/index/addexpensecategory"
                >
                  <span>Add Expense Category</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/quotation1.svg" alt="img" /><span>
                Quotation</span
              >
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/quotationlist')"
                  @click="navigateTo('/index/quotationlist')"
                  to="/index/quotationlist"
                >
                  <span>Quotation List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addquotation')"
                  @click="navigateTo('/index/addquotation')"
                  to="/index/addquotation"
                >
                  <span>Add Quotation</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/transfer1.svg" alt="img" /><span>
                Transfer</span
              >
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/transferlist')"
                  @click="navigateTo('/index/transferlist')"
                  to="/index/transferlist"
                >
                  <span>Transfer List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/addtransfer')"
                  @click="navigateTo('/index/addtransfer')"
                  to="/index/addtransfer"
                >
                  <span>Add Transfer</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/importtransfer')"
                  @click="navigateTo('/index/importtransfer')"
                  to="/index/importtransfer"
                >
                  <span>Import Transfer</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/return1.svg" alt="img" /><span>
                Return</span
              >
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/salesreturnlist')"
                  @click="navigateTo('/index/salesreturnlist')"
                  to="/index/salesreturnlist"
                >
                  <span>Sales Return List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/newsalesreturnlist')"
                  @click="navigateTo('/index/newsalesreturnlist')"
                  to="/index/newsalesreturnlist"
                >
                  <span>New Sales Return</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/purchasereturnlist')"
                  @click="navigateTo('/index/purchasereturnlist')"
                  to="/index/purchasereturnlist"
                >
                  <span>Purchase Return List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/newpurchasereturnlist')"
                  @click="navigateTo('/index/newpurchasereturnlist')"
                  to="/index/newpurchasereturnlist"
                >
                  <span>New Purchase Return</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/users1.svg" alt="img" /><span> People</span>
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/customerlist')"
                  @click="navigateTo('/index/customerlist')"
                  to="/index/customerlist"
                >
                  <span>Customer List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/customeradd')"
                  @click="navigateTo('/index/customeradd')"
                  to="/index/customeradd"
                >
                  <span>Add Customer</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/supplierlist')"
                  @click="navigateTo('/index/supplierlist')"
                  to="/index/supplierlist"
                >
                  <span>Supplier List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/supplieradd')"
                  @click="navigateTo('/index/supplieradd')"
                  to="/index/supplieradd"
                >
                  <span>Add Supplier</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/userlist')"
                  @click="navigateTo('/index/userlist')"
                  to="/index/userlist"
                >
                  <span>User List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/useradd')"
                  @click="navigateTo('/index/useradd')"
                  to="/index/useradd"
                >
                  <span>Add User</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/storelist')"
                  @click="navigateTo('/index/storelist')"
                  to="/index/storelist"
                >
                  <span>Store List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/storeadd')"
                  @click="navigateTo('/index/storeadd')"
                  to="/index/storeadd"
                >
                  <span>Add Store</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/time.svg" alt="img" /><span> Report</span>
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/purchaseorderreport')"
                  @click="navigateTo('/index/purchaseorderreport')"
                  to="/index/purchaseorderreport"
                >
                  <span>Purchase Order Report</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/inventoryreport')"
                  @click="navigateTo('/index/inventoryreport')"
                  to="/index/inventoryreport"
                >
                  <span>Inventory Report</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/salesreport')"
                  @click="navigateTo('/index/salesreport')"
                  to="/index/salesreport"
                >
                  <span>Sales Report</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/invoicereport')"
                  @click="navigateTo('/index/invoicereport')"
                  to="/index/invoicereport"
                >
                  <span>Invoice Report</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/purchasereport')"
                  @click="navigateTo('/index/purchasereport')"
                  to="/index/purchasereport"
                >
                  <span>Purchase Report</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/supplierreport')"
                  @click="navigateTo('/index/supplierreport')"
                  to="/index/supplierreport"
                >
                  <span>Supplier Report</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/customerreport')"
                  @click="navigateTo('/index/customerreport')"
                  to="/index/customerreport"
                >
                  <span>Customer Report</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/users1.svg" alt="img" /><span> Users</span>
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/userlist')"
                  @click="navigateTo('/index/userlist')"
                  to="/index/userlist"
                >
                  <span>User List</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/useradd')"
                  @click="navigateTo('/index/useradd')"
                  to="/index/useradd"
                >
                  <span>Add User</span>
                </router-link>
              </li>
            </ul>
          </li>
          <li class="submenu">
            <a href="javascript:void(0);"
              ><img src="/img/icons/settings.svg" alt="img" /><span>
                Settings</span
              >
              <span class="menu-arrow"></span
            ></a>
            <ul>
              <li>
                <router-link
                  :class="getActiveMenu('/index/generalsettings')"
                  @click="navigateTo('/index/generalsettings')"
                  to="/index/generalsettings"
                >
                  <span>General Settings</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/emailsettings')"
                  @click="navigateTo('/index/emailsettings')"
                  to="/index/emailsettings"
                >
                  <span>Email Settings</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/paymentsettings')"
                  @click="navigateTo('/index/paymentsettings')"
                  to="/index/paymentsettings"
                >
                  <span>Payment Settings</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/currencysettings')"
                  @click="navigateTo('/index/currencysettings')"
                  to="/index/currencysettings"
                >
                  <span>Currency Settings</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/grouppermissions')"
                  @click="navigateTo('/index/grouppermissions')"
                  to="/index/grouppermissions"
                >
                  <span>Group Permissions</span>
                </router-link>
              </li>
              <li>
                <router-link
                  :class="getActiveMenu('/index/taxrates')"
                  @click="navigateTo('/index/taxrates')"
                  to="/index/taxrates"
                >
                  <span>Tax Rates</span>
                </router-link>
              </li>
            </ul>
          </li>
        </ul>
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
    getActiveMenu(path) {
      const activePath = localStorage.getItem("savedPath");
      if (path === activePath) {
        return "active";
      } else {
        return "";
      }
    },
    openNewTab() {
      const routeData = this.$router.resolve({ name: "PointofSale" });
      window.open(routeData.href, "_blank");
    },
  },
};
</script>
<style></style>
