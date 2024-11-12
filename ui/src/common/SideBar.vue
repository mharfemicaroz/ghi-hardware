<template>
  <div class="sidebar" id="sidebar">
    <div class="sidebar-inner slimscroll">
      <div id="sidebar-menu" class="sidebar-menu">
        <ul>
          <SidebarMenuItem
            v-for="(item, index) in menuItems"
            :key="index"
            :item="item"
            @navigate="navigateTo"
            :route="$route.path"
          />
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import SidebarMenuItem from "./SidebarMenuItem.vue";

export default {
  components: { SidebarMenuItem },
  data() {
    return {
      menuItems: [
        {
          label: "Dashboard",
          icon: "/img/icons/dashboard.svg",
          route: "/index/dashboard",
        },
        {
          label: "Product",
          icon: "/img/icons/product.svg",
          submenu: [
            { label: "Product List", route: "/index/productlist" },
            { label: "Add Product", route: "/index/addproduct" },
            { label: "Category List", route: "/index/categorylist" },
            { label: "Add Category", route: "/index/addcategory" },
            { label: "Sub Category List", route: "/index/subcategorylist" },
            { label: "Add Sub Category", route: "/index/addsubcategory" },
            { label: "Brand List", route: "/index/brandlist" },
            { label: "Add Brand", route: "/index/addbrand" },
            { label: "Voucher List", route: "/index/voucherlist" },
            { label: "Add Voucher", route: "/index/addvoucher" },
          ],
        },
        {
          label: "Sales",
          icon: "/img/icons/sales1.svg",
          submenu: [
            { label: "Sales List", route: "/index/saleslist" },
            { label: "Add Sales", route: "/index/salesadd" },
            { label: "POS", route: "/pos", newTab: true },
          ],
        },
        {
          label: "Purchase",
          icon: "/img/icons/purchase1.svg",
          submenu: [
            { label: "Purchase List", route: "/index/purchaselist" },
            { label: "Add Purchase", route: "/index/addpurchase" },
          ],
        },
        {
          label: "People",
          icon: "/img/icons/expense1.svg",
          submenu: [
            { label: "Customer List", route: "/index/customerlist" },
            { label: "Add Customer", route: "/index/customeradd" },
            {
              label: "Supplier List",
              route: "/index/supplierlist",
            },
            {
              label: "Add Supplier",
              route: "/index/supplieradd",
            },
          ],
        },
      ],
    };
  },
  methods: {
    navigateTo(item) {
      if (item.newTab) {
        window.open(item.route, "_blank");
      } else {
        localStorage.setItem("savedPath", item.route);
        this.$router.push(item.route);
      }
    },
  },
};
</script>
